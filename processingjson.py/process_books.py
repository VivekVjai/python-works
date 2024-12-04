

from json import load

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\books.json")

data=load(f)

all_titles=[book.get("title") for book in data]

print(all_titles)

#books with pages <250

page_filter=[book.get("title") for book in data if book.get("pages")<250]

print(page_filter)

#print all genres

all_genres=[book.get("genre") for book in data]

print(set(all_genres))  #ivide set(all_genres) kodukkan karanam doubling undel ozhivakkan aanu 

#genre_count

genre_count={genre:all_genres.count(genre) for genre in all_genres}

print(genre_count)

#print costly book 

costly_book=max(data,key=lambda d:d.get("price"))

print(costly_book)

#author with more than one book 

all_author=[book.get("author") for book in data]

auther_count={author:all_author.count(author) for author in all_author}

print([k for k,v in auther_count.items() if v>1])

