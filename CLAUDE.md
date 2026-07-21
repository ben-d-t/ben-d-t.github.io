# Project Context

This is Ben Thomas's personal website, hosted at www.benthomas.xyz.

## Architecture

- **Static site generator**: Quartz v4 (forked from jackyzha0/quartz)
- **Content source**: `content/` is a **symlink** to the Obsidian vault at `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Garden/content` (the real files live in the vault)

### Why git history contains real files under `content/`

Git cannot track files through a symlink (`git add content/` → `fatal: pathspec 'content/' is beyond a symbolic link`). `npx quartz sync` works around this in `handleSync` (`quartz/cli/handlers.js:519`): it detects the symlink, stashes it, copies the real vault files into `content/`, runs `git add . && git commit`, then puts the symlink back. So the committed tree holds real files while the working copy holds a symlink.

**Failure mode seen on 2026-07-20:** iCloud replaced `content` with a **macOS Alias file**. `lstat().isSymbolicLink()` is false for an Alias, so sync skipped the dereference and committed the alias blob plus the deletion of all 133 notes. If a sync ever deletes the whole content tree, run `file content` — if it says "MacOS Alias file" instead of resolving to a directory, recreate the link with `ln -s` (never by option-cmd-dragging in Finder, which makes an Alias).
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
