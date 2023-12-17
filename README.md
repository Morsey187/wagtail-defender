# Wagtail defender

django-defender configured for Wagtail

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/wagtail-defender.svg)](https://badge.fury.io/py/wagtail-defender)
[![defender CI](https://github.com/Morsey187/wagtail-defender/actions/workflows/test.yml/badge.svg)](https://github.com/Morsey187/wagtail-defender/actions/workflows/test.yml)

## Links

- [Documentation](https://github.com/Morsey187/wagtail-defender/blob/main/README.md)
- [Changelog](https://github.com/Morsey187/wagtail-defender/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/Morsey187/wagtail-defender/blob/main/CONTRIBUTING.md)
- [Discussions](https://github.com/Morsey187/wagtail-defender/discussions)
- [Security](https://github.com/Morsey187/wagtail-defender/security)

## Supported versions

- Python ...
- Django ...
- Wagtail ...

## Installation

First install using pip (TODO publish package)

- `pip install wagtail-defender`

Then add django-defender and wagtail-defender to your project's INSTALLED_APPS:

```Python
INSTALLED_APPS = [
    "defender",
    "wagtail_defender",
    # ...
]
```

Configure [django-defender](https://django-defender.readthedocs.io/en/latest/#customizing-django-defender) in your settings file, example:

```python
DEFENDER_LOGIN_FAILURE_LIMIT = 3
DEFENDER_COOLOFF_TIME = 300  # seconds
DEFENDER_LOCKOUT_TEMPLATE = "wagtail_defender/lockout.html" # optional
```

Finally run migrations:

```sh
python manage.py migrate
```

## Customizing wagtail-defender

This package is designed to make managing django-defender possible via the Wagtail admin along with styling features from django defender such as lockout templates to better compliment Wagtail, apart from setting permissions for the addtional admin views provided, wagtail-defender is otherwise not customisable, and instead adapts to how [django-defender](https://github.com/jazzband/django-defender#customizing-django-defender) is configured.

### Permissions

TODO, by default, views are restricted to superusers only.

## Contributing

### Setup

To make changes to this project, first clone this repository:

```sh
git clone https://github.com/Morsey187/wagtail-defender.git
cd wagtail-defender
```

### Redis

This package requires using redis as Django's cache backend. Before contributing make sure to install and run redis locally using the `redis.config`` file in the root directory.

On mac you can run:
```sh
brew install redis
```
And then:
```sh
redis-server ./redis.conf
```

### Install

With your preferred virtualenv activated, install testing dependencies:

#### Using pip

```sh
python -m pip install --upgrade pip>=21.3
python -m pip install -e '.[testing]' -U
```

#### Using flit

```sh
python -m pip install flit
flit install
```

### pre-commit

Note that this project uses [pre-commit](https://github.com/pre-commit/pre-commit).
It is included in the project testing requirements. To set up locally:

```shell
# go to the project directory
$ cd wagtail-defender
# initialize pre-commit
$ pre-commit install

# Optional, run all checks once for this, then the checks will run only on the changed files
$ git ls-files --others --cached --exclude-standard | xargs pre-commit run --files
```

### How to run tests

Now you can run tests as shown below, however, ensure your Redis server is running (`redis-server ./redis.conf`) before running any tests:

```sh
tox
```

or, you can run them for a specific environment `tox -e python3.11-django4.2-wagtail5.1` or specific test
`tox -e python3.11-django4.2-wagtail5.1-sqlite wagtail-defender.tests.test_file.TestClass.test_method`

To run the test app interactively, use `tox -e interactive`, visit `http://127.0.0.1:8020/admin/` and log in with `admin`/`changeme`.

## TODO

- [ ] Docs on setting and configuring admin permissions
- [ ] Remove "add" and "edit" views from AccessAttempt ModelViewset
- [ ] Filterset on AccessAttempt ModelViewset to support filtering fields
    - [ ] Should default to failed login attempts only
- [ ] Dashboard view to easily view and ban sus login attempts from IP addresses 
- [ ] Utils to support sending notifications for:
    - [ ] High volumes of failed login attempts
    - [ ] When a user is locked out
- [ ] Support setting `DEFENDER_STORE_ACCESS_ATTEMPTS` to true or false
- [ ] bulk action support for redis items
- [ ] Add setting for warning message to inform user they could be locked out after N attempts.
- [ ] Add whitelist and blacklist support to django-defender
    - [ ] Option to save cache related to LOCKOUTs to database as well as review for blacklist and spotting malicious IP addresses.
- [ ] Allow managing support in Admin
- [ ] Unit tests and load testing
- [ ] Look into support for logging and notifiying users of unusual successful sigin attempts (device, location)

## Notes

IP addresses can sometimes be hidden behind a proxy such as cloudflare depending on your hosting infrastructure which can cause issues with tracking and blocking IP addresses. One way to resolve this is via middleware https://gist.github.com/Morsey187/562817f4d631ae453e186a3a2f5fe604.
