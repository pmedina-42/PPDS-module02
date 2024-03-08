import pandas as pd


def load(path: str):
    """carga a tu puta madre"""
    try:
        assert path.endswith('.csv'), "invalid file format"
        data = pd.read_csv(path)
        dimensions = data.shape
        print(f"Loading dataset of dimensions {dimensions}")
        return data
    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")
    except FileNotFoundError as fnfe:
        print(f"{type(fnfe).__name__}: file not found")
    except PermissionError as pe:
        print(f"{type(pe).__name__}: {pe}")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
