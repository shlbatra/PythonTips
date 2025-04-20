# uv

## Built using Rust

## Command for uv auto completion on shell
eval "$(uv generate-shell-completion zsh)"

# Set up new project
uv init <projectname> --app
uv init <projectname> --lib
uv init <projectname> --package

# create virtual env and set up project
uv run hello.py
# add package depedencies
uv add pandas
uv remove sqlalchemy

# sync virtual env with current depedencies in pyproject.toml
uv sync
# manually create lock file
uv lock
# Upgrade package manually
uv lock --upgrade package pandas
# tree of depedencies
uv tree

uv init another_project
uv init yet-another-project --no-workspace

uv tool run ruff
uv tool run ruff check / uvx ruff check
uv tool dir
uv tool update-shell

uv tool install ruff / uv tool uninstall ruff / uv tool upgrade ruff

uv python list
uv python install 3.10.0 
uv python install '>=3.9,<=3.11'
uv venv 3.10.0

uv publish --password