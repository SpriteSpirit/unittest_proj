def get_val(collection, key, default='git'):
    if collection is None:
        collection = {}

    if len(collection) == 0:
        return default

    if key is None:
        key = ""

    if key in collection:
        return collection[key]
    else:
        return default
