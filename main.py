from fastapi import FastAPI
from auth.auth import router as auth_router

from routers import (
    content_library, recommendations, conversations,
    topics, engagement, collection
)

app = FastAPI(title="PathFactory MCP Server")

# Auth route
app.include_router(auth_router)

# Modular routes
app.include_router(content_library.router)
app.include_router(recommendations.router)
app.include_router(conversations.router)
app.include_router(topics.router)
app.include_router(engagement.router)
app.include_router(collection.router)
