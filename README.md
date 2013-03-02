PUPILS
=======

Application for the management of any event related to educational, sports or
leisure, in which the protagonists are children.

## Prerequisites ##

- python >= 2.7
- pip
- virtualenv/wrapper

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages pupils-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages pupils-env
cd pupils-env
source bin/activate
```

### Clone the code ###
```bash
git clone https://github.com/franlu/pupils.git pupils
```

### Install requirements ###
```bash
cd pupils
pip install -r requirements.txt
```

## Running ##
```bash
python manage.py runserver
```
Open browser to http://127.0.0.1:8000


#### Owner ####

* [Fco Javier Lucena] (https://github.com/franlu)

#### Contributors ####

* [Serafín Vélez] (https://github.com/seravb)
* [Álvaro Hurtado] (https://github.com/alvarohurtado84)
* [Pablo Torres] (https://github.com/unmelon)

