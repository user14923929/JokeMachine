
# JokeMachine

A simple Flask API that serves random programming jokes.

## Features

- Returns random jokes with setup and delivery format
- JSON response format
- Unicode support enabled

## Installation

```bash
pip install flask
```

## Usage

Run the application:

```bash
python main.py
```

The API will be available at `http://localhost:5000`

## API Endpoint

### GET `/`

Returns a random joke in JSON format.

**Response:**
```json
[
    {
        "type": "setup",
        "text": "Why do programmers prefer dark mode?"
    },
    {
        "type": "delivery",
        "text": "Because light attracts bugs. 🐞"
    }
]
```

## Requirements

- Python 3.x
- Flask
