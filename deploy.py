from datetime import datetime
import os
import re
import subprocess

# Fetch and reset repo
subprocess.run(["git", "fetch"], check=True)
print("Fetched")
subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
print("Updated files")

# Directories and files to exclude
EXCLUDE_DIRS = [".venv", ".git", "__pycache__"]
EXCLUDE_FILES = ["deploy.py"]


def get_comment_syntax(filename):
    if filename.endswith(".js"):
        return "// start devb", "// end devb"
    elif filename.endswith(".py") and not filename.endswith(".pyc"):
        return "# start devb", "# end devb"
    elif filename.endswith(".html"):
        return "<!-- start devb -->", "<!-- end devb -->"
    elif filename.endswith(".css"):
        return "/* start devb */", "/* end devb */"
    else:
        return None, None


def remove_dev_blocks(file_path, start_comment, end_comment):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Processing: {file_path}")

    pattern = rf"{re.escape(start_comment)}.*?{re.escape(end_comment)}\n?"
    updated_content = re.sub(pattern, "", content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)


for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    for file in files:
        if file in EXCLUDE_FILES:
            continue  # Skip excluded files

        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            start_comment, end_comment = get_comment_syntax(file_path)
            if start_comment and end_comment:
                remove_dev_blocks(file_path, start_comment, end_comment)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, "data", "last_deploy.txt"), "w") as file:
    file.write(datetime.now().strftime("%d-%m-%Y at %H:%M:%S"))


subprocess.run(["touch", "/var/www/ckv_gijs6_nl_wsgi.py"], check=True)
print("Redeployed page")
