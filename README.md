# Tribes social

## About 
Its a social media In the early stages, not really for the public but Ill keep it open

## Philosophy

Tribes social is meant to imatate the social circle of a tribe where ever possible. Some features may include 

- Assinged avatars
- Votes for cetrain features/rights within the tribe
- Elected banishments
- Elected leader
- Custom css made from each meber to make your tribe your own

## Things I have that you might need

### Python 3.10
```
Django==4.1.4
channels==4.0.0
daphne==4.0.0
channels-redis==4.0.0
python-dotenv
bleach
psycopg2
```

### Not Python
```
docker (to run channels)
postgres (for database)
```

## Start up

```
systemctl start docker
docker run -p 6379:6379 -d redis:5
python3 manage.py runserver
```

That is all
