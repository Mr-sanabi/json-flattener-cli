def flatten_dict(data, parent_key=""):
    result = {}

    for key, value in data.items():
        if parent_key == "":
            new_key = key
        else:
            new_key = parent_key + "." + key
            
        if isinstance(value, dict):
            nested_result = flatten_dict(value, new_key)
            result.update(nested_result)
        else:
            result[new_key] = value
        
    return result

def flatten_records(records):
    rows = []
    for record in records:
        flat_records = flatten_dict(record)
        rows.append(flat_records)
    
    return rows