# Cheap Goods
Cheap Goods is a p2p platform that enables local products at an affordable rate

## Installation
- make sure git and python3 is installed on your local machine, if it ain't installed then do this;

```bash
# installs git on an ubuntu machine
$ sudo apt-get install git -y

# installs python3 on an ubuntu machine
$ sudo apt-get install python3 -y
```

- git clone this repository to your local machine

```bash
$ git clone https://sammykingx/cheapGoods
```

- Install the necessary dependencies
```
$ pip install -r requirements.txt
```

- run the application entry point
```bash
$ python3 main.py
```
_by development the application is designed to run on localhost:5000, to change the port just go to the main.py and change the port argument value_

_Also don't forget to turn off debug mode when running this on your live server/production environment_

- go to your web browser to load the applicaton

## Web Infrastructure
![](./images/infrastructure_design.PNG)
- nginx web server
- flask web framework
- gunicorn wsgi server

## db Schema
![](./images/complete_er_diagram.PNG)

## application file structure

```bash
.
├── app_package
│   ├── __init__.py
│   ├── routes
│   │   ├── index.py
│   ├── static
|   |   ├── styles
|   |   ├── scripts
│   └── templates
├── main.py
```

## Contributors

- Iyebhora Samuel (sammykingx)
- [Tebiremen Okojie](https://github.com/Tebiremen)
- Big N

## [Licensing](./LICENSE)
