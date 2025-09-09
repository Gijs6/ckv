#!/usr/bin/env python3

import os
import sys
import shutil
import json
import subprocess
import time
import threading
import argparse
from datetime import datetime
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from tqdm import tqdm
from colorama import Fore, Style, init
import random

init()


class StaticSiteBuilder:
    def __init__(self, site_dir="site", build_dir="build"):
        self.site_dir = Path(site_dir)
        self.build_dir = Path(build_dir)
        self.base_dir = Path(__file__).parent
        
        # Set up Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.site_dir / "templates"),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        # Add custom functions for static site generation
        self.env.globals['url_for'] = self._url_for
        self.env.globals['request'] = self._create_mock_request()
        
    def _url_for(self, endpoint, **values):
        """Custom url_for function for static site generation"""
        if endpoint == 'static':
            filename = values.get('filename', '')
            return f'/static/{filename}'
        
        # Handle route endpoints
        route_map = {
            'home': '/gijstenberg4a2/',
            'about_me': '/gijstenberg4a2/over-mij/',
            'intro': '/gijstenberg4a2/introductielessen/',
            'own_initiatives': '/gijstenberg4a2/eigen-initiatieven/',
            'period_1': '/gijstenberg4a2/blok-1/',
            'period_2': '/gijstenberg4a2/blok-2/',
            'period_3': '/gijstenberg4a2/blok-3/',
            'period_4': '/gijstenberg4a2/blok-4/',
            'period_5': '/gijstenberg4a2/blok-5/',
            'period_6': '/gijstenberg4a2/blok-6/',
            'final_report': '/gijstenberg4a2/eindverslag/',
            'favicon': '/favicon.ico',
            'robots': '/robots.txt',
            'security_txt': '/.well-known/security.txt',
        }
        
        return route_map.get(endpoint, f'/{endpoint}/')
    
    def _create_mock_request(self):
        """Create a mock request object for templates"""
        class MockRequest:
            def __init__(self):
                self.path = '/'
                
        return MockRequest()
        
    def clean_build_dir(self):
        """Remove and recreate build directory"""
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
        self.build_dir.mkdir(exist_ok=True)
        
    def copy_static_files(self):
        """Copy all static files to build directory"""
        static_src = self.site_dir / "static"
        static_dest = self.build_dir / "static"
        
        if static_src.exists():
            shutil.copytree(static_src, static_dest)
            
    def get_commit_and_deploy_data(self):
        """Get git commit info and deploy timestamp"""
        try:
            with open(self.site_dir / "data" / "last_deploy.txt", "r") as f:
                latest_deploy_date = f.read().strip()
        except FileNotFoundError:
            latest_deploy_date = "unknown"
            
        try:
            latest_commit_hash = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%h"], 
                cwd=self.base_dir
            ).strip().decode()
            
            latest_commit_hash_long = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%H"], 
                cwd=self.base_dir
            ).strip().decode()
            
            latest_commit_timestamp = int(subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%ct"], 
                cwd=self.base_dir
            ).strip())
            
            latest_commit_date = datetime.fromtimestamp(latest_commit_timestamp).strftime(
                "%d-%m-%Y om %H:%M:%S"
            )
        except subprocess.CalledProcessError:
            latest_commit_hash = "unknown"
            latest_commit_hash_long = "unknown"
            latest_commit_date = "unknown"
            
        return {
            "latest_deploy_date": latest_deploy_date,
            "latest_commit_hash": latest_commit_hash,
            "latest_commit_hash_long": latest_commit_hash_long,
            "latest_commit_date": latest_commit_date,
        }
        
    def get_random_background(self):
        """Get random background for error pages"""
        try:
            with open(self.site_dir / "data" / "backgroundlist.json", "r") as file:
                data = json.load(file)
            random_choice = random.choice(data)
            
            return (
                random_choice.get("imgurl"),
                random_choice.get("artwork"),
                random_choice.get("artist"),
                random_choice.get("txtcolor"),
            )
        except Exception:
            return (
                "/static/imgs/error/primordial_chaos.jpg",
                "Primordial Chaos - No 16 (1906-1907)",
                "Hilma af Klint",
                "white",
            )
            
    def render_page(self, template_name, output_path, **context):
        """Render a single page"""
        template = self.env.get_template(template_name)
        
        # Set the request path for active menu highlighting
        page_path = "/" + output_path.replace("/index.html", "").replace("index.html", "")
        if page_path.endswith("/"):
            page_path = page_path[:-1]
        
        # Create a new mock request for this page
        mock_request = self._create_mock_request()
        mock_request.path = page_path
        
        # Add global context
        commit_data = self.get_commit_and_deploy_data()
        context.update(commit_data)
        context['request'] = mock_request
        
        html = template.render(**context)
        
        # Ensure output directory exists
        output_file = self.build_dir / output_path
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
            
    def build_pages(self):
        """Build all pages"""
        pages = [
            ("home.html", "gijstenberg4a2/index.html"),
            ("about_me.html", "gijstenberg4a2/over-mij/index.html"),
            ("intro.html", "gijstenberg4a2/introductielessen/index.html"),
            ("own_ini.html", "gijstenberg4a2/eigen-initiatieven/index.html"),
            ("period_1.html", "gijstenberg4a2/blok-1/index.html"),
            ("period_2.html", "gijstenberg4a2/blok-2/index.html"),
            ("period_3.html", "gijstenberg4a2/blok-3/index.html"),
            ("period_4.html", "gijstenberg4a2/blok-4/index.html"),
            ("period_5.html", "gijstenberg4a2/blok-5/index.html"),
            ("period_6.html", "gijstenberg4a2/blok-6/index.html"),
            ("final_report.html", "gijstenberg4a2/eindverslag/index.html"),
        ]
        
        for template_name, output_path in pages:
            self.render_page(template_name, output_path)
            
        # Create root redirect
        self.render_page("redirect.html", "index.html", redirect_url="/gijstenberg4a2/")
        
        # Create 404 page
        imgurl, artwork, artist, txtcolor = self.get_random_background()
        self.render_page(
            "error.html", 
            "404.html",
            errornum="404",
            message1="Deze pagina bestaat niet!",
            message2="De URL die je hebt opgevraagd bestaat niet.",
            imgurl=imgurl,
            artwork=artwork,
            artist=artist,
            txtcolor=txtcolor
        )
        
    def create_special_files(self):
        """Create special files like favicon, robots.txt, etc."""
        # Copy favicon
        favicon_src = self.site_dir / "static" / "favs" / "main.ico"
        if favicon_src.exists():
            shutil.copy(favicon_src, self.build_dir / "favicon.ico")
            
        # Copy robots.txt and security.txt
        for filename in ["robots.txt", "security.txt"]:
            src = self.site_dir / "static" / filename
            if src.exists():
                shutil.copy(src, self.build_dir / filename)
                
        # Create .well-known directory for security.txt
        wellknown_dir = self.build_dir / ".well-known"
        wellknown_dir.mkdir(exist_ok=True)
        if (self.site_dir / "static" / "security.txt").exists():
            shutil.copy(
                self.site_dir / "static" / "security.txt",
                wellknown_dir / "security.txt"
            )
            
    def build(self):
        """Main build process with progress bar and colorful output"""
        print(f"{Fore.CYAN}=> Building CKV Site <={Style.RESET_ALL}")
        
        tasks = [
            ("Cleaning", self.clean_build_dir),
            ("Static Files", self.copy_static_files),
            ("Pages", self.build_pages),
            ("Special Files", self.create_special_files),
        ]
        
        with tqdm(
            total=len(tasks),
            desc="Building",
            bar_format="{desc}[{bar:60}] {percentage:3.0f}%",
            ascii="-#",
        ) as pbar:
            for desc, task in tasks:
                pbar.set_description(desc)
                task()
                pbar.update(1)
        
        print(f"{Fore.GREEN}Build complete!{Style.RESET_ALL}\n")
        print(f"{Fore.BLUE}Output directory: {Style.BRIGHT}{self.build_dir}{Style.RESET_ALL}")


