#!/usr/bin/env python3
"""
build_openapi.py — Reusable scaffolding to turn an Apifox-targeted markdown API doc
into a valid OpenAPI 3.x JSON file for `apifox import --format openapi`.

This is a TEMPLATE. The helper functions are the reusable part; the
`build_paths()` / `build_schemas()` sections are where you map the specific
markdown document into operations and models.

Usage:
    python3 build_openapi.py <input.md> -o /tmp/out.openapi.json
    # input.md is accepted for context/logging; adaptation happens in build_paths().

Then validate and count:
    python3 -c "import json;d=json.load(open('/tmp/out.openapi.json'));print('ops',sum(len(v) for v in d['paths'].values()))"
"""
import argparse
import json
import re
from collections import OrderedDict

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def norm(name: str) -> str:
    """CamelCase / PascalCase a raw identifier into a safe schema name."""
    s = re.sub(r"[^0-9a-zA-Z]+", " ", name).strip()
    return "".join(p[:1].upper() + p[1:] for p in s.split())


def prop(typ, description=None, example=None, enum=None, items=None,
         fmt=None, required=False):
    p = {"type": typ}
    if description:
        p["description"] = description
    if fmt:
        p["format"] = fmt
    if enum is not None:
        p["enum"] = enum
    if example is not None:
        p["example"] = example
    if typ == "array" and items is not None:
        p["items"] = items
    if required:
        p["x-required"] = True  # informational; required-ness tracked separately
    return p


def ref(name: str) -> dict:
    return {"$ref": f"#/components/schemas/{name}"}


def model(name: str, props: "OrderedDict", required: list = None) -> dict:
    m = {"type": "object", "properties": props}
    if required:
        m["required"] = required
    return m


def body(schema, description=None) -> dict:
    """schema may be a $ref dict or an inline object."""
    if isinstance(schema, str):
        schema = ref(schema)
    b = {"content": {"application/json": {"schema": schema}}}
    if description:
        b["description"] = description
    return b


def query(name, typ="string", description=None, required=False):
    q = {"name": name, "in": "query", "schema": {"type": typ}}
    if description:
        q["description"] = description
    if required:
        q["required"] = True
    return q


def path_param(name, typ="string", description=None):
    p = {"name": name, "in": "path", "schema": {"type": typ}, "required": True}
    if description:
        p["description"] = description
    return p


def resp_200(model_ref=None, example=None):
    content = {}
    if model_ref is not None:
        content["application/json"] = {"schema": ref(model_ref)}
        if example is not None:
            content["application/json"]["example"] = example
    return {"200": {"description": "成功", "content": content}} if content else \
           {"200": {"description": "成功"}}


def errs(*codes):
    msgs = {
        "400": "参数错误 / 请求非法",
        "401": "未认证 / 无访问权限",
        "403": "禁止访问",
        "404": "资源不存在",
        "500": "服务器内部错误",
    }
    out = {}
    for c in codes:
        out[c] = {"description": msgs.get(c, "错误")}
    return out


def op(tags, operation_id, summary, description=None, parameters=None,
       request_body=None, responses=None):
    o = {"tags": tags, "operationId": operation_id, "summary": summary}
    if description:
        o["description"] = description
    if parameters:
        o["parameters"] = parameters
    if request_body:
        o["requestBody"] = request_body
    o["responses"] = responses or {"200": {"description": "成功"}}
    return o


# ---------------------------------------------------------------------------
# Document-specific section — EDIT PER MARKDOWN DOC
# ---------------------------------------------------------------------------

BASE = "/api"  # adjust to the doc's base path prefix

def build_schemas():
    """Return OrderedDict of #/components/schemas from the markdown doc."""
    schemas = OrderedDict()
    # Example:
    # schemas["FooRequest"] = model("FooRequest",
    #     OrderedDict([("id", prop("integer", example=1)),
    #                  ("name", prop("string", required=True))]),
    #     required=["name"])
    return schemas


def build_paths(schemas):
    """Return the OpenAPI `paths` object. Merge methods on one key per path."""
    paths = OrderedDict()
    # Example:
    # paths[BASE + "/foos"] = {
    #     "get": op(["分组名"], "listFoos", "查询列表",
    #               responses={**resp_200("FooList", {"list": []}), **errs("500")}),
    #     "post": op(["分组名"], "createFoo", "创建",
    #                request_body=body("FooRequest"),
    #                responses={**resp_200("FooResponse"), **errs("400")}),
    # }
    return paths


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def build(title, version="1.0.0", server=None):
    schemas = build_schemas()
    paths = build_paths(schemas)
    spec = OrderedDict()
    spec["openapi"] = "3.0.3"
    spec["info"] = {"title": title, "version": version}
    if server:
        spec["servers"] = [{"url": server}]
    spec["paths"] = paths
    spec["components"] = {"schemas": schemas}
    return spec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_md", help="source markdown API doc (for context)")
    ap.add_argument("-o", "--output", default="/tmp/out.openapi.json")
    ap.add_argument("--title", default="API")
    ap.add_argument("--server", default=None)
    args = ap.parse_args()

    spec = build(args.title, server=args.server)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
    ops = sum(len(v) for v in spec["paths"].values())
    print(f"wrote {args.output}: {len(spec['paths'])} paths, {ops} operations, "
          f"{len(spec['components']['schemas'])} schemas")


if __name__ == "__main__":
    main()
