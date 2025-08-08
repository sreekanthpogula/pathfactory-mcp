from fastapi import APIRouter, Depends
from auth.auth import get_current_user

router = APIRouter(prefix="/conversations", tags=["Conversations"])

@router.get("/", summary="Get conversations")
async def get_conversations(user: str = Depends(get_current_user)):
    return {
        "user": user,
        "data": [
            {"id": 1, "title": "Mock Video Conversation 1"},
            {"id": 2, "title": "Mock Ebook Conversation 2"},
            {"id": 3, "title": "Mock Article Conversation 3"},
            {"id": 4, "title": "Mock Podcast Conversation 4"},
            {"id": 5, "title": "Mock Webinar Conversation 5"},
            {"id": 6, "title": "Mock Course Conversation 6"},
            {"id": 7, "title": "Mock Infographic Conversation 7"},
            {"id": 8, "title": "Mock Case Study Conversation 8"},
            {"id": 9, "title": "Mock Whitepaper Conversation 9"},
            {"id": 10, "title": "Mock Report Conversation 10"},
            {"id": 11, "title": "Mock Guide Conversation 11"},
            {"id": 12, "title": "Mock Checklist Conversation 12"},
            {"id": 13, "title": "Mock Template Conversation 13"},
            {"id": 14, "title": "Mock Tool Conversation 14"},
            {"id": 15, "title": "Mock Resource Conversation 15"},
        ]
    }
