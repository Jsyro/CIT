## How to contribute
Government employees, public and members of the private sector are encouraged to contribute to the repository by **forking and submitting a pull request**.

(If you are new to GitHub, you might start with a [basic tutorial](https://help.github.com/articles/set-up-git) and  check out a more detailed guide to [pull requests](https://help.github.com/articles/using-pull-requests/).)

Pull requests will be evaluated by the repository guardians on a schedule and if deemed beneficial will be committed to the master.

All contributors retain the original copyright to their stuff, but by contributing to this project, you grant a world-wide, royalty-free, perpetual, irrevocable, non-exclusive, transferable license to all users **under the terms of the license under which this project is distributed.**

## Git Workflow

### Creating a Pull Request

- Branch new features off the `develop` branch.
- Naming convention based off the problem at hand.  (i.e. update-export-for-fault-tolerance )
- Before pushing your new feature up to Github, make sure to pull in the latest develop, and fix any merge conflicts that might happen.
`git pull origin develop`
- Push your branch up to github.
`git push origin <branchname>`
- open a pull request against develop and request a team member review it.
- once reviewed and approved, merge the request

### Merging your code into develop.

- GitHub will not let you merge code that has not passed the following checks
  - The pipeline builds correctly

  - Another developer has performed code review and you have implemented requested changes

  - Your branch is not behind develop in terms of commits.  If it is, pull the changes into your branch and resolve any merge conflicts.
- Once these conditions are met GitHub will allow you to merge in your code.
- After merge is complete be sure to delete the feature branch so that it doesn't clutter the Github branch list.

### Deploying to test and prod

- Automatic deploy = deployments to test happens when merging to develop, make a PR from feature-branch -> develop.
- Manual deployments to prod will be triggered by the repos admin, after being reviewed and approved.
