## Commit guidelines

##### general guidelines
[How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/)

We think that covers pretty much everything about how and why good commit message matters.
just keep in mind that commit message should be sort and on the point.

##### Commit message should start with any of these words.
- `WIP` - when the commit is for anything that is work in progress. for example.
    1. `WIP - orientation bug`
    2. `WIP - fix crash on windows`

    this means that that commit is not a fix in itself but will be followed up by
    another commits and it is just a part of group of commits that have a meaning.
- `Fix` - when you fix something for example
    1. `Fix- orientation bug` but keep in mind, that commit is final commit for that fix.
    you can use `WIP` for WIP commits,

- `Added` - when something is added. for example
    1. `Added .gitignore`
    2. `Added .editorconfig`

- `Updated` - when you update something. for example
    1. `updated .gitignore`
    2. `updated .editorconfig`

    updated is used when you update any existing stuff.

- `Removed` - when you remove something. for example
    1. `removed outdated config. files`
    
- `Chore` - when you do a routine or repeted task
    1. `Chore - updated build config`
    2. `Chore - bumped version number`

