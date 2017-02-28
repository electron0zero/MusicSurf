## Getting Started

This guide will help you setup development environment

## Get required packages

**install Python**
install python3
    *if you are on windows we recommend [Anaconda](https://www.continuum.io/downloads) distribution, it will make your life easy*

**install required dependencies**

Run `pip install -r requirements.txt`

If you are on windows then you will see that some packages *like `lxml`* failed to install.

Go to [this website](http://www.lfd.uci.edu/~gohlke/pythonlibs/) and get wheel of that package for your python and OS Arch. type.

*for example `lxml` package for 64bit OS with python 3.5.2 will be `lxml‑x.x.x‑cp35‑cp35m‑win_amd64.whl`*

Find wheel for your setup and install it by running `pip install /path/to/wheelfile.whl`

## Style Guide

Once you are done with all the installation let's talk about code style and setting up text editor

we use [editorconfig](http://editorconfig.org/) to maintain indentation consistency.

so go ahead and find an editorconfig plugin for your text editor

*if you don't have a text editor of choice we recommend you to use [Atom](https://atom.io/) or [VSCode](https://code.visualstudio.com/), if you prefer to use an IDE then [pycharm](https://www.jetbrains.com/pycharm/) is quite nice*

we try to stick with PEP-8 as much as possible so please install [pylint](https://www.pylint.org/) to show you style related warnings.

## Code

Now you are all ready to start then let's talk about Code and how it's laid out.

see `/docs` folder for documentation

#### Folder Structure

- .github : Pull request and issue templates [see more](https://github.com/blog/2111-issue-and-pull-request-templates)
- docs : documentation
-
-
- tests : automated tests (unit/integration tests)


## Need Help

Create an issue
