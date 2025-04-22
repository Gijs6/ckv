# [*CKV*-website](https://ckv.gijs6.nl/)

At my school, everyone has to make a website for the subject CKV (*culturele en kunstzinnige vorming*, so basically "culture and art") for all reports, reflections, and those kinds of things. The idea is to have a personal space everyone can update easily. Practically everyone just uses Wix because it's easy to use and requires no coding.

But I decided to build mine from scratch, because I like having full control over every detail. With Wix, you're stuck with whatever features they offer *(for free, I'm not paying! (...yeah I am paying for the hosting and the domain (well I already had a subscription to PythonAnywhere and I already had the domain, so I'm not really paying anything extra), but I'm not paying for features!!!))*, but by coding it myself, I can do literally everything to my liking (well, not *everything*, browsers still have their limits, but **definitely** more than what Wix allows).

So while everyone else is dragging and dropping in Wix and working with stupidly large margins, I'm over here figuring out Flask routes and how to style an audio player and how I can fix one item not stretching with flex-grow when it's the only item on the row because of flex-wrap, but the other items do need to stretch <small>(if someone knows, please [mail](mailto:gijs6@dupunkto.org) me!)</small>. It will definitely take longer, and I will definitely be annoyed by some very stupid bugs and some very annoying style stuff, but it will feel at least like my own website.

***

Built with [Flask](https://github.com/pallets/flask) and [Jinja](https://github.com/pallets/jinja) (yeah I like Flask, it is just simple but amazing). I could easily use a static site generator, but I like styling everything and just being able simply write some code for each requests, so just writing the HTML myself works the best.

## Run yourself

If you want to run the site yourself, just clone this repo, install all the required packages via `pip install -r requirements.txt` and run `py main.py` (`flask --app main run` also works, but that could be with some diffrent settings). You can then visit the site at `localhost:5000` (or another link, the correct link will be printed in the terminal).
