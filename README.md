# DC-Project_5 — Investigating Netflix Movies

**Author:** Completed independently by Ivan Shelest

**Based on DataCamp project:** [Investigating Netflix Movies](https://app.datacamp.com/learn/projects/1674)

---

## Project Description

Netflix, founded in 1997 as a DVD rental service, has grown into one of the world’s largest entertainment and media companies. With thousands of movies and series available globally, it provides an ideal dataset for exploring patterns and trends within the entertainment industry.

In this project, exploratory data analysis (EDA) is performed on a dataset of Netflix titles to investigate whether **movie durations have been decreasing over time** and what genres or characteristics may contribute to this trend.

The analysis focuses on understanding the distribution of movie durations by year, identifying outliers, and visualizing genre-based differences in film length.

---

## Objectives

1. **Explore Netflix movie data** — filter and prepare relevant information for analysis.
2. **Investigate the trend in movie durations over time** — determine whether films are becoming shorter.
3. **Analyze genre-specific patterns** — see which genres tend to produce shorter or longer movies.
4. **Visualize findings** — build an informative scatter plot showing duration versus release year.

---

## Dataset

**File:** `netflix_data.csv`
This dataset contains information on Netflix movies and TV shows.

| Column         | Description                                |
| -------------- | ------------------------------------------ |
| `show_id`      | Unique identifier of the title             |
| `type`         | Type of show — either "Movie" or "TV Show" |
| `title`        | Title of the movie or show                 |
| `director`     | Director’s name                            |
| `cast`         | List of main cast members                  |
| `country`      | Country of origin                          |
| `date_added`   | Date the title was added to Netflix        |
| `release_year` | Year of release on Netflix                 |
| `duration`     | Duration of the movie in minutes           |
| `description`  | Short description of the title             |
| `genre`        | Show genre                                 |

---

## Methodology

1. **Data Import and Preparation**

   * Load dataset using `pandas`.
   * Filter to include only titles where `type == "Movie"`.
   * Select relevant columns: `title`, `country`, `genre`, `release_year`, and `duration`.

2. **Subset Creation**

   * Extract short movies (`duration < 60` minutes) to identify unusually short content.

3. **Genre Visualization**

   * Assign genre-specific colors for clear visual grouping:

     * `Children` — blue
     * `Documentaries` — green
     * `Stand-Up` — orange
     * All others — gray

4. **Scatter Plot Analysis**

   * Plot movie duration versus release year using `matplotlib`.
   * Observe the distribution to determine if durations trend downward.

---

## Code Summary

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
netflix_df = pd.read_csv('netflix_data.csv')

# Select movies only
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Identify short movies
short_movies = netflix_movies[netflix_movies['duration'] < 60]
print(short_movies.head(20))

# Define color scheme by genre
genre_colors = {
    'Children': 'blue',
    'Documentaries': 'green',
    'Stand-Up': 'orange'
}

colors = []
for _, row in netflix_movies.iterrows():
    colors.append(genre_colors.get(row['genre'], 'gray'))

# Plot
fig, ax = plt.subplots()
ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')
plt.show()

answer = 'no'
```

---

## Results

### Visualization — Movie Duration by Year

The scatter plot shows that:

* Movie durations fluctuate but generally **decrease slightly** after 2010.
* A noticeable cluster of **shorter movies (under 90 minutes)** appears in the 2010–2020 range.
* Genres such as **Documentaries** and **Children’s movies** have significantly shorter average durations compared to other genres.

### Short Movies

Examples of films under 60 minutes include:

* *World War II in Colour: The Gathering Storm*
* *Fittest on Earth: The Story of CrossFit*
* *Jim Gaffigan: Mr. Universe*

These belong primarily to **Documentary** or **Stand-Up** genres, which explains the lower durations.

---

## Interpretation

The analysis supports the hypothesis that while there is no drastic decline in average movie duration, **modern releases tend to be slightly shorter on average**, especially in genres like documentaries and stand-up specials.

This pattern may reflect changing viewer preferences, an increase in streaming-oriented short-form content, and the evolution of production strategies focusing on faster engagement.

---

## Technologies Used

* Python 3.12
* pandas — data manipulation
* matplotlib — visualization
* VS Code

---

## Repository Structure

```
DC-Project_5/
│
├── netflix_data.csv   # Dataset
├── main.py            # Analysis script
└── README.md          # Documentation
```

---

## Conclusion

Exploratory analysis of Netflix movie data reveals that film durations have experienced a **slight downward trend** in recent years, primarily due to the rise of short-form genres like **documentaries, children’s programming, and stand-up comedy**.
Overall, the variety of durations illustrates Netflix’s strategy to cater to diverse audiences and consumption patterns.