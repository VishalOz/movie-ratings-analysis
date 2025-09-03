# 🎬 Movie Ratings Analysis (IMDb Top 1000 Kaggle Dataset)
# --------------------------------------------------------
# Tasks:
# 1. Load Kaggle IMDb Top 1000 dataset
# 2. Handle missing values with NumPy
# 3. Find top 10 movies by rating per genre
# 4. Calculate correlation between runtime & rating
# 5. Visualize results

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# 1. Load the dataset
# --------------------------
df = pd.read_csv('./src/imdb_top_1000.csv')  # adjust path if needed

# Quick overview
print("First 5 rows:")
print(df.head(), "\n")

print("Dataset shape:", df.shape)
print("Columns:", df.columns, "\n")

# --------------------------
# 2. Handle Missing Values
# --------------------------

# Clean Runtime column: remove 'min' and convert to float
df['Runtime'] = df['Runtime'].str.replace(" min","").astype(float)

# Fill missing numeric values with mean using NumPy
df['IMDB_Rating'] = df['IMDB_Rating'].fillna(np.nanmean(df['IMDB_Rating']))
df['Runtime'] = df['Runtime'].fillna(np.nanmean(df['Runtime']))

# Extract main genre (take first genre if multiple)
df['main_genre'] = df['Genre'].str.split(',').str[0]

# --------------------------
# 3. Top 10 Movies by Rating per Genre
# --------------------------
top_10_per_genre = (
    df.groupby('main_genre', as_index=False)
      .apply(lambda x: x.nlargest(10, 'IMDB_Rating'))
      .reset_index(drop=True)
)

# Display results
for genre, group in top_10_per_genre.groupby('main_genre'):
    print(f"\n--- Top 10 in {genre} ---")
    print(group[['Series_Title', 'IMDB_Rating', 'Runtime']])

# --------------------------
# 4. Correlation between Runtime & Rating
# --------------------------
corr = df['Runtime'].corr(df['IMDB_Rating'])
print(f"\nCorrelation between Runtime and Rating: {corr:.3f}")

# --------------------------
# 5. Visualization
# --------------------------

# Scatter Plot: Runtime vs Rating
plt.figure(figsize=(8,5))
plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.6, c='blue')
plt.title('Movie Duration vs. Rating')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('IMDB Rating (0–10)')
plt.grid(True)
plt.show()

# Bar Chart: Average Rating per Genre
avg_rating_per_genre = df.groupby('main_genre')['IMDB_Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
avg_rating_per_genre.plot(kind='bar', color='orange')
plt.title('Average IMDB Rating per Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()
