# JSON Flattener CLI

A standard-library Python CLI that converts nested JSON records into a flat CSV table.

## Features

- recursively flattens nested dictionaries using dotted column names;
- serializes list values as JSON text so their structure is preserved;
- builds a union of fields across every record;
- creates missing output directories;
- reports invalid roots and malformed records clearly.

## Usage

The JSON root must be a list of objects.

```bash
python -m src.main data/input.json data/output.csv
```

Example input:

```json
[{"id": 1, "profile": {"city": "Warsaw"}, "tags": ["python", "data"]}]
```

The corresponding columns include `id`, `profile.city`, and `tags`.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Stack

Python 3.11+, argparse, json, csv, pytest. Runtime dependencies: none.
