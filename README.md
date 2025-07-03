# Gym Management Web App

This repository contains a basic Flask web application for managing a gym. It provides simple API endpoints to manage gym members and classes using in-memory storage.

## Requirements

- Python 3.11+
- Flask 3.x

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

```bash
python3 app.py
```

The application will be available at `http://localhost:5000/`.

### API Endpoints

- `GET /members` - list all members
- `POST /members` - add a member (JSON body with `name`)
- `GET /classes` - list all classes
- `POST /classes` - add a class (JSON body with `title`)
