from json import load



def output_database(table_value: str) -> dict:
    """Parse JSON file and return dict"""
    with open(f"database/{table_value}.json", "r", encoding="utf-8") as file:
        json_text = load(file)
        return json_text

    
        
