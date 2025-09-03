# movie-ratings-analysis

This project analyzes a Kaggle IMDb Top 1000 dataset, including movie titles, genres, ratings, and runtimes.

## Features
- Cleans missing data using **NumPy mean imputation**
- Identifies **Top 10 movies by rating per genre**
- Calculates **correlation** between runtime and rating
- Provides visualizations (**scatter plot** + **bar chart**)

## Dataset
[Kaggle - IMDb Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

> You need a free Kaggle account to download the CSV.

## How to Run
1. Download the dataset CSV (`imdb_top_1000.csv`) from Kaggle.  
2. Place it in the project folder (or adjust the path in `Movies.py`).  
3. Open `Movies.py` or a Jupyter Notebook and run the code.

## Notes
The Kaggle CSV column names differ from OpenDataBay, so the code handles:  
- `Series_Title` → Movie title  
- `IMDB_Rating` → Rating  
- `Runtime` → Runtime (converted to numeric)  
- `Genre` → Extracts main genre for analysis

## Example Outputs
- Scatter plot: Movie Runtime vs Rating  
- Bar chart: Average Rating per Genre  
- Top 10 movies per genre printed in console
