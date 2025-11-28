# SafeConnect Backend (FastAPI)

This is the backend service for **SafeConnect**, a human-centered safety check-in mobile app (Android + iOS).  
The goal of this backend is to provide a lightweight, clean, and extendable API for:

- User registration  
- Trusted contacts  
- Safety check-ins (“I’m OK” / “Need to Talk”)  
- Configurable notifications (future)  

The project is intentionally simple but structured, making it easy to evolve into a full production backend.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- Simple in-memory storage (for demo purposes)
- Ready for SQL database expansion (e.g., PostgreSQL + SQLAlchemy)

---

## 📁 Project Structure
backend/ 
├── main.py        
# FastAPI app with routes 
├── models.py      
# Pydantic models (User, Contact, CheckIn) 
├── storage.py      
# In-memory storage implementation 
├── requirements.txt 
# Dependencies
└── README.md       
# (this file)
---

## ⚙️ How to Run the Backend

### 1. Clone the repository

```bash
git clone https://github.com/your-user/safeconnect-mobile.git
cd safeconnect-mobile/backend

2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Start the server

uvicorn main:app --reload

5. Open API documentation

FastAPI automatically generates docs at:

🔗 http://127.0.0.1:8000/docs (Swagger UI)
🔗 http://127.0.0.1:8000/redoc (ReDoc)


---

🧱 Core Models

User

id

name

email


Trusted Contact

id

user_id

name

relationship

notify_ok

notify_need_to_talk

is_primary


Check-in

id

user_id

type (“OK” or “NEED_TO_TALK”)

timestamp

selected_contact_ids

notified_contact_ids



---

🛠 API Endpoints

🔹 Health check

GET /health

🔹 Create user

POST /users

Example:

{
  "name": "Caro",
  "email": "caro@example.com"
}

🔹 List users

GET /users

🔹 Create trusted contact

POST /users/{user_id}/contacts

🔹 Get user contacts

GET /users/{user_id}/contacts

🔹 Create safety check-in

POST /users/{user_id}/checkins

Example:

{
  "type": "OK",
  "selected_contact_ids": ["contact1", "contact2"]
}

🔹 List check-ins for a user

GET /users/{user_id}/checkins


---

📌 Notes

Storage is in-memory, so data resets when the server restarts.

This keeps the backend lightweight and perfect for demos, interviews, and front-end integration.

It's structured so migrating to a real database requires minimal refactoring.



---

🔮 Future Roadmap

Replace in-memory storage with PostgreSQL + SQLAlchemy

JWT authentication

Push notifications via Firebase (Android) and APNs (iOS)

Scheduled reminders for missing check-ins

Multi-user family groups

Real analytics + audit logs



---

👨‍💻 Author

Backend developed as part of the SafeConnect mobile project by Sergio Ramírez,
specialized in Android (Kotlin/Compose), iOS (SwiftUI), Python backend, IoT, and cloud-connected systems.

---


