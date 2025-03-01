# Conventions  

*Just to make the website look a **little** less chaotic and to make my code a bit less awful* 

***This file is completely unnecessary, but I started on this so I must finish it!***

## Style things

- Text describing the content of a page is in a **green** *kleurvak binnen-buiten*.  
- Border-radius is **20px**.  
- Artwork titles have a font-weight of **500**, and artist names are **800**.  
- All text that is **not** an artist's name or artwork title (within an artwork's description, so near a video, image, audio, ...) is *italic*.  
- The two rules above apply only to text **directly related** to an artwork (near a video, image, audio, ...). In other cases, all names (both artwork and artist) are *italic*.  
- All elements inside the `content`-div are in `<div>`'s with the class `"paginablok"`.  
- The *paginablok* for *Kleine verklaring & uitleg* is in a **red** *kleurvak binnen-buiten*.  

## Other things
- Place styles in the CSS file where they are loaded on as few pages as necessary.  
- `ckvbasis.css` contains only styles that are used across multiple pages.  
- The alt tag of an image should be in the same lang as the page (so Dutch for this site)
- The alt tag of an artwork should be `{artwork (including year)} - {artist}`
- The alt tag of all other kinds of images should be sort descriptive tags of the content of the images
- Images that are solely used for aesthetic purposes do not need an alt tag.
