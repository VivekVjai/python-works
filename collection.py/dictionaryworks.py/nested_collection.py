

movies=[
        
        {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
        
        {"id":2,"title":"kgf2","year":2022,"language":"kannada","run_time":120},

        {"id":3,"title":"goat","year":2020,"language":"tamil","run_time":130},

        {"id":4,"title":"vazha","year":2022,"language":"malayalam","run_time":130},

        {"id":5,"title":"arm","year":2024,"language":"malayalam","run_time":150},
   

]

#count of movies

print(len(movies))

#print all movie title

for m in movies:

    print(m.get("title"))


#using list comprehesion

movie_titles=[m.get("title") for m in movies]

print(movie_titles)

#movie with highest run time 

highest_runtime_movie=max(movies,key=lambda m:m.get("run_time"))

print(highest_runtime_movie.get("title"))

#movie with lowest run time 

lowest_runtime_movie=min(movies,key=lambda m:m.get("run_time"))

print(lowest_runtime_movie)

#rand movies same run time undel athu randum enganae print aakum 


highest_runtime_movie=max(movies,key=lambda m:m.get("run_time"))

max_run_time=highest_runtime_movie.get("run_time")

max_runtime_movies=[m.get("title") for m in movies if m.get("run_time")==max_run_time]

print(max_runtime_movies)


#malayalam movies

malyalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]

print(malyalam_movies)

print(len(malyalam_movies))

#in which year most number of movies released

movies_year=[m.get("year") for m in movies]

print(movies_year)

year_count={y:movies_year.count(y) for y in movies_year}

print(year_count)

