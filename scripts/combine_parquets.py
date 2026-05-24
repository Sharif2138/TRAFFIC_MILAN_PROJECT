import pandas as pd

from pathlib import Path
from tqdm import tqdm

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = (
    BASE_DIR / "processed_dataset"
)

files = sorted(
    PROCESSED_DIR.glob("*.parquet")
)

print(
    f"Found {len(files)} parquet files"
)

dfs = []

for file in tqdm(files):

    df = pd.read_parquet(file)

    dfs.append(df)

final_df = pd.concat(
    dfs,
    ignore_index=True
)

final_df = final_df.sort_values(
    [
        "square_id",
        "time_interval"
    ]
)

print(
    final_df.shape
)

output_file = (
    BASE_DIR / "milan_final.parquet"
)

final_df.to_parquet(
    output_file,
    index=False
)

print(
    f"Saved to {output_file}"
)
