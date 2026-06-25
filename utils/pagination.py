def paginate(
    query,
    page: int = 1,
    size: int = 10
):
    return query.offset(
        (page - 1) * size
    ).limit(size)