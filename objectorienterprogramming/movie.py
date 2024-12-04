#movie
#title,rating,runtime,director,gener

#arm,kgf

class Movie:

    title:str
    rating:int
    runtime:int
    director:str
    genre:str

    def set_movie(self,title,rating,runtime,director,genre):
        
        self.title=title
        self.rating=rating
        self.runtime=runtime
        self.director=director
        self.genre=genre

    def display_movie(self):

        print(self.title,self.rating,self.runtime,self.director,self.genre)

movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_movie("arm",4,90,"jithinlal","fiction")

movie_instance2.set_movie("kgf",4.5,120,"prashanthneel","action")

movie_instance1.display_movie()

movie_instance2.display_movie()

