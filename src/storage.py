import csv
from pathlib import Path

def save_csv(filename, rows):
    if not rows:
        return 
    
    fields = list(dict.fromkeys(key for row in rows for key in row))
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
