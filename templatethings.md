# Things for B5 en B6 that I don't want to lose

*... so I just dumped it here*

HTML

```
{% block content %}
    <div class="pageblock bloknietbegonnen">
        <span class="bloknietbegonnenblok">Blok</span>
        <div class="bloknietbegonnennumsdiv">
            <span class="numrij-12">4</span>
            <span class="numrij-11">4</span>
            <span class="numrij-10">4</span>
            <span class="numrij-9">4</span>
            <span class="numrij-8">4</span>
            <span class="numrij-7">4</span>
            <span class="numrij-6">4</span>
            <span class="numrij-5">4</span>
            <span class="numrij-4">4</span>
            <span class="numrij-3">4</span>
            <span class="numrij-2">4</span>
            <span class="numrij-1">4</span>
            <span class="numrij-0">4</span>
            <span class="numrij-1">4</span>
            <span class="numrij-2">4</span>
            <span class="numrij-3">4</span>
            <span class="numrij-4">4</span>
            <span class="numrij-5">4</span>
            <span class="numrij-6">4</span>
            <span class="numrij-7">4</span>
            <span class="numrij-8">4</span>
            <span class="numrij-9">4</span>
            <span class="numrij-10">4</span>
            <span class="numrij-11">4</span>
            <span class="numrij-12">4</span>
        </div>
        <span class="bloknietbegonnentekst">Deze pagina is nog niet beschikbaar. Kom later terug!</span>
    </div>
{% endblock %}
```


CSS

```


/* Nog niet begonnen blokpags */


.bloknietbegonnen {
    flex-grow: 1;
    background: var(--geel);
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    flex-direction: column;
}

.bloknietbegonnenblok {
    font-size: 6em;
}

.bloknietbegonnennumsdiv span {
    transition: all 250ms ease;
    opacity: 0;
}

.bloknietbegonnentekst {
    font-size: 1.5em;
}

.bloknietbegonnennumsdiv {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    position: relative;
    gap: 2px;
}



.numrij-12 {
    font-size: 0.4em;
    font-weight: 100;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 1200ms;
}

.numrij-11 {
    font-size: 0.6em;
    font-weight: 100;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 1100ms;
}

.numrij-10 {
    font-size: 0.8em;
    font-weight: 100;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 1000ms;
}

.numrij-9 {
    font-size: 1.1em;
    font-weight: 100;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 900ms;
}
.numrij-8 {
    font-size: 1.4em;
    font-weight: 100;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 800ms;
}

.numrij-7 {
    font-size: 1.9em;
    font-weight: 200;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 700ms;
}

.numrij-6 {
    font-size: 2.5em;
    font-weight: 300;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 600ms;
}

.numrij-5 {
    font-size: 3.3em;
    font-weight: 400;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 500ms;
}

.numrij-4 {
    font-size: 4.4em;
    font-weight: 500;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 400ms;
}

.numrij-3 {
    font-size: 5.9em;
    font-weight: 600;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 300ms;
}

.numrij-2 {
    font-size: 7.9em;
    font-weight: 700;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 200ms;
}

.numrij-1 {
    font-size: 10.5em;
    font-weight: 800;
    animation: fadein 150ms ease-in-out forwards;
    animation-delay: 100ms;
}

.numrij-0 {
    font-size: 17em;
    font-weight: 900;
    animation: fadein 150ms ease-in-out forwards;
}


.numrij-12:hover {
    font-size: 0.6em;
}

.numrij-11:hover {
    font-size: 0.8em;
}

.numrij-10:hover {
    font-size: 1.1em;
}

.numrij-9:hover {
    font-size: 1.4em;
}

.numrij-8:hover {
    font-size: 1.9em;
}

.numrij-7:hover {
    font-size: 2.5em;
}

.numrij-6:hover {
    font-size: 3.3em;
}

.numrij-5:hover {
    font-size: 4.4em;
}

.numrij-4:hover {
    font-size: 5.9em;
}

.numrij-3:hover {
    font-size: 7.9em;
}

.numrij-2:hover {
    font-size: 10.5em;
}

.numrij-1:hover {
    font-size: 14em;
}

.numrij-0:hover {
    font-size: 18.7em;
}





@keyframes fadein {
    0% {
        opacity: 0%;
    }
    100% {
        opacity: 100%;
    }
}

```