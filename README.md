# Software Engineering Pipeline

Small project to learn agile workflows with GitHub Actions.

## Project overview

This repository is a small Python project used to practice a professional software engineering workflow with Git, GitHub, Pull Requests and GitHub Actions.

The project contains a simple calculator module and automated tests. Each new change should be developed in a separate branch and integrated into `main` through a Pull Request.

## Development workflow

The project follows a simple Agile/GitHub workflow:

1. Create or select a feature branch.
2. Implement a small change.
3. Commit the change locally.
4. Push the branch to GitHub.
5. Open a Pull Request into `main`.
6. Wait for the CI pipeline to run.
7. Review the changes and merge only if the checks pass.

This workflow allows several developers to work in parallel without pushing directly to `main`.

## Running checks locally

Before pushing changes, install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the automated tests:

```bash
pytest --tb=short
```

Run the linter:

```bash
flake8 . --max-line-length=88
```

## CI pipeline

The GitHub Actions workflow runs automatically on every push or Pull Request.

The pipeline has two main jobs:

1. `lint`: checks code style using `flake8`.
2. `test`: runs the automated tests using `pytest`.

The `test` job depends on the `lint` job. This means that if the code style check fails, the tests are not executed. This acts as a quality gate before merging changes into `main`.

## Branch naming convention

Branches should use descriptive names that explain the purpose of the work.

Good examples:

```text
feature/multiply
feature/ci-readme-instructions
bugfix/fix-tests
```

Less clear examples:

```text
test
changes
```

Descriptive branch names make collaboration easier because the team can understand the purpose of each branch before opening it.
