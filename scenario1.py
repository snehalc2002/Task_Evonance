"""*/Scenario 1: Data ValidationTask: Write a function validate_data(data) that checks if a list of dictionaries 
(e.g., [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]) contains valid integer values for
the "age" key. Return a list of invalid entries./*"""

def validate_data(data):
    return [entry for entry in data if not isinstance(entry.get("age"), int)]


info = [
    {"name": "Amit", "age": 28},
    {"name": "Neha", "age": "twenty"},
    {"name": "Ravi", "age": 45},
    {"name": "Sara"},
    {"name": "Kiran", "age": 3.5}
]


invalid = validate_data(info)
print("Invalid entries:", invalid)
