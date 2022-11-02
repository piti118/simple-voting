# Simple Voting API

There are three choices "dog", "cat", "mouse"

# Setup

```
pip install -r requirements.txt
```

```
python voting.py
```

should spin up a web server at

```
http://localhost:8888
```

## Vote via api
http post to
```
/vote
```
with the following json body
```
{"name": "dog"}
```

## View result
```
/result
```
