from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / "index.html"


app = FastAPI(
    title="Tandav Lights Bhusawal API",
    version="1.0.0",
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# WEBSITE HOMEPAGE
# --------------------------------------------------

@app.get("/")
def homepage():
    return FileResponse(INDEX_FILE)


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "Tandav Lights Bhusawal API",
        "time": datetime.now(timezone.utc).isoformat(),
    }


# --------------------------------------------------
# BOOKING MODEL
# --------------------------------------------------

class Booking(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=7, max_length=20)
    event_type: str = Field(min_length=2, max_length=50)
    event_date: str = Field(min_length=4, max_length=20)
    venue: str = Field(min_length=2, max_length=250)
    requirements: str = Field(default="", max_length=2000)


# --------------------------------------------------
# BOOKING API
# --------------------------------------------------

@app.post("/api/bookings")
def create_booking(booking: Booking):
    return {
        "success": True,
        "message": "Booking request received",
        "booking": booking.model_dump(),
    }