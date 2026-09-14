# Contributing to GroupResources

Thanks for helping build the group's knowledge base. Every page is written in Quarto Markdown
(`.qmd`), and all changes go through a pull request that is reviewed before it goes live.

## What can and cannot be published

**Everything in this repository is public**, both the source on GitHub and the rendered website.
Before contributing, make sure your content contains **none** of the following:

- Unpublished research results, data or figures
- Personal information about students, staff or anyone else
- Anything confidential, under an NDA, or covered by an industry or collaboration agreement
- Anything export-controlled
- Internal-only lab information (for example, access details, credentials or private contacts)

If you are unsure, leave it out and ask during review. Remember that git history is public too:
removing something in a later commit does not unpublish it.

This is not a course site, so there is no enrollment-gated or graded content.

## Local setup

1. **Install Quarto** from <https://quarto.org/docs/get-started/>.
2. **Install Python dependencies** (needed for pages with executable code):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Preview the site** with live reload while you edit:

   ```bash
   quarto preview
   ```

   To do a full build into `_site/`, run `quarto render`.

## Where a new page goes

| Topic | Folder |
|---|---|
| CFD and numerical methods explainers | `theory/` |
| How-tos for software the group uses | `software/` |
| General, public lab operating information | `policies/` |

Use a short, lowercase, hyphenated file name, for example `software/openfoam-first-case.qmd`.
New pages appear automatically in the section's sidebar and index listing, so you don't need to edit
`_quarto.yml` or the section `index.qmd`. If a topic doesn't fit any section, propose a new section in
your pull request.

## Writing a page

### Frontmatter

Every page starts with YAML frontmatter. `title` and `categories` are required, and the first
category must match the section. A `description` is strongly encouraged, since it appears in the
section listing.

```yaml
---
title: "Making Good Plots with Matplotlib"
description: "Producing clear, publication-quality figures with matplotlib."
categories: [Software, matplotlib, Python]
---
```

Section categories are `Theory`, `Software` and `Policies`. Add further categories as topic tags.

### Images

Put images in a folder next to the page, named after the page, and reference them with relative
paths so the page stays self-contained and easy to move:

```
software/
  paraview-plot-types.qmd
  paraview-plot-types-images/
    streamlines.png
```

```markdown
![Streamlines around a cylinder.](paraview-plot-types-images/streamlines.png){#fig-streamlines}
```

### Math

Write LaTeX math between `$...$` (inline) or `$$...$$` (display). It is rendered with KaTeX.

### Cross-references

Use Quarto's cross-reference syntax rather than manual links or hard-coded numbers. Label figures,
sections and equations, then refer to them with `@`:

```markdown
## Least squares {#sec-least-squares}

$$
\nabla \phi_P \approx \frac{1}{V_P} \sum_f \phi_f \mathbf{S}_f
$$ {#eq-green-gauss}

As shown in @eq-green-gauss and discussed in @sec-least-squares ...
```

Labels must start with `fig-`, `sec-`, `eq-` or `tbl-`. In a Quarto *website*, `@` references
resolve within the same page. To point to another page, use a relative link, optionally to a
labelled section: `[least squares](../theory/gradient-reconstruction.qmd#sec-least-squares)`.

### Executable code

Code cells run when the page is rendered, so examples always show their real output. See
`software/matplotlib-good-plots.qmd` for an example. Add `jupyter: python3` to the frontmatter and
use Quarto cell options:

````markdown
```{python}
#| label: fig-decay
#| fig-cap: "Exponential decay."
import matplotlib.pyplot as plt
...
```
````

The site uses `freeze: auto`: executed output is stored in `_freeze/` and only re-computed when the
page's source changes. **After editing a page with code, run `quarto render` on that page and commit
the updated `_freeze/` files** along with your `.qmd`. If your code needs a new Python package, add it
to `requirements.txt`. Keep examples quick to run, and never load private data.

## Submitting changes

1. Create a branch (group members) or fork the repository (others).
2. Add or edit `.qmd` pages, and preview locally with `quarto preview`.
3. Open a pull request against `main` and complete the checklist in the template.
4. A GitHub Actions check renders the site to make sure it builds.
5. **At least one reviewer must approve before merge.** The reviewer checks that the content is
   accurate, clearly written and, above all, safe to publish.
6. Once merged, the site rebuilds and deploys automatically within a few minutes.

## Licensing

By contributing, you agree that written content is licensed under
[CC BY 4.0](LICENSE-CONTENT.md) and code under the [MIT License](LICENSE).
