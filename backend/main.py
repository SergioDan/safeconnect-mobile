from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import UserCreate, User, ContactCreate, Contact, CheckInCreate, CheckIn
from .storage import storage

app = FastAPI(
    title="SafeConnect Backend API",
    description="Simple backend for SafeConnect check-in app (demo).",
    version="0.1.0",
)

# CORS para permitir que apps móviles consuman la API fácilmente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# Users


@app.post("/users", response_model=User)
def create_user(payload: UserCreate) -> User:
    user = storage.create_user(payload)
    return user


@app.get("/users", response_model=list[User])
def list_users() -> list[User]:
    return storage.list_users()


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str) -> User:
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Contacts


@app.post("/users/{user_id}/contacts", response_model=Contact)
def create_contact(user_id: str, payload: ContactCreate) -> Contact:
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return storage.create_contact(user_id, payload)


@app.get("/users/{user_id}/contacts", response_model=list[Contact])
def list_contacts(user_id: str) -> list[Contact]:
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return storage.list_contacts_for_user(user_id)


# Check-ins


@app.post("/users/{user_id}/checkins", response_model=CheckIn)
def create_checkin(user_id: str, payload: CheckInCreate) -> CheckIn:
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    checkin = storage.create_checkin(user_id, payload)

    # Aquí en el futuro:
    # - Buscar contactos configurados
    # - Enviar notificaciones push a cada uno
    # - Integrar con Firebase/APNs
    return checkin


@app.get("/users/{user_id}/checkins", response_model=list[CheckIn])
def list_checkins(user_id: str) -> list[CheckIn]:
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return storage.list_checkins_for_user(user_id)
