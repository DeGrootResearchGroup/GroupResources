# Research presentation template

A Quarto revealjs starter for research talks, defenses and group meetings: Western purple
headings, a fixed footer bar (Western Engineering logo, deck title, slide number), and a fixed
16:9 slide size so the deck doesn't "float" like a plain web page. Colour and logo are taken from
the [mme3303](https://github.com/ctdegroot/mme3303) course slides — swap `theme.scss` and
`img/logo.png` to rebrand.

This folder is intentionally **not** part of the GroupResources website build (see the
`!templates/` exclusion in the root `_quarto.yml`) — it's a standalone starting point you copy out
per presentation, not a knowledge-base page.

## Using it

Copy this folder out to wherever you keep the talk (a new repo, a folder in your notes, etc.) and
rename `template.qmd` to something meaningful:

```bash
cp -r templates/presentation ~/talks/my-conference-talk
cd ~/talks/my-conference-talk
mv template.qmd slides.qmd
quarto preview slides.qmd
```

`quarto preview` opens a live-reloading browser view. Edit the YAML header (title, author,
institute) and replace the example slides with your content. The `.notes` div under a slide is
speaker notes — press `s` while presenting to open the notes window.

## Fixed slide size, not a "floating" page

`width`/`height` in the YAML (1280×720) fix the deck's aspect ratio and pixel dimensions. Reveal.js
scales that whole fixed box up or down to fit whatever window or screen it's shown on (it
letterboxes rather than reflowing), so content stays exactly where you put it regardless of
display — this is what was missing when the slides felt like they were "floating" before. `margin`
controls the padding inside that fixed box; `center: false` keeps slide content anchored under the
heading instead of vertically centering (more consistent from slide to slide, closer to how Beamer
lays things out).

## Typography and header convention

Sizing and layout follow the
[Assertion-Evidence](https://www.assertion-evidence.com/) approach used widely in engineering
presentation training (Penn State, IEEE workshops): a full-sentence headline at a consistent
28-36pt-equivalent, body text no smaller than 18-24pt-equivalent, and the headline always in the
same header position rather than reset per slide. Concretely here:

- `$presentation-font-size-root` is 36px (close to reveal.js's own 40px default) — body text is
  1:1 with that, not shrunk, since research-slide guidance treats small body text as the most
  common readability failure.
- Every slide's first heading sits flush at the top-left with a purple rule underneath, in the same
  position regardless of how much content follows — the "header" convention you'd expect from
  Beamer or PowerPoint's Title-and-Content layout. Only the auto-generated title/cover slide
  (`#title-slide`) is exempted, keeping Quarto's own centered cover treatment.
- Prefer a short assertion ("Damping reduces peak displacement by 40%") over a topic label
  ("Results") as the heading where it fits your talk — that's the actual substance of the
  Assertion-Evidence method, the layout above just makes it consistent to use.
- Assertive headlines run longer than topic labels and will wrap to two lines; this is handled —
  the rule sits under the last wrapped line, not a fixed offset, so it doesn't cut through the
  second line or float above it.

## Footer

The centered footer text is the `footer:` key in `template.qmd`'s YAML — change it per talk (a
conference name, a defense committee, a project name). The logo and the `slide-number: true` flag
are separate YAML keys next to it if you want to swap or drop either.

If you touch `theme.scss`'s footer rules, three reveal.js/Quarto behaviours bit us while building
this and are worth knowing about before changing anything there:

- reveal.js's footer plugin toggles the footer/logo/slide-number elements with an inline
  `style="display: block"` for show/hide. A plain `display: flex` in the stylesheet loses to that
  inline style, which silently disables `align-items`/`justify-content` centering — it needs
  `!important`.
- The default theme puts `margin: var(--r-block-margin) 0` on every `.reveal img`, including the
  logo. Left unset, that margin eats into the `bottom` offset and shifts the logo up from where it
  looks like it should sit — the logo rule zeroes it explicitly.
- reveal.js core puts a 5px `padding` on `.slide-number` as a content-box addition, which grows the
  box past the footer's height unless you also set `box-sizing: border-box` (or zero the padding).

## Layout control (the Beamer-replacement part)

- `theme.scss` is the equivalent of a Beamer `.sty` — colours, fonts, footer/logo/slide-number
  positioning all live there under `scss:rules`. It's plain CSS, so anything you could do with a
  Beamer macro you can do here with a selector.
- Two-column layouts: wrap content in `::: {.columns}` / `::: {.column width="50%"}` (built into
  Quarto's revealjs format, no custom CSS needed).
- A dense slide: add `{.smaller}` after a heading to shrink that slide's font size.
- For anything more custom (precise positioning, overlays), target `.reveal .slides section` (or a
  class you add to a specific slide) in `theme.scss` — same approach as the mme3303 course slides'
  `custom.css`.

## Exporting to PDF

Recommended: [decktape](https://github.com/astefanutti/decktape), a headless-Chrome tool built
specifically for exporting reveal.js decks. It drives reveal.js's own per-slide navigation rather
than relying on the fragile `?print-pdf` CSS layout, and one page per slide with the footer/logo/
slide number repeating correctly on every page is confirmed working with this template:

```bash
npx decktape reveal slides.html slides.pdf
```

You can also use the browser's own Print dialog: open the deck with `?print-pdf` appended to the
URL (e.g. `slides.html?print-pdf`), then Print → Save as PDF with background graphics enabled and
margins set to none. This is the standard reveal.js print path and should also repeat the fixed
footer on every page (per the CSS paging spec), but it wasn't verified here — `Chrome
--headless --print-to-pdf` (a *different*, non-interactive path than the print dialog) produced a
single near-blank page in testing, because reveal.js's print-layout JavaScript never got a chance
to run before the snapshot was taken. If you hit the same thing with some other automated tool,
decktape is the reliable option; if you need to suppress the footer for a particular export
instead, the fallback the mme3303 course template uses is to hide it in print entirely:

```scss
.print-pdf .footer,
.print-pdf .slide-logo,
.print-pdf .slide-number {
  display: none !important;
}
```

## What's deliberately left out

This is the minimal version: no chalkboard annotation, no instructor/student role toggling. Both
are straightforward to add back by copying the relevant plugin/CSS from
[mme3303](https://github.com/ctdegroot/mme3303) if a future deck needs them.
