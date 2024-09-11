import pandas as pd

#loading the CSV file I got on Kaggle

data = pd.read_csv('horror_movies.csv')


horror_movies = data[data['genre_names'].str.contains('Horror', na=False)]

#checking for missing values
print(horror_movies.isnull().sum())


#drop rows with missing values in key columns and adjust column names if necessary
horror_movies = horror_movies[['title', 'popularity', 'release_date']]

#Keeping the relevant columns
horror_movies = horror_movies[['title', 'popularity', 'release_date']]

print(horror_movies.columns)