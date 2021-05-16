# Dhurabini Backend
**D**hurabini **hu**dhibiti **ra**slimali **bi**ashara**ni**  
  
![license](https://img.shields.io/badge/license-AGPL%203.0%20or%20later-blue)
![org](https://img.shields.io/badge/org-c3n7-blueviolet)
[![codecov](https://codecov.io/gh/c3n7/dhurabini-backend/branch/main/graph/badge.svg?token=T2V1V4CVKU)](https://codecov.io/gh/c3n7/dhurabini-backend)
[![Python package](https://github.com/c3n7/dhurabini-backend/actions/workflows/main.yml/badge.svg)](https://github.com/c3n7/dhurabini-backend/actions/workflows/main.yml)

## Setting up a development enviroment
### (n)vim + coc.nvim
_You can use **nvim** or **vim**, as long as you have `coc.nvim` installed._  
Assuming you've set-up and activated a virtual environment, install `dev-requirements.txt`
```shell
pip install -r dev-requirements.txt
```
To deal with pylint's issues like `model has no objects property`, add a local config file:
  - In **(n)vim**'s command mode:  
  ```shell
  :CocLocalConfig
  ```
  - The above command will create a `.vim/coc-settings.json` file. Add this to it:
  ```json
  {
    "python.linting.pylintArgs": [
      "--load-plugins=pylint_django",
      "--load-plugins=pylint_django.checkers.migrations",
      "--disable=django-not-configured",
      "--django-settings-module=backend.settings",

      "--disable=C0114, C0115, C0116"
    ]
  }
  ```

### VS Code/Codium
Assuming you've set-up and activated a virtual enviroment, install development requirements:
```shell
pip install autopep8 pylint pylint-django
```
To deal with pylint's django-related issues like the aforementioned `model has no objects property`, add a workspace configuration file in `.vscode/settings.json` with the following contents:
```json
{
    "python.pythonPath": "venv/bin/python",
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--load-plugins=pylint_django.checkers.migrations",
        "--disable=django-not-configured",
        "--django-settings-module=backend.settings",
        "--disable=C0114, C0115, C0116"
    ]
}
```
where `venv/` is the folder containing your virtual environment.


## Setting up CI/DevOps workflows
### Codecov
- Add the repository to [codecov](https://codecov.io) to get a _CODECOV_TOKEN_.
- In your project's GitHub repository `settings` > `secrets`, click `New repository secret` and add the _CODECOV_TOKEN_.

