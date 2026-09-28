# Delivery Performance Analytics

Data analytics project developed as part of my **IHK Data Analytics certification**.

The project analyzes e-commerce delivery data to identify factors associated with delivery delays and translate the findings into actionable business insights.

## Project Objective

The analysis focuses on understanding how operational factors such as:

- delivery distance
- delivery time windows
- traffic conditions
- weather
- driver experience
- package characteristics

relate to the risk of delayed deliveries.

## Key Insight

By combining multiple operational factors, deliveries were grouped into risk classes.

The observed delay rate increased across the three risk levels:

- **Low risk:** 26.3%
- **Elevated risk:** 42.6%
- **High risk:** 55.4%

The analysis also showed that long delivery distances combined with short delivery windows were associated with particularly high delay rates.

## Workflow

1. Data cleaning and validation
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Statistical analysis
5. Risk classification
6. Dashboard development and visualization

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Statistical Analysis
- Power BI
- Tableau
- Jupyter Notebook

## Tableau Dashboard

[View the interactive Delivery Performance Dashboard](https://public.tableau.com/views/IHK_Lieferanalyse_Final/LieferperformanceAnalysederVersptungsrisiken?:language=de-DE&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Repository Structure

- `eda_feature_engineering.ipynb` — exploratory analysis and feature engineering
- `eda_feature_engineering.py` — Python analysis workflow
- `lieferungen_cleaned.csv` — cleaned delivery dataset
- `lieferdaten_ml_vorbereitet.csv` — dataset prepared for machine learning
- `lieferdaten_tableau.csv` — dataset prepared for visualization
- `DE.txt` — supporting German postal-code data

## About

This project demonstrates my approach to combining **data analysis, business understanding and visualization** to identify operational patterns and support data-driven decision-making.