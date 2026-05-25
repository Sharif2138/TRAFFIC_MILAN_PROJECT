# Comparative Time Series Analysis and Forecasting of Mobile Network Traffic

## Overview

This project explores mobile network traffic patterns in Milan, Italy using the Telecom Italia Mobile (TIM) dataset.

The work was completed as part of a Machine Learning for Sequential Data assignment and focuses on three main goals:

1. Processing a large telecommunications dataset (~5 GB) efficiently
2. Exploring temporal and spatial traffic patterns
3. Comparing three forecasting models:

- ARIMA
- LSTM
- GRU

The main objective was to predict future mobile network traffic and compare how different forecasting approaches perform in terms of prediction accuracy and computational efficiency.

---

### Forecasting Design

After testing different configurations, a lookback window of 24 observations was selected.

This represents roughly four hours of historical traffic data.

To keep the comparison fair, the same preprocessing pipeline was used across all three geographical areas included in the forecasting experiments.

---

## Repository Structure

```text
.
├── Task3_forecasting.ipynb
├── task2_eda.ipynb
├── scripts
├── raw_dataset
├── milan_final.parquet
├── processed_data
├── README.md
└── requirements.txt
```

---

## Installation

```bash
git clone git@github.com:Sharif2138/TRAFFIC_MILAN_PROJECT.git
cd traffic_milan_project
pip install -r requirements.txt
```

---

## Running the Project

Download the dataset from Havard dataverse link "[https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGZHFV](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGZHFV)" to your local laptop
put all files into a raw data folder
then run the pythin files in the scripts folder to process the files and store them into processed_data folder where they a merged into one file called milan_final.parquet

Run the notebooks in the following order:

1. scripts – Data Handling and Memory Management
2. Task 2 – Exploratory Data Analysis
3. Task 3 – Forecasting Models

Following this order reproduces the figures, tables, and results discussed in the final report.

---

## Main Results

### Best Performing Model

Among the three forecasting approaches, GRU achieved the best overall performance.

| Model | Average RMSE |
|-------|-------------|
| GRU | 62.77 |
| LSTM | 64.06 |
| ARIMA | 709.51 |

### Main Findings

Some key observations from the analysis include:

- Mobile traffic follows clear daily and weekly patterns
- Traffic distribution across Milan is highly uneven
- Central areas generate noticeably higher traffic volumes
- GRU provided the best balance between accuracy and training time
- ARIMA struggled to capture the nonlinear nature of mobile traffic behaviour

---

## Limitations

The models still faced challenges when predicting sudden traffic spikes.

Possible reasons for these forecasting errors include:

- Public events
- Holidays
- Unexpected user behaviour

Since these situations appeared less frequently in the training data, they were harder for all models to learn and predict accurately.

---

## References

The complete IEEE reference list can be found in the final report.

---

## AI Usage Statement

AI tools were used for debugging assistance, and explanations. However, all code, analysis, interpretations, model selection decisions, and final conclusions were verified and fully understood by the author before submission.