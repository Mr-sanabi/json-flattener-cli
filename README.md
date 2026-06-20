# JSON Flattener CLI

A small Python CLI tool that reads nested JSON records, flattens nested fields using dot notation, and exports the result to a clean CSV file.

## Features

- Reads JSON data from a local file
- Supports a list of JSON records
- Flattens nested dictionaries using dot notation
- Converts nested fields like `address.city` and `company.name` into CSV columns
- Exports flattened records to CSV
- Uses argparse for input and output file paths
- Handles missing files, invalid JSON, non-list JSON roots, and empty JSON lists

## Tech Stack

- Python
- json
- csv
- argparse

## Usage

```bash
python src/main.py <input_file> <output_file>
```

Example:

```bash
python src/main.py examples/sample.json data/output.csv
```

## Example input

```json
[
  {
    "id": 1,
    "name": "John Miller",
    "address": {
      "city": "Warsaw",
      "country": "Poland"
    },
    "company": {
      "name": "Northwind Trading"
    }
  }
]
```

## Example output columns

```text
id,name,address.city,address.country,company.name
```

## What I practiced

- Reading JSON files
- Working with nested dictionaries
- Recursive flattening
- Converting JSON records into CSV rows
- Building a small CLI tool
- Basic input validation and error handling