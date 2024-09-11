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
decade_group = horror_movies.groupby('decade')['popularity'].mean().reset_index()

#display the grouped data
#print(decade_group)


# Creating the visualization for the data
#plotting the popularity of horror by decade

plt.figure(figsize=(10,6))
plt.plot(decade_group['decade'], decade_group['popularity'], marker='o', linestyle='-')
plt.title('Average Popularity of Horror Movies by Decade')
plt.xlabel('Decade')
plt.ylabel('Average Popularity')
plt.xticks(decade_group['decade'])
plt.show()
