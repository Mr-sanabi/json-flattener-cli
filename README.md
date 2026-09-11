# JSON Flattener CLI

A Python 3.11+ CLI that converts a JSON list of objects into a CSV table. No runtime dependencies.

## Run

```bash
python -m src.main data/input.json data/output.csv
```

Nested dictionaries become dotted columns, such as `profile.city`. Lists remain JSON text inside cells; they are not expanded into rows. Columns include fields from all records.

Input must be a list of objects. For example: `[{"id": 1, "profile": {"city": "Warsaw"}}]`.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
