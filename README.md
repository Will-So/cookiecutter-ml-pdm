

<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/fpgmaas/cookiecutter-pdm/main/docs/static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">

---

[![Release](https://img.shields.io/github/v/release/fpgmaas/cookiecutter-pdm)](https://pypi.org/project/cookiecutter-pdm/)
[![Build status](https://img.shields.io/github/actions/workflow/status/fpgmaas/cookiecutter-pdm/main.yml?branch=main)](https://github.com/fpgmaas/cookiecutter-pdm/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-pdm)](https://pypi.org/project/cookiecutter-pdm/)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://fpgmaas.github.io/cookiecutter-pdm/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-pdm)](https://img.shields.io/github/license/fpgmaas/cookiecutter-pdm)


This ia a template that aims to be able to get started with an ML project without needing to understand `pdm` and all of
the other tools that go into making modern Python projects possible. Features include:

- Unified commands using `inv` for all common tasks. Including entering in Ipython shell `inv shell` to testing with `inv test`
to starting a jupyter lab instanv with `inv jupyter`.
- Automatically strips out output and other metadata from the git history of Jupyter notebooks with `nbstripout`
- [PDM](https://pdm.fming.dev/latest/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [black](https://pypi.org/project/black/), [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), and [deptry](https://github.com/fpgmaas/deptry/)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)

---
<p align="center">
  <a href="https://fpgmaas.github.io/cookiecutter-pdm/">Documentation</a> - <a href="https://github.com/fpgmaas/cookiecutter-pdm-example">Example</a> -
  <a href="https://pypi.org/project/cookiecutter-pdm/">PyPi</a>
</p>

---


## Quickstart

### Installing pdm and invoke
Getting started with this package depends on `pdm` and `invoke`. If you've never
used these packages, the cleanest way to install them is with `pipx`. You will  
then have it available for all future projects on your machine. On MacOS, this can be
done with the following commands:

```shell
brew install pipx
pipx install pdm
pipx install invoke
```

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

``` bash
pip install cookiecutter-pdm
ccpdm
```

Alternatively, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

``` bash
pip install cookiecutter
cookiecutter https://github.com/fpgmaas/cookiecutter-pdm.git
```

Create a repository on GitHub, and then run the following commands, replacing `<project-name>`, with the name that you gave the Github repository and
`<github_author_handle>` with your Github username.

``` bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

 ```bash
 make install
 ```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-pdm/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-pdm/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-pdm/features/codecov/).

## Other Types of tasks you may want to define
### 1. `invoke serve`

e.g., if you want to use streamlit. You can have a task that runs something like this:

```streamlit run streamlit_app.py```

### 2. Invoke cibuild
To setup the environment to run tests. 

### 3. setup
If you need to e.g., add entries to your database to get started, you can add a setup command. 


## Acknowledgements

This project was forked from Florian Maas' [Cookiecutter package](https://github.com/fpgmaas/cookiecutter-pdm/tree/main), which in turn is partially based on [Audrey
Feldroy\'s](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.
