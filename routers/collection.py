from fastapi import APIRouter, Depends, Query
from typing import Optional
from auth.auth import get_current_user
from utils.filtering import apply_filters_and_pagination

router = APIRouter(prefix="/collection", tags=["Collection"])

MOCK_COLLECTIONS = [
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


@router.get("/", summary="Get collection with search, filtering, pagination")
async def get_collection(
    user: str = Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search keyword"),
    category: Optional[str] = Query(None, description="Filter by category"),
    owner: Optional[str] = Query(None, description="Filter by owner"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
):
    filters = {"category": category, "owner": owner}
    result = apply_filters_and_pagination(MOCK_COLLECTIONS, q, filters, page, limit)
    return {"user": user, **result}
