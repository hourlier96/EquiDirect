def set_foreign_key(payload: dict, entity: str, id: int) -> dict:
    payload[entity] = {
        "connect": {
            "id": id,
        }
    }
    return payload
