from fastapi import FastAPI
from api.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

whitelist = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
] # Whitelisted domains for CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
