import json

def test_json():
    data = {"name": "Lab 4", "completed": True}
    json_str = json.dumps(data)
    print(f"[JSON] Серіалізований рядок: {json_str}")