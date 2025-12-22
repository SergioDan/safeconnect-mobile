# SafeConnect Backend (FastAPI)

## Run locally

### 1) Create venv (recommended)
python -m venv .venv

### 2) Activate venv
# macOS/Linux:
source .venv/bin/activate

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

### 3) Install dependencies
pip install -r requirements.txt

### 4) Run server (from the backend folder)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

## API Docs
- Swagger: http://localhost:8000/docs
- Health:  http://localhost:8000/health

## Quick test flow (example)

### Create a user
POST /users
{
  "name": "Android User",
  "email": null
}

### Add a contact
POST /users/{user_id}/contacts
{
  "name": "Mom",
  "phone": "+57 3000000000",
  "priority": 1
}

### List contacts
GET /users/{user_id}/contacts

### Send a check-in
POST /users/{user_id}/checkins
{
  "type": "OK",
  "selected_contact_ids": []
}

### List check-ins
GET /users/{user_id}/checkins