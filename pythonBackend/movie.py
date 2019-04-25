import imdb
import random 

# ia = imdb.IMDb()

# keyword_list = ia.search_keyword('sun') # will get similar keywords to search with
# movie_list = ia.get_keyword('lego') # will return movies with this keyword
# # print(movie_list)
# search = movie_list[0].movieID
# print(search)
# movie = ia.get_movie(search)
# print(movie)
# print(movie.get('genre'))
# flag = 0
# genre_list = movie.get('genre')
# for elem in genre_list:
#     if elem == genre: # movie meets genre requirement
#         flag = 1


# print(search['genre'])
# call below not working
# movie = ia.search_movie(search)
# print(movie)
# jaws = ia.get_movie('0304000')
# maybe = ia.Movie.'genre'
# print(keywordList)
# print()
# print(movie_list)
# something = ia.get_movie_infoset()
# print(something)
# print(jaws)
# print(jaws.'title'())

# will take an input genre and generate 5 possible movies of interest
def movie_rec(input):
    recs = []
    options = {
        'Action': ['destructive','violent','explosion','fast-paced'],
        'Triller': ['dark','twisted','exciting','scary'],
        'Comedy': ['hilarious','funny','parody'],
        'Animation': ['fun','delightful','cartoon'],
        'Adventure': ['explore','hazard','exciting','wild','fast-paced'],
        'Family': ['kids','cartoon','Disney','wholesome']
    }
    short_list = options.get(input)
    int = random.randint(0,len(short_list)-1)
    keyword = short_list[int]
    db = imdb.IMDb()
    movie_list = db.get_keyword(keyword)
    i = 0
    j = 0
    while i < 5:
        if j == len(movie_list):
            int = random.randint(0,len(short_list)-1)
            keyword = short_list[int]
            movie_list = db.get_keyword(keyword)
        searchID = movie_list[j].movieID
        movie = db.get_movie(searchID)
        genre_list = movie.get('genre')
        for elem in genre_list:
            if elem == input:
                flag = 1
        if flag == 1:
            recs.append(movie.get('title'))
            i += 1
            flag = 0
        j += 1
    return recs

# will turn a sentiment input into a genre recommendation
def genre_rec(sentiment):
    # dictionary containing genres from IMDb
    options = {
        'anger': ['Action','Thriller','Adventure'],
        'fear': ['Horror','Thriller'],
        'joy': ['Comedy','Musical','Animation',],
        'sadness': ['Romance','Comedy'],
        'analytical': ['Biography','Sci-Fi','Fantasy','Documentary'],
        'confident': ['Drama','Mystery'],
        'tentative': ['Family','Romance'],
    }
    # selects a genre at random from list
    short_list = options.get(sentiment)
    int = random.randint(0,len(short_list)-1)
    return short_list[int]

if __name__ == '__main__':
    # print(genre_rec('anger'))
    print(movie_rec('Comedy'))