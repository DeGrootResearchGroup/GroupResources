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
_quarto.yml      Site configuration (navigation, theme, execution)
index.qmd        Home page
theory/          CFD and numerical methods explainers
software/        How-tos for tools the group uses
policies/        General lab operating information
_freeze/         Cached output of executed code (committed)
```

## License

This repository uses two licenses:

- **Code** (scripts, configuration and code examples) is licensed under the [MIT License](LICENSE).
- **Written content** (the text and figures of the pages) is licensed under
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT.md).
