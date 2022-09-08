[![CI on main](https://github.com/hossg/pytest-bdd-cucumbers/actions/workflows/main.yml/badge.svg)](https://github.com/hossg/pytest-bdd-cucumbers/actions/workflows/main.yml)


# pytest-bdd-cucumbers

A simple demonstration of some of the capabilities of pytest-bdd.

## Installation:
1. Ensure poetry is installed on your system
2. From the ./src folder, execute the command 
```
poetry install
```

## Run
The clearest way to run these is to execute the following command to explicitly see the Features and Scenarios that pass and fail:
```
poetry run pytest --gherkin-terminal-reporter -v
```
