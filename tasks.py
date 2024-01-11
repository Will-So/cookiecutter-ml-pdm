from invoke import task
@task
def install(context):
    """Installs the project's dependencies"""
    context.run('pdm install')
    context.run('pdm run pre-commit install')

@task
def add(context, package: str):
    """Adds a new dependency to the project"""
    context.run(f'pdm add {package}')

@task
def update(context):
    """Updates the project's dependencies"""
    context.run('pdm update')

@task
def check(context):
    """Runs specified checks for the project"""
    print("🚀 Checking pdm lock file consistency with 'pyproject.toml': Running pdm lock --check")
    context.run("pdm lock --check")

    print("🚀 Linting code: Running pre-commit")
    context.run("pdm run pre-commit run -a")

@task
def jupyter(context):
    """Runs Jupyter lab with files opened in users $HOME directory"""
    context.run('pdm run jupyter lab --notebook-dir=$HOME')

@task
def ipython(context):
    """Runs ipython shell with the project's dependencies installed."""
    context.run('pdm run ipython')

@task
def loopTest(context):
    """Runs test every time a file is saved and audibly says passed or failed each time. """
    context.run('ptw --onpass "say passed" --onfail "say failed" --ignore notebooks')

@task
def docs(context):
    """Runs docs"""
    context.run('pdm run mkdocs serve')

@task
def testDocs(context):
    """Tests that there are no issues with docs"""
    context.run('pdm run mkdocs build -s')

@task
def clean(context):
    """Deletes dist, .venv, and pdm's cache"""
    context.run('rm -rf dist .venv')
    context.run('pdm cache clear')

@task
def build(context):
    print("🚀 Building package: Running pdm build")
    context.run('pdm build')

@task
def publish(context):
    print("🚀 Publishing package: Running pdm publish")
    context.run('pdm publish')

### ---- THE BELOW ARE ALL ALIASES ---- ###
@task(loopTest)
def lt(context):
    """alias for loopTest command"""
    pass


@task(ipython)
def shell(context):
    """alias for ipython command"""
    pass


