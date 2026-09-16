# GroupResources

Public knowledge base for the DeGroot Research Group at Western University: practical software
how-tos, CFD and numerical methods theory notes, and publicly shareable lab policies.

**Live site:** <https://degrootresearchgroup.github.io/GroupResources/>

The site is built with [Quarto](https://quarto.org) and deployed to GitHub Pages by GitHub Actions
on every push to `main`.

## Contributing

Group members contribute pages through pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for
local setup, where new pages go, authoring conventions and the review process. All content must be
safe to publish publicly.

Quick start:

```bash
pip install -r requirements.txt
quarto preview
```

## Repository layout

```
_quarto.yml           Site configuration (navigation, theme, execution)
index.qmd             Home page
theory/               CFD and numerical methods explainers
software/             How-tos for tools the group uses
openfoam/             Using and understanding OpenFOAM
project-management/   How we plan and track research work
policies/             General lab operating information
templates/            Reusable starting points (e.g. the presentation template); not part of the
                      site build directly, but software/presentation-template.qmd links to a zip
                      of it that scripts/build_presentation_template_zip.py rebuilds before every
                      render
scripts/              Build helper scripts (pre-render hooks etc.), not site pages
_freeze/              Cached output of executed code (committed)
```

## License

This repository uses two licenses:

- **Code** (scripts, configuration and code examples) is licensed under the [MIT License](LICENSE).
- **Written content** (the text and figures of the pages) is licensed under
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT.md).
