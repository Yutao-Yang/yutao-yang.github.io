# Yutao Yang — Academic Homepage

Personal academic homepage published at [yutao-yang.github.io](https://yutao-yang.github.io/). The site uses Jekyll and the Academic Pages theme core, with a custom high-contrast design and Latin Modern Roman typography.

## Repository structure

```text
yutao-yang.github.io/
├── _config.yml              # Website metadata, author profile, links, and Jekyll settings
├── _config_docker.yml       # Local preview override: removes the production URL prefix
├── _data/
│   ├── navigation.yml       # Header navigation
│   └── ui-text.yml          # Theme interface labels
├── _pages/
│   ├── about.md             # Main homepage: all profile and résumé content
│   ├── 404.md               # Not-found page
│   └── sitemap.md           # Human-readable sitemap
├── _includes/               # Theme HTML components; required by Jekyll
├── _layouts/                # Theme page layouts; required by Jekyll
├── _sass/                   # Theme Sass source; required to compile main.css
├── assets/
│   ├── css/main.scss        # Custom visual design and responsive rules
│   ├── js/                  # Navigation behavior
│   ├── fonts/               # Academicons
│   └── webfonts/            # Font Awesome icons
├── images/
│   ├── profile.png          # Formal portrait
│   └── favicon*             # Website icons
├── files/
│   └── Yutao_Yang_CV_EN.pdf  # Public English CV; no Chinese CV is published
├── Gemfile                  # Ruby/Jekyll dependencies
├── package.json             # Optional JavaScript rebuild commands
└── LICENSE                  # Upstream theme license
```

Generated folders such as `_site/` and `.sass-cache/` are ignored by Git and must not be uploaded.

## Routine maintenance

### Update personal information or add an experience

1. Edit the corresponding section in `_pages/about.md`.
2. Keep dates in `Mon. YYYY` format.
3. Add a new News entry when the update is important and time-sensitive.
4. Rebuild locally and inspect the result before committing.

### Update the CV

1. Rebuild the source CV in `D:\A-YutaoYang\cv`.
2. Replace `files/Yutao_Yang_CV_EN.pdf` without changing its filename.
3. Open the English CV download button in the local preview. Do not add the Chinese CV to this public repository.

### Update the portrait

Replace `images/profile.png` with the new image and keep the same filename. A portrait-oriented, high-resolution image with a plain background works best.

### Update navigation

Edit `_data/navigation.yml`. Homepage section links must match an `id` in `_pages/about.md`, for example `/#projects` → `id="projects"`.

### Update visual styling

Custom styles are appended to `assets/css/main.scss` under `Yutao Yang — monochrome academic profile`. Avoid editing compressed output inside `_site/` because it is regenerated on every build.

## Acknowledgements

This website is built upon the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template, which is based on the [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme. The content, typography, layout, and visual styling have been customized for Yutao Yang's personal academic homepage. The upstream license is retained in [`LICENSE`](LICENSE).

## Local build on Windows

Ruby 3.3 and Bundler 2.5 are used in the current workspace.

```powershell
bundle _2.5.23_ install
jekyll build --config _config.yml,_config_docker.yml
python -m http.server 4000 --directory _site
```

Open `http://127.0.0.1:4000/`. The `_config_docker.yml` name is retained from the upstream template, but it is simply a local URL override and does not require Docker.

## Pre-publish checklist

1. Run the local Jekyll build successfully.
2. Inspect desktop and narrow-window layouts.
3. Test the English CV, GitHub, Scholar, ORCID, CSDN, and project links.
4. Run `git diff --check`.
5. Review `git status` so generated folders and private documents are not included.
6. Commit and push to the GitHub Pages repository.

## Privacy rule

This repository is public. Do not add identity documents, household registration records, certificate scans containing personal numbers, private contact records, or unpublished confidential project materials. Those remain in the private root profile repository only.
