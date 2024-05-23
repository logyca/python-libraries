# References

https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://python-poetry.org/docs/pyproject/

# Select library to upload or update

cd library

# Example: Files descriptions
    .
    |-- logyca/                # Library main folder
    |   |-- logyca/            # Source code
    |   |   |-- __init__.py    # Index of data objets, the attribute __version__ is used by pyproject.toml for upload changes in https://pypi.org, for develop use x.y.#a#
    |   |-- test/              # Unit tests to ensure that the functionality or objects of the library are consistent
    |-- .pypirc                # File needed to upload to https://pypi.org, you can copy the .pypirc-sample file to build it
    |-- .pypirc-sample         # Example data for build file .pypirc
    |-- LICENSE.txt            # License to publish
    |-- pyproject.toml         # Is the specified file format of PEP 518 which contains the build system requirements of Python projects.
    |-- README.md              # Readme to publish

# Before uploading any changes, you must first run the unit tests is it exists

cd Logyca\tests
```console
# Pre-requisite
pip install pytest -y
pip show pytest

# Make test
pytest -s
```

# Define version to publish

Change Attribute: setup.py: VERSION

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.

Example

* Develop (Alpha release): __version__ = "0.1.5a13"
* Number versions are not published by default, they must be installed by manually defining their number
* Production: __version__ = "0.1.5"

# Pre-Requisites to Build + Publish

```python
# Create virtual environment
python -m pip install pipenv
# Activate virtual environment
python -m pipenv shell

# Build tool
pip install --upgrade setuptools build

# Publish to pypi/Azure DevOps Artifacts tool
pip install --upgrade twine

```

# Build + Publish in https://pypi.org

```console
# be located in the library folder
cd folder/
# then run this in the same folder where setup.py is located.    
python -m build
# Upload to PyPI Production
twine upload dist/* --config-file ../.pypirc --verbose --repository pypi
```

For testing
```console
# be located in the library folder
cd folder/
# Upload to PyPI Develop
twine upload dist/* --config-file ../.pypirc --verbose --repository testpypi
```

# Build + Publish in https://dev.azure.com

```console
# be located in the library folder
cd folder/
# then run this in the same folder where setup.py is located.    
python -m build

# Upload to PyPI Production logyca
twine upload -r logyca --config-file .pypirc-azure --verbose dist/*

# Upload to PyPI Production logyca-postgres
twine upload -r logyca-postgres --config-file ../.pypirc-azure --verbose dist/*
```

# Delete Cache

Powershell
```Powershell
Get-ChildItem -Directory -Recurse -Filter "*.egg-info" | Remove-Item -Force -Recurse
Get-ChildItem -Directory -Recurse -Filter "dist" | Remove-Item -Force -Recurse
```

# Install from pypi

```console
pip install logyca==$version
pip show logyca

```

# Install from Azure DevOps Artifact

```console

### logyca
# For only APIResult and Health
pip install logyca==1.8.0 --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca/pypi/simple/
# For fastapi with api-key or oauth dependency injection
pip install fastapi
pip install logyca[oauth_token]==x.x.x --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca/pypi/simple/
pip install logyca[api_key_simple_auth]==x.x.x --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca/pypi/simple/
pip install logyca[oauth_token-api_key_simple_auth]==x.x.x --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca/pypi/simple/
# For update
pip install logyca --upgrade --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca/pypi/simple/
pip show logyca

### logyca_postgres
# No postgres drivers, just package files and check minimum requirements
pip install sqlalchemy
pip install logyca_postgres==0.0.0b7 --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca-postgres/pypi/simple/
pip show asyncpg
pip show psycopg2

# checks postgres drivers, install files and alerts the user to choose and install the necessary versions required
pip install sqlalchemy
pip install logyca_postgres[async]==0.0.0b7 --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca-postgres/pypi/simple/
pip show asyncpg
pip show psycopg2
pip install logyca_postgres[sync]==0.0.0b7 --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca-postgres/pypi/simple/
pip show asyncpg
pip show psycopg2

pip install logyca_postgres --upgrade --index-url https://pkgs.dev.azure.com/grupologyca/shared_code_library/_packaging/logyca-postgres/pypi/simple/
pip show logyca_postgres

```


