from datetime import datetime

def test_datetime():
    now = datetime.now()
    print(f"[Datetime] Поточна дата і час: {now.strftime('%Y-%m-%d %H:%M:%S')}")