# Promote a OneDrive project folder to Git

Every project starts at `Documents\Projects\<project-slug>` and stays there. Git promotion adds
version history in place; it does not move the folder or change the project source of truth.

1. Review project data classifications, sharing rules, and remote-repository access. Do not publish
   confidential or otherwise restricted project material to an unapproved remote.
2. Confirm the project README and `.gitignore` are present. Check that exports, secrets, local
   credentials, and private material are excluded.
3. Replace `<OneDriveRoot>` below with the actual OneDrive path, then review files and initialize
   Git only with the owner's approval:

```powershell
Set-Location "<OneDriveRoot>\Documents\Projects\<project-slug>"
git status --short
git init
git add README.md .gitignore *.md *.yaml
git status --short
```

4. Review the staged diff before committing. Add nested/source files deliberately; do not use
   blanket staging if the folder contains material that should remain local.
5. Create a remote only after choosing an approved host and repository visibility. Do not push
   automatically.

Git and OneDrive synchronization can both update the same files. Avoid editing the same file
concurrently on multiple devices, wait for OneDrive sync to settle before rebasing or switching
branches, and resolve sync conflicts before continuing.
