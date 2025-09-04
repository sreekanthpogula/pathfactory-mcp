from fastapi import APIRouter, Depends, Query
from typing import Optional
from auth.auth import get_current_user
from utils.filtering import apply_filters_and_pagination

router = APIRouter(prefix="/topics", tags=["Topics"])

MOCK_TOPICS = [
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


@router.get("/", summary="Get topics with search, filtering, pagination")
async def get_topics(
    user: str = Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search keyword"),
    category: Optional[str] = Query(None, description="Filter by category"),
    owner: Optional[str] = Query(None, description="Filter by owner"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
):
    filters = {"category": category, "owner": owner}
    result = apply_filters_and_pagination(MOCK_TOPICS, q, filters, page, limit)
    return {"user": user, **result}
