import csv

import pytest

from src.flattener import flatten_records
from src.storage import save_csv


def test_nested_records_and_lists_are_flattened():
    rows = flatten_records([{"id": 1, "profile": {"city": "Kyiv"}, "tags": ["a", "b"]}])
    assert rows == [{"id": 1, "profile.city": "Kyiv", "tags": '["a", "b"]'}]


def test_non_object_record_is_rejected():
    with pytest.raises(TypeError):
        flatten_records(["invalid"])


def test_csv_uses_union_of_fields(tmp_path):
    output = tmp_path / "nested" / "rows.csv"
    save_csv(output, [{"id": 1}, {"id": 2, "name": "Ada"}])
    with output.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    assert rows[0] == {"id": "1", "name": ""}
    assert rows[1] == {"id": "2", "name": "Ada"}
