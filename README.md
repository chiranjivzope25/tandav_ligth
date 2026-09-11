# Tandav Lights • Bhusawal — Vercel + FastAPI

## Structure

```text
Tandav_Lights_Bhusawal_Vercel/
├── index.html
├── requirements.txt
└── api/
    └── index.py
```

## Run locally

```bash
pip install -r requirements.txt
npm install -g vercel
vercel dev
```

Open:

`http://localhost:3000`

API health:

`http://localhost:3000/api/health`

FastAPI docs:

`http://localhost:3000/api/docs`

## Deploy

From this folder:

```bash
vercel
```

Then production:

```bash
vercel --prod
```

Vercel's current FastAPI support can detect FastAPI applications automatically, and `api/index.py` is a supported Python function entrypoint.

## Booking flow

The booking form sends the details to:

`POST /api/bookings`

After successful validation, the frontend opens the existing Tandav Lights WhatsApp booking message.

## Important storage note

This API does NOT store bookings in a local SQLite/JSON file.

Vercel Functions are serverless, so local filesystem data should not be treated as permanent booking storage. For a real booking/admin system, connect the endpoint to a persistent database such as Vercel Postgres/Neon/Supabase or another hosted database.

## Security note

Do not create a public unauthenticated endpoint that returns all customer bookings. Add authentication before building an admin dashboard.
