# [*CKV*-website](https://ckv.gijs6.nl/)

At my school, everyone has to make a website for the subject CKV (*culturele en kunstzinnige vorming*, so basically "culture and art") for all reports, reflections, and those kinds of things. The idea is to have a personal space everyone can update easily. Practically everyone just uses Wix because it's easy to use and requires no coding.

But I decided to build mine from scratch, because I like having full control over every detail. With Wix, you're stuck with whatever features they offer *(for free, I'm not paying! (...yeah I am paying for the hosting and the domain (well I already had a subscription to PythonAnywhere and I already had the domain, so I'm not really paying anything extra), but I'm not paying for features!!!))*, but by coding it myself, I can do literally everything to my liking (well, not *everything*, browsers still have their limits, but **definitely** more than what Wix allows).

So while everyone else is dragging and dropping in Wix and working with stupidly large margins, I'm over here figuring out Flask routes and how to style an audio player and how I can fix one item not stretching with flex-grow when it's the only item on the row because of flex-wrap, but the other items do need to stretch <small>(if someone knows, please [mail](mailto:gijs6@dupunkto.org) me!)</small>. It will definitely take longer, and I will definitely be annoyed by some very stupid bugs and some very annoying style stuff, but it will feel at least like my own website.

***

Built with [Flask](https://github.com/pallets/flask) and [Jinja](https://github.com/pallets/jinja) (yeah I like Flask, it is just simple but amazing). I could easily use a static site generator, but I like styling everything, so just writing the HTML myself works the best.

If you want to run the site yourself, just clone this repo, install Flask via `pip install flask`, and run `py main.py` (or `python3 main.py` or just whatever works). You can then visit the site at `localhost:5000` (or another link, the correct link will be printed in the terminal). If you just open the HTML files, the menu and base of the pages won't load correctly.

***

*Nu alleen nog 5 punten halen overal op die rubrics...😉*

*Waarschijnlijk spreek je gewoon Nederlands en vraag je je af waarom dit in hemelsnaam in het Engels staat. Simpel: dat is hier de norm. En jij begrijpt dit waarschijnlijk prima - terwijl je het eigenlijk niet eens **hoeft** te begrijpen.*

***

## To do list

- [x] Add alt txt to images (-> see conventions)
- [x] Start on page *Blok 3*
  - [x] Pick image or video for background page title
  - [x] Write *algemene informatie*
  - [x] Choose form for *tussenverslag* and for the general page content (-> just text (like blok 1) but more in the *flow* of the tussenverslag and in a nicer order)
  - [ ] Write (or create, depending on the form) the tussenverslag
- [ ] Rewrite
  - [x] Rewrite *Blok 1*
    - [x] Rewrite *over mij*
    - [ ] Rewrite short informative txt's
    - [ ] Rewrite *Blok 2* (mostly the infograpic)
- [x] Better 404 and 500 pages (with art from Mondriaan?)
- [x] **Fix layout*** (and images) on popups in infograpic (blok 2)!
- [ ] Quicker loading times for the vid on blok 1
- [x] Add new artworks to the randombackgrounds-list for the errorpages
- [ ] Make a bit mobile friendly (not media querys for **everyting** but adjusting the font-size and those kinds of things); just improve the *uSeR eXpErIeNcE* for mobile

