import pandas as pd
from typing import List
from schemas import RecordCreate

def validate_csv(file) -> List[RecordCreate]:
    df = pd.read_csv(file.file)

    expected = ['name', 'age', 'score']
    if not all(col in df.columns for col in expected):
        raise ValueError("CSV must contain name, age, and score columns")

    df = df.dropna()
    df['age'] = df['age'].astype(int)
    df['score'] = df['score'].astype(float)

    return [RecordCreate(**row) for row in df.to_dict(orient="records")]
