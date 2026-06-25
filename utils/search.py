from sqlalchemy import or_


def apply_search(query, model, search: str, fields: list):

    if not search:
        return query

    conditions = []

    for field in fields:
        conditions.append(
            getattr(model, field).ilike(f"%{search}%")
        )

    return query.filter(or_(*conditions))