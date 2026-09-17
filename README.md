# Jake Dickinson's Professional Portfolio

For details on the base template, please see https://techfolios.github.io.

## Updating the portfolio

Profile, contact details, skills, experience, education, resume projects, and
certificates live in `_data/bio.json`. The home page and web resume share this
data. Certificates accept an optional `url` when a verified credential link is
available. The resume has print styles for the browser's Save as PDF option.

Project pages live in `projects/`; essays live in `essays/`. Keep the original
essay dates when making design changes. Shared templates are in `_includes/`
and `_layouts/`, with the theme in `css/techfolio-theme/default.css`.

## Local checks

```sh
bundle install
bundle exec jekyll build
python scripts/check_site.py
bundle exec jekyll serve
```

The HTML check uses Python's standard library and validates local links, anchor
targets, image alt attributes, unique IDs, and page landmarks. Preview the site
at desktop and mobile widths and check the resume's print preview after layout
changes. External destinations are not covered by the local link check.

Bootstrap's existing stylesheet is vendored in `css/vendor/` so core layout
does not depend on a CDN. Google Fonts is optional; system fonts provide a
fallback. MathJax loads only for pages with `mathjax: true` in front matter.
