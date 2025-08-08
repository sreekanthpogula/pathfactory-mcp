from fastapi import APIRouter, Depends
from auth.auth import get_current_user

router = APIRouter(prefix="/collection", tags=["Collection"])

@router.get("/", summary="Get collection")
async def get_collection(user: str = Depends(get_current_user)):
    return {
        "user": user,
        "data": [
            {"id": 1, "title": "Mock Video collection 1"},
            {"id": 2, "title": "Mock Ebook collection 2"},
            {"id": 3, "title": "Mock Article collection 3"},
            {"id": 4, "title": "Mock Podcast collection 4"},
            {"id": 5, "title": "Mock Webinar collection 5"},
            {"id": 6, "title": "Mock Course collection 6"},
            {"id": 7, "title": "Mock Infographic collection 7"},
            {"id": 8, "title": "Mock Case Study collection 8"},
            {"id": 9, "title": "Mock Whitepaper collection 9"},
            {"id": 10, "title": "Mock Report collection 10"},
            {"id": 11, "title": "Mock Guide collection 11"},
            {"id": 12, "title": "Mock Checklist collection 12"},
            {"id": 13, "title": "Mock Template collection 13"},
            {"id": 14, "title": "Mock Tool collection 14"},
            {"id": 15, "title": "Mock Resource collection 15"},
        ]
    }
