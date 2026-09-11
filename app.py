from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


# =========================================================
# PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
INDEX_FILE = BASE_DIR / "index.html"


# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="Tandav Lights Bhusawal API",
    description="Tandav Lights Bhusawal website backend",
    version="1.0.0",
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# BOOKING MODEL
# =========================================================

class Booking(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100
    )

    phone: str = Field(
        min_length=7,
        max_length=20
    )

    event_type: str = Field(
        min_length=2,
        max_length=50
    )

    event_date: str = Field(
        min_length=4,
        max_length=20
    )

    venue: str = Field(
        min_length=2,
        max_length=250
    )

    requirements: str = Field(
        default="",
        max_length=2000
    )


# =========================================================
# WEBSITE
# =========================================================

@app.get("/", include_in_schema=False)
async def homepage():
    """
    Serve the Tandav Lights website.
    """

    if not INDEX_FILE.exists():
        return {
            "error": "index.html not found"
        }

    return FileResponse(
        INDEX_FILE,
        media_type="text/html"
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/api/health")
async def health():

    return {
        "status": "ok",
        "service": "Tandav Lights Bhusawal API",
        "time": datetime.now(timezone.utc).isoformat()
    }


# =========================================================
# BOOKING API
# =========================================================

@app.post("/api/bookings")
async def create_booking(booking: Booking):

    return {
        "success": True,
        "message": "Booking request received",
        "booking": {
            "name": booking.name,
            "phone": booking.phone,
            "event_type": booking.event_type,
            "event_date": booking.event_date,
            "venue": booking.venue,
            "requirements": booking.requirements
        }
    }