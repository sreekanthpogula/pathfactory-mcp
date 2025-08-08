from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.auth import router as auth_router

from routers import (
    content_library, recommendations, conversations,
    topics, engagement, collection
)

app = FastAPI(title="PathFactory MCP Server", version="1.0.0")


# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth route
app.include_router(auth_router)

# Modular routes
app.include_router(content_library.router)
app.include_router(recommendations.router)
app.include_router(conversations.router)
app.include_router(topics.router)
app.include_router(engagement.router)
app.include_router(collection.router)

@app.get("/")
async def root():
    return {"message": "PF MCP Tools API is running"}
