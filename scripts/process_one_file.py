import pandas as pd

file_path = "../raw_dataset/sms-call-internet-mi-2013-11-01.txt"

df = pd.read_csv(
    file_path,
    sep="\t",
    header=None
)

print(df.head())
print(df.shape)


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

print(df.head())

memory_before = (
    df.memory_usage(deep=True)
    .sum()
    / 1024**2
)

print(
    f"Memory before: {memory_before:.2f} MB"
)

df = df[
    [
        "square_id",
        "time_interval",
        "internet"
    ]
]

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

df["square_id"] = (
    df["square_id"]
    .astype("int16")
)

df["internet"] = (
    df["internet"]
    .astype("float32")
)


memory_after = (
    df.memory_usage(deep=True)
    .sum()
    / 1024**2
)

print(
    f"Memory after: {memory_after:.2f} MB"
)

df.to_parquet(
    "../processed_dataset/test.parquet",
    index=False
)
