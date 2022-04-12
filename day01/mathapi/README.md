# Web Application with Python and Flask

## Version 3

- HTTP Methods
- Proxy Objects mention (Lazy, Dependencies, ...)
- Parameters

## Installation

```shell
pip install -r requirements.txt
```

## Run

Windows PS (with **flask**):
```shell
$env:FLASK_APP = "app.main:app"
flask run
```

Windows PS (with **waitress**):
```shell
waitress-serve --host=localhost --port=5000 --url-scheme=https app.main:app
```

Windows PS (with **waitress**, bat file):
```shell
.\run.ps1
```
