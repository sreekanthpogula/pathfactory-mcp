from fastapi import APIRouter, Depends
from auth.auth import get_current_user

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/", summary="Get recommendations")
async def get_recommendations(user: str = Depends(get_current_user)):
    return {
        "user": user,
        "data": [
            {"id": 1, "title": "Mock Video recommendation 1"},
            {"id": 2, "title": "Mock Ebook recommendation 2"},
            {"id": 3, "title": "Mock Article recommendation 3"},
            {"id": 4, "title": "Mock Podcast recommendation 4"},
            {"id": 5, "title": "Mock Webinar recommendation 5"},
            {"id": 6, "title": "Mock Course recommendation 6"},
            {"id": 7, "title": "Mock Infographic recommendation 7"},
            {"id": 8, "title": "Mock Case Study recommendation 8"},
            {"id": 9, "title": "Mock Whitepaper recommendation 9"},
            {"id": 10, "title": "Mock Report recommendation 10"},
            {"id": 11, "title": "Mock Guide recommendation 11"},
            {"id": 12, "title": "Mock Checklist recommendation 12"},
            {"id": 13, "title": "Mock Template recommendation 13"},
            {"id": 14, "title": "Mock Tool recommendation 14"},
            {"id": 15, "title": "Mock Resource recommendation 15"},

        ]
    }
