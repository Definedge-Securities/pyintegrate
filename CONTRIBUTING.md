# Contributing

We highly appreciate feedback and contributions from the community! If you'd like to contribute to this project, please make sure to review and follow the guidelines below.

# TL;DR

## Code of conduct

In the interest of fostering an open and welcoming environment, please review and follow our [code of conduct](./CODE_OF_CONDUCT.md).

## Code and copy reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests) for more
information on using pull requests.

## Report an issue

Report all issues through [GitHub Issues](./issues). Before reporting an issue, please make sure to search through existing issues to see if your issue has already been reported.

## File a feature request

File your feature request through [GitHub Issues](./issues). Before filing a feature request, please make sure to search through existing issues to see if your request has already been filed.

## Create a pull request

When making pull requests to the repository, make sure to follow these guidelines for both bug fixes and new features:

- Before creating a pull request, file a GitHub Issue so that maintainers and the community can discuss the problem and potential solutions before you spend time on an implementation.
- In your PR's description, link to any related issues or pull requests to give reviewers the full context of your change.
- For commit messages, follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) format.
- For example, if you update documentation, your commit message might be: `docs: updated installation documentation`.
- Make sure to add tests for your change. If you're adding a new feature, make sure to add tests for the new feature.
- Run all tests locally before submitting a pull request.
- Before committing, install pre-commit hooks using `make install_hooks` or `poetry run pre-commit install`. This will ensure that your code is formatted and that your commit messages follow the Conventional Commits format.

# Get Started!

Ready to contribute? Here's how to set up `pyintegrate` for local development.

1. Fork the `pyintegrate` repo on GitHub.
2. Clone your fork locally:

    ```bash
    git clone https://github.com/your_github_username/pyintegrate.git
    ```

3. Ensure that you are using Python 3.9 or above: 

    ```bash
    python --version
    ```

4. Install `poetry` for dependency management and packaging: 

    ```bash
    make install_poetry
    ```

    OR

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

5. Install dependencies using `poetry`:

    ```bash
    make install
    ```

    OR

    ```bash
    poetry install
    ```

6. Install pre-commit hooks:
    
    ```bash
    make install_hooks
    ```

    OR

    ```bash
    poetry run pre-commit install
    ```

7. Create a branch for local development:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

8. When you're done making changes, check that your changes pass the tests:

    ```bash
    make test
    ```

    OR

    ```bash
    poetry run pytest -s tests/unit
    ```

9. To run integration tests

    ```bash
    poetry run pytest -s tests/integration --apiToken "api_token" --apiSecret "api_secret" --totp "totp"
    ```

    OR you can store the session keys and use them for subsequent runs as below

    ```bash
    poetry run pytest -s tests/integration --uid "uid" --actid "actid" --apiSessionKey "api_session_key" --wsSessionKey "ws_session_key"
    ```

Note
----
Integration tests require a valid API token and secret as the orders would be placed in the live market. Please use a test account for integration testing else use unit tests.


9. Commit your changes and push your branch to GitHub:

    ```bash
    git add .
    git commit -m "fix: detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

    In brief, commit messages should follow these conventions:

    - For commit messages, follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) format.
    - Always contain a subject line which briefly describes the changes made. For example "Update CONTRIBUTING.md".
    - Subject lines should not exceed 50 characters.
    - The commit body should contain context about the change - how the code worked before, how it works now and why you decided to solve the issue in the way you did.

10. Submit a pull request through GitHub.
