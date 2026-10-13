# Mapping a Markdown API doc → OpenAPI 3.x for `apifox import`

## Why OpenAPI (not per-endpoint CLI edits)

`apifox import --format openapi` creates many endpoints + modules in one call,
preserving field types, `required` flags, enums, and example responses. Editing
16 endpoints one-by-one via `endpoint update` is risky because that command is a
full-replace and can clobber existing fields.

## Pipeline

1. Read the markdown doc; extract per endpoint: method, path, group (→ tag/module),
   request params (path/query/body), response fields, enums, examples, error codes.
2. Use `scripts/build_openapi.py` helpers to populate `build_schemas()` and
   `build_paths()`. Keep response models named `<Op>Response` / `<Op>Request`.
3. Group endpoints under `tags` that match the doc's section names; each distinct
   tag becomes an Apifox module (folder).
4. Emit JSON with `ensure_ascii=False` so Chinese descriptions survive.

## Pitfalls

- **Multi-method same path:** build one `paths[path]` dict containing BOTH
  methods (`{"get": ..., "post": ...}`). If you assign
  `paths[path] = {"get": ...}` then `paths[path] = {"post": ...}`, the second
  overwrites the first and you silently lose one operation (the openapi op count
  comes out one short; `import` reports `ignoreCount: 1`).
- **Enums:** declare via `"enum": [...]` on the property so Apifox shows allowed
  values (e.g. status: draft/published/archived).
- **Examples:** set `"example"` on properties and/or `"example"` on the 200
  response content so reviewers see realistic payloads.
- **Validation:** always `json.load` the output and print
  `sum(len(v) for v in d['paths'].values())` to confirm the operation count
  equals the doc's endpoint count before importing.

## Import report interpretation

- `createCount` = number of *path-level* items (a path with GET+POST counts once).
- `folder createCount` = number of modules created from tags.
- `ignoreCount` > 0 usually means a duplicate/conflicting path was skipped — check.
- `errorCount` should be 0.
- After import, verify with `endpoint list` (authoritative count), not
  `project get` (its `endpointCount` may be a stale cache showing 0).
