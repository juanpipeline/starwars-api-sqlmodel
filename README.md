# STAR WARS API

```bash
   _____ _                                    
  / ____| |                                   
 | (___ | |_ __ _ _ ____      ____ _ _ __ ___ 
  \___ \| __/ _` | '__\ \ /\ / / _` | '__/ __|
  ____) | || (_| | |   \ V  V / (_| | |  \__ \
 |_____/ \__\__,_|_|    \_/\_/ \__,_|_|  |___/
                                              
           _____ _____ 
     /\   |  __ \_   _|
    /  \  | |__) || |  
   / /\ \ |  ___/ | |  
  / ____ \| |    _| |_ 
 /_/    \_\_|   |_____|
                             
```

This repo is an API Restful to create a Starwars character. Here I use SQLModel as ORM
and FAST API as web service framework. Also I present a proper file structure, and a new
way to code the search endpoints

## Install the requrements

```bash
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
```

## Run migrations

```bash
python -m alembic upgrade head
```

## run the application

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 80 
```

## Utils -  Alembic commands

```bash
python -m alembic revision --autogenerate -m "first model"
python -m alembic upgrade head
```

## References

* [SQLModels](https://sqlmodel.tiangolo.com)
* [FastAPI](https://fastapi.tiangolo.com)
* [Tiangolo Full Stack example](https://github.com/tiangolo/full-stack-fastapi-postgresql)
* [enerBit pygination](https://pypi.org/project/pygination/)
