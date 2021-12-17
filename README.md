# py_lab

## NB! Set the python path!!!!!
* Many of the modules here are dependent on other modules outside of their module hierarchy
  * Therefore, you will need to...
```
export PYTHONPATH=~/path/to/py_lab
```

## Managing Packages

* Add a new package to the environment
    * Edit Pipfile

```
[packages]
atlassian-python-api = "*"
```

* Update the current pipenv and lock

```
pipenv install # or update
pipenv lock
```

## Setup dev environment

* Setup Python dependencies

```
pipenv install
pipenv install --dev
```

## Enter the dev environment
* If you don't see: (py_lab) command prompt:$_____
* Then start this project's virtualenv with:

```
pipenv shell
```

* Or run a single command inside the virtualenv using:

```
pipenv run
```

## Add module to dev environment
* You don't need to have entered the dev environment
```
pipenv install name_of_module
pipenv install --dev name_of_module
```

## Run tests
* First enter the pip environment
```
# Run all tests
pytest

# run specific tests
pytest ./path/script.py::test_name -sv
```

## Systems

### Atlassian

#### Access with API Token

* Create API Token
    * https://id.atlassian.com/manage-profile/security/api-tokens
* Create file with access info (filename.txt)

```
user
token
jira_url
```

* Input as piped command line args to python script accessing atlassian

```
cat ~/path/filename.txt | xargs python ./atlass/list_of_issues
```