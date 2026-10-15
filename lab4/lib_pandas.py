import pandas as pd

def test_pandas():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print(f"[Pandas] DataFrame:\n{df}")