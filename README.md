# pytest-ci-demo

[![CI](https://github.com/megunay/pytest-ci-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/megunay/pytest-ci-demo/actions)
[![codecov](https://codecov.io/gh/megunay/pytest-ci-demo/branch/main/graph/badge.svg?token=956da3ab-47c8-4ca2-a167-f604332d5892)](https://codecov.io/gh/megunay/pytest-ci-demo)

## 📌 Project Overview
This repository is a **demo project** that shows how to set up:
- Automated testing with `pytest`
- Coverage tracking with `pytest-cov`
- Continuous integration with **GitHub Actions**
- Coverage reporting with **Codecov**

The tests themselves are intentionally simple (basic math checks) to keep the focus on CI/CD setup rather than application logic.

## 🔍 Example Tests
This demo doesn’t just check math—it also includes API tests against [Reqres](https://reqres.in/) (a free REST API for testing):

- Fetching paginated users
- Fetching a single user by ID
- Creating a user with POST


## 🚀 Tech Stack
- [Python 3.11](https://www.python.org/)
- [pytest](https://docs.pytest.org/en/latest/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Codecov](https://about.codecov.io/)

## 🧪 Running Tests Locally
Clone the repo and install dependencies:

```bash
git clone https://github.com/megunay/pytest-ci-demo.git
cd pytest-ci-demo
pip install -r requirements.txt