import pandas as pd
import matplotlib.pyplot as plt
#load the csv file

data = pd.read_csv('C:/Users/PawPaw/PycharmProjects/HorrorMovieProject/horror_movies.csv')

#Filer for horror genre

horror_movies = data[data['genre_names'].str.contains('Horror', na=False)]

#drop rows with missing values in the key columns

horror_movies = horror_movies.dropna(subset=['title', 'popularity', 'release_date'])

#keeping relevant columns
horror_movies = horror_movies[['title', 'popularity', 'release_date']]

#converting the release_date column to datetime and extracting the yar

horror_movies['release_date'] = pd.to_datetime(horror_movies['release_date'], errors='coerce')
horror_movies['year'] = horror_movies['release_date'].dt.year

#Grouping by decade
horror_movies['decade'] = (horror_movies['year']//10) * 10

#The above code is the exact copy of the first half of he Grouping_by_decade python file
#Now will investigate the 2020s spike in horror popularity.

#creating a new dataframe specific to the 2020s to investigate the source of the spike
horror_movies_2020s = horror_movies[horror_movies['decade']== 2020]

#now I will be sorting by popularity to see if I can locate any oddities
top_movies_2020s = horror_movies_2020s.sort_values(by='popularity', ascending=False)

#results
#print(top_movies_2020s.head(20))

#Something is still off, so going to break down by year now
year_counts = horror_movies_2020s['year'].value_counts().sort_index()
print("Number of movies per year in the 2020s")
print(year_counts)

#This next step will allow me to compare paopuarlity across years in the 2020s
average_popularity_per_year = horror_movies_2020s.groupby('year')['popularity'].mean().reset_index()
print('\nAverage popularity per year in the 2020s:')
print(average_popularity_per_year)
