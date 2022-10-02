def cleanEmptyValue(obj, items_copy):
    for key, value in items_copy:
        if not value:
            del obj[key]
    return obj
