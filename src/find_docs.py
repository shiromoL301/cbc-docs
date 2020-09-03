import json
from typing import Union


def get_all_docs(DEBUG=True) -> dict:
    with open("./md/manifest.json", "r") as f:
        manifest = json.load(f)

    result = manifest["docs"]
    if DEBUG:
        result = list(
            map(lambda x: {**x, "path": f"/docs/{x['path']}"}, result))
    else:
        result = list(
            map(lambda x: {**x, "path": f"{x['path']}.html"}, result))

    return result


def find_doc(target_name: str) -> Union[dict, None]:
    with open("./md/manifest.json", "r") as f:
        manifest = json.load(f)

    if target_name == "" or manifest["docs"] == []:
        print("target_name or manifest not found")
        return None

    for m in manifest["docs"]:
        if target_name == m["path"]:
            return m

    return None
