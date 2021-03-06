import json
import hashlib


def json_hash(obj):
    dump = json.dumps(obj, sort_keys=True)
    h = hashlib.sha256()
    h.update(dump)
    return h.hexdigest()
