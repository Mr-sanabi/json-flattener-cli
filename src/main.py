import argparse

from src.json_loader import load_json
from src.flattener import flatten_records
from src.storage import save_csv

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    return parser.parse_args()



def main():
    args = parse_args()

    records = load_json(args.input_file)

    if records is None:
        return
    
    if not isinstance(records, list):
        print("Error: JSON root must be a list of records")
        return
    
    if not records:
        print("Warning: JSON list is empty")
        return
    
    try:
        rows = flatten_records(records)
    except TypeError as error:
        print(f"Error: {error}")
        return
    save_csv(args.output_file, rows)


    print(f"Records loaded: {len(records)}")
    print(f"Rows flattened: {len(rows)}")
    print(f"Rows saved: {len(rows)}")
    print(f"Output file: {args.output_file}")


if __name__ == "__main__":
    main()
