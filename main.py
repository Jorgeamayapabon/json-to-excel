from src.tool_manager import create_tables, load_json_data

data = load_json_data()
create_tables(data)