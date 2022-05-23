# Dathomir

Python project to clone all `gitlab` or `github` repositories using gitlab api

**_Version: 1.0.0_**

## Summary

- [Requirements](#requirements)
- [Get started](#get-started)
- [How it works](#how-it-works)
- [VS Code](#vs-code)
- [Formatting](#formatting)
- [Contact](#formatting)
- [Credits](#credits)

## Requirements

- [Python](https://www.python.org/) >= 3.9.5

packages to install with pip

```bash
python3 -m pip install --user pip install virtualenv
python3 -m pip install --user pip install pep8
```

## Get started

If you don't have python

```bash
$ [sudo] apt-get install python3
$ pip install virtualenv
```

```bash
$ git clone git@github.com:LucasNoga/dathomir.git
$ cd horus
$ virtualenv -p 3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cp config.example.json config.json
$ python3 main.py
```

## How it works

The script connect to the self-hosted GitLab instance and request api to get all repository path  
Then clones it into repositories folder

## VS Code

To add in `settings.json`

```js
  "python.linting.pylintArgs": [
    "--disable=W0703", // W0703: Generic Exception
    "--load-plugins",
    "pylint_flask_sqlalchemy",
    "pylint_flask"
  ]
```

## Formatting

The source code is format with the [pep8 guidelines](https://peps.python.org/pep-0008/)  
The source code is validating by [pylint](https://pylint.pycqa.org/en/latest/)

## Contact

- To make a pull request: https://github.com/LucasNoga/dathomir/pulls
- To summon an issue: https://github.com/LucasNoga/dathomir/issues
- For any specific demand by mail: [luc4snoga@gmail.com](mailto:luc4snoga@gmail.com?subject=[GitHub]%20Dathomir%20Project)

## Credits

Made by Lucas Noga.  
Licensed under GPLv3.
