# py_lab

## Setup dev environment
* Setup Python dependencies
```
pipenv install
pipenv install --dev
```
* If you don't see: (py_gh_metrics) command prompt:$_____
* Then start this project's virtualenv with:
```
pipenv shell
```
* Or run a single command inside the virtualenv using:
```
pipenv run
```

## Run tests
```
# Run all tests
pytest

# run specific tests
pytest ./path/script.py::test_name -sv
```