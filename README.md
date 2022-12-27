# Tribes social

## About 
Its a social media In the early stages, not really for the public but Ill keep it open


## Things I have that you might need
Django==4.1.4
channels==4.0.0
daphne==4.0.0
channels-redis==4.0.0
docker

## Start up

```
systemctl start docker
docker run -p 6379:6379 -d redis:5
python3 manage.py runserver
```

That is all
