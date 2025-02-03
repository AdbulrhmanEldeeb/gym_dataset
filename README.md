# Gym Membership Data Analysis  

## Overview  
This project analyzes gym membership data to extract insights about member behaviors, subscriptions, and habits. Various visualizations and summary statistics are generated using Python, Pandas, and Plotly.  
## 📌 Dataset on Kaggle  
[Gym Membership Dataset](https://www.kaggle.com/datasets/ka66ledata/gym-membership-dataset)  

## 📊 Kaggle Notebook  
[Gym Membership Data Analysis](https://www.kaggle.com/code/abdulrhmaneldeeb/gym-eda0)  

## Features  
- **Exploratory Data Analysis (EDA)**: Understanding the dataset with descriptive statistics.  
- **Visualization**: Interactive charts and plots to explore patterns.  
- **Data Aggregation**: Summarizing data by gender, age, and subscription type.  
- **Exporting Insights**: Saving key statistics as `.txt` and `.csv` files.  

## Data Processing  
- Extracted key metrics such as **average time in gym**, **visit frequency**, and **personal training participation**.  
- Generated pivot tables to compare trends by **gender** and **subscription type**.  
- Segmented data into different age groups (e.g., members over 45 and under 15).  
## Association Rule Mining
- notebook of association rules [here](notebooks/assosiation_rules_.ipynb)
- data of association rules [here](/association_rules)
- Using the Apriori algorithm, we identified frequent itemsets and association rules in gym members' preferred group lessons.

Key Insights

- Frequent Itemsets: Popular combinations of gym classes members frequently attend together.

- Association Rules: Relationships between different classes based on member preferences.

## Visualizations  
1. **Bar Charts**:  
   - Popular gym lessons  
   - Distribution of favorite drinks  
   - Number of personal trainers and their clients  

2. **Histograms & KDE Plots**:  
   - Distribution of **average time spent in the gym**  
   - Peak check-in hours  

3. **Pie Charts**:  
   - **Drink subscription usage**  
   - **Sauna usage distribution**  
   - **Personal training participation**  

## File Outputs  
- `../data/over_45_age.csv`: Data for gym members over 45 years old  
- `../data/lower_than_15_age.csv`: Data for gym members under 15 years old  
- `../outputs/gender_summary_stats_*.txt`: Summary statistics for different metrics grouped by gender  
- `../vis/*.html`: Interactive Plotly visualizations  

## Requirements  
- Python 3.x  
- Pandas  
- Plotly  
- NumPy  
- mlxtend