class BuildHandler(FileSystemEventHandler):
    def __init__(self, build_func):
        self.build_func = build_func
        self.last_build = 0

    def on_modified(self, event):
        if event.is_directory:
            return

        # Ignore build directory changes
        if "build/" in event.src_path:
            return

        # Debounce builds (max once per second)
        now = time.time()
        if now - self.last_build < 1:
            return

        self.last_build = now
        filename = os.path.basename(event.src_path)
        print(
            f"\n{Fore.YELLOW}Restarting! {Style.BRIGHT}{filename} has changed.{Style.RESET_ALL}\n"
        )
        self.build_func()


class DevHTTPServer(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="build", **kwargs)


def build():
    """Standalone build function"""
    builder = StaticSiteBuilder()
    builder.build()


def serve(port=8000):
    """Development server with file watching"""
    print(f"{Fore.BLUE}Development server{Style.RESET_ALL}\n")

    # Initial build
    build()

    # Set up file watcher
    event_handler = BuildHandler(build)
    observer = Observer()
    observer.schedule(event_handler, "site", recursive=True)
    observer.start()

    # Start HTTP server in a separate thread
    server = HTTPServer(("localhost", port), DevHTTPServer)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print(
        f"{Fore.GREEN}Serving on {Style.BRIGHT}http://localhost:{port}{Style.RESET_ALL}"
    )
    print(f"{Fore.MAGENTA}Watching for changes...{Style.RESET_ALL}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Stopping server...{Style.RESET_ALL}")
        observer.stop()
        server.shutdown()
        observer.join()


def main():
    parser = argparse.ArgumentParser(description="CKV Site Builder")
    parser.add_argument(
        "command",
        nargs="?",
        default="build",
        choices=["build", "serve"],
        help="Command to run (default: build)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for development server (default: 8000)",
    )

    args = parser.parse_args()

    if args.command == "serve":
        serve(args.port)
    else:
        build()


if __name__ == "__main__":
    main()