import pandas as pd
import numpy as np

from pathlib import Path
from tqdm import tqdm

import gc

# locate files

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "raw_dataset"

PROCESSED_DIR = BASE_DIR / "processed_dataset"

PROCESSED_DIR.mkdir(
    exist_ok=True
)

# find files
files = sorted(
    RAW_DIR.glob("*.txt")
)

print(
    f"Found {len(files)} files"
)

# process each file

for file in tqdm(files):

    try:

        print(
            f"\nProcessing: {file.name}"
        )

        df = pd.read_csv(
            file,
            sep="\t",
            header=None
        )

        # rename columns
        df.columns = [
            "square_id",
            "time_interval",
            "country_code",
            "sms_in",
            "sms_out",
            "call_in",
            "call_out",
            "internet"
        ]

        # measure memory before processing
        memory_before = (
            df.memory_usage(
                deep=True
            ).sum()
            / 1024**2
        )

        # keep required columns
        df = df[
            [
                "square_id",
                "time_interval",
                "internet"
            ]
        ]

        # Handle missing values
        df["internet"] = (
            df["internet"]
            .fillna(0)
        )

        df = (
            df
            .groupby(
                [
                    "square_id",
                    "time_interval"
                ]
            )
            ["internet"]
            .sum()
            .reset_index()
        )

        # optimise data types
        df["square_id"] = (
            df["square_id"]
            .astype(np.int16)
        )

        df["time_interval"] = (
            df["time_interval"]
            .astype(np.int64)
        )

        df["internet"] = (
            df["internet"]
            .astype(np.float32)
        )

        # Measure memory after processing
        memory_after = (
            df.memory_usage(
                deep=True
            ).sum()
            / 1024**2
        )

        # save parquet
        output_file = (
            PROCESSED_DIR
            / f"{file.stem}.parquet"
        )

        df.to_parquet(
            output_file,
            index=False
        )

        print(
            f"Rows: {len(df):,}"
        )

        print(
            f"Memory Before: "
            f"{memory_before:.2f} MB"
        )

        print(
            f"Memory After: "
            f"{memory_after:.2f} MB"
        )

        del df

        gc.collect()

    except Exception as e:

        print(
            f"Error processing "
            f"{file.name}"
        )

        print(e)

print(
    "\nAll files processed!"
)
