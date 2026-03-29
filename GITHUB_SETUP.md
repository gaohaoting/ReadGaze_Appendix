# GitHub setup (after local git init)

If you use the [GitHub CLI](https://cli.github.com/) and are not logged in yet:

```bash
gh auth login
```

On GitHub, create an empty public repository (no README/license from the web UI if you want a single clean history from this folder).

Then:

```bash
cd /Users/gaohaoting/ght/Course/Popov/ReadGaze_Appendix
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

Use SSH instead of HTTPS if that is your preference:

```bash
git remote add origin git@github.com:<your-username>/<repo-name>.git
```

If GitHub rejects the push, ensure you are logged in (`gh auth login` or SSH keys configured).
