# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')

netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

short_movies = netflix_movies[netflix_movies['duration'] < 60]
print(short_movies.head(20))

genre_colors = {
    'Children': 'blue',
    'Documentaries': 'green',
    'Stand-Up': 'orange'}
colors = []
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre in genre_colors:
        colors.append(genre_colors[genre])
    else:
        colors.append('gray')
        
fig, ax = plt.subplots()

scatter = ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')

plt.show()

answer = 'no'