from fastapi import APIRouter, Depends, Query
from typing import Optional
from auth.auth import get_current_user
from utils.filtering import apply_filters_and_pagination

router = APIRouter(prefix="/content_library", tags=["Content Library"])

MOCK_CONTENT = [
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
    {"id": 16, "title": "Mock Video 16"},
    {"id": 17, "title": "Mock Ebook 17"},
    {"id": 18, "title": "Mock Article 18"},
    {"id": 19, "title": "Mock Podcast 19"},
    {"id": 20, "title": "Mock Webinar 20"},
    {"id": 21, "title": "Mock Course 21"},
    {"id": 22, "title": "Mock Infographic 22"},
    {"id": 23, "title": "Mock Case Study 23"},
    {"id": 24, "title": "Mock Whitepaper 24"},
    {"id": 25, "title": "Mock Report 25"},
    {"id": 26, "title": "Mock Guide 26"},
    {"id": 27, "title": "Mock Checklist 27"},
    {"id": 28, "title": "Mock Template 28"},
    {"id": 29, "title": "Mock Tool 29"},
    {"id": 30, "title": "Mock Resource 30"},
]


@router.get("/", summary="Get content library with search, filtering, pagination")
async def get_content_library(
    user: str = Depends(get_current_user),
    q: Optional[str] = Query(None, description="Search keyword"),
    type: Optional[str] = Query(None, description="Filter by content type"),
    author: Optional[str] = Query(None, description="Filter by author"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
):
    filters = {"type": type, "author": author}
    result = apply_filters_and_pagination(MOCK_CONTENT, q, filters, page, limit)
    return {"user": user, **result}
