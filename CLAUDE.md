# Project Context

This is Ben Thomas's personal website, hosted at www.benthomas.xyz.

## Architecture

- **Static site generator**: Quartz v4 (forked from jackyzha0/quartz)
- **Content source**: The `content/` folder is a symlink to an Obsidian vault at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Garden/content`
- **Hosting**: GitHub Pages via GitHub Actions

## Git Setup

- **origin**: git@github.com:ben-d-t/ben-d-t.github.io.git (the published site)
- **upstream**: https://github.com/jackyzha0/quartz.git (for pulling Quartz updates)
- **Main branch**: v4

## Deployment

Run `npx quartz sync` to commit changes and push to GitHub. This triggers `.github/workflows/deploy.yml`, which:
1. Runs `npx quartz build`
2. Deploys the `public/` folder to GitHub Pages

## Key Files

- `quartz.config.ts` - Site configuration
- `quartz.layout.ts` - Layout configuration
- `quartz/` - Quartz source code (required for builds, don't remove)
- `docs/` - Quartz documentation (not needed for this site, but kept for clean upstream merges)
