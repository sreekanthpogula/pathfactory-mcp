from fastapi import APIRouter, Depends
from auth.auth import get_current_user

router = APIRouter(prefix="/content_library", tags=["Content Library"])

@router.get("/", summary="Get content library")
async def get_content_library(user: str = Depends(get_current_user)):
    return {
        "user": user,
        "data": [
            {"id": 1, "title": "Mock Video 1"},
            {"id": 2, "title": "Mock Ebook 2"},
            {"id": 3, "title": "Mock Article 3"},
            {"id": 4, "title": "Mock Podcast 4"},
            {"id": 5, "title": "Mock Webinar 5"},
            {"id": 6, "title": "Mock Course 6"},
            {"id": 7, "title": "Mock Infographic 7"},
            {"id": 8, "title": "Mock Case Study 8"},
            {"id": 9, "title": "Mock Whitepaper 9"},
            {"id": 10, "title": "Mock Report 10"},
            {"id": 11, "title": "Mock Guide 11"},
            {"id": 12, "title": "Mock Checklist 12"},
            {"id": 13, "title": "Mock Template 13"},
            {"id": 14, "title": "Mock Tool 14"},
            {"id": 15, "title": "Mock Resource 15"},
        ]
    }
