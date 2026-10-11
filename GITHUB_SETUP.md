# Publish the standalone repository

This folder is a complete ready-to-push **standalone** project. The current connected GitHub integration can read and update existing repositories, but cannot create a new repository. Do not silently place these files inside Green Knight or Never Coming Soon.

## One-time action

There are two paths. **Easiest for this chat:** create a repository named `dr-marvins-marvelous-machines` under your GitHub account and initialize it with a README, so `main` exists. Share the new repository URL in the chat. The GitHub connection can then update README and create all remaining files in that existing repo.

**Manual terminal alternative:** create an empty repository with no README, license or .gitignore. From a terminal in this project folder, run:

```bash
git init -b main
git add .
git commit -m "Initialize Dr. Marvin brand and invention content OS"
git remote add origin https://github.com/jolthevc/dr-marvins-marvelous-machines.git
git push -u origin main
```

You may also upload the unzipped files with GitHub's web UI, maintaining the directory paths. A ZIP uploaded as one file will **not** automatically become the repo's file tree.

Once created, the existing GitHub connection can maintain and update files using authorized repository write operations.

## Before relying on the system

- Verify the account/repo slug and update `prompts/START_A_CHAT.md` if different.
- Run `python tools/validate.py`; install `jsonschema` for full checks.
- Do one complete selected-packet pilot before building the console.
- Build the small console only when explicitly requested.

No repo, Instagram profile, social images, posts or console are created simply by reading these instructions.
