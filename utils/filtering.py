from typing import List, Dict, Optional


def apply_filters_and_pagination(
    data: List[Dict],
    q: Optional[str] = None,
    filters: Optional[Dict[str, str]] = None,
    page: int = 1,
    limit: int = 10,
    sort_by: Optional[str] = None,
    order: str = "asc",
):
    """
    Apply search, filtering, sorting, and pagination on a list of dictionaries.
    """
    results = data

    # Apply search
    if q:
        results = [item for item in results if q.lower() in item["title"].lower()]

    # Apply filtering
    if filters:
        for key, value in filters.items():
            if value:
                results = [
                    item
                    for item in results
                    if key in item and str(item[key]).lower() == value.lower()
                ]

    # Apply sorting
    if sort_by and sort_by in results[0]:
        reverse = order.lower() == "desc"
        results = sorted(
            results, key=lambda x: str(x[sort_by]).lower(), reverse=reverse
        )

    # Pagination
    total = len(results)
    start = (page - 1) * limit
    end = start + limit
    paginated_results = results[start:end]

    return {
        "total": total,
        "page": page,
        "per_page": limit,
        "has_next": end < total,
        "data": paginated_results,
    }
