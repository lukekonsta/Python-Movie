import media
import fresh_tomatoes

get_out = media.Movie("Get Out",
                      "horror movie",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ" )

#print(get_out.show_trailer())
#get_out.storyline

lista = [get_out]

#fresh_tomatoes.open_movies_page(lista)

print(get_out.valid_ratings)
print(media.Movie.valid_ratings)
print(media.Movie.__doc__)
#print(get_out.__name__)
print(get_out.__module__)
