# [*CKV*-website](https://ckv.gijs6.nl/)

At my school, everyone has to make a website for the subject CKV (*culturele en kunstzinnige vorming*, basically "culture and art") for all reports, reflections, and those kinds of things. The idea is to have a personal space everyone can update easily. Practically everyone just uses Wix because it's easy to use and requires no coding, but I built mine from scratch :D

I built it with [Flask](https://github.com/pallets/flask) and [Jinja](https://github.com/pallets/jinja). I could easily use a static site generator, but I like just being able to simply write some code for each request, and just writing the HTML myself works fine.

## Run yourself

Clone the repo, install dependencies with `pip install -r requirements.txt` and run the web app with `flask --app main run`.
