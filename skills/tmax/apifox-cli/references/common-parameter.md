# Common Parameter (common-parameter create) — JSON template

Add a request header to ALL endpoints in a project via a project-level common
parameter (the standard Apifox way to "add an auth/trace header to every API").

## Get the authoritative schema first (do not guess field names/enums)

```bash
bash <skill>/scripts/apifox.sh cli-schema get common-parameter-create
```

## Template payload

```json
{
  "parameters": {
    "header": [
      {
        "name": "x-contact-id",
        "description": "联系人 ID，用于鉴权/身份解析",
        "type": "string",
        "required": true,
        "defaultValue": "20017344941",
        "defaultEnable": true,
        "enable": true
      }
    ]
  }
}
```

## Field notes

- Top level must be `parameters`, whose value is structured by location:
  `header`, `query`, `path`, `cookie` (use the one matching the param `in`).
- Header item required fields: `name`. Commonly set: `type` (string/integer/...),
  `required`, `defaultValue`, `defaultEnable`, `enable`, `description`.
- `defaultEnable: true` + `enable: true` => the header is inherited and
  auto-applied by every endpoint in the project (endpoint's own
  `commonParameters` stays `{}` = "inherit, not overridden").
- Validate before create:
  ```bash
  bash <skill>/scripts/apifox.sh cli-schema validate common-parameter-create --file /tmp/cp.json
  ```
- Create:
  ```bash
  bash <skill>/scripts/apifox.sh common-parameter create --project <projectId> --file /tmp/cp.json
  ```
- Verify:
  ```bash
  bash <skill>/scripts/apifox.sh common-parameter list --project <projectId>
  ```
