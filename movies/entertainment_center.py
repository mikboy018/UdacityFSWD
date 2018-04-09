import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "Toys coming to life", "http://www.imdb.com/title/tt0114709/", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "See Pocahontas", "https://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

caddyshack = media.Movie("Avatar", "A story of a groundskeeper and his nemesis, the gopher", "https://www.amazon.com/Caddyshack-Chevy-Chase/dp/B003PJGD5Y", "https://www.youtube.com/watch?v=x9Nl39uWEYk")

toy_story_b = media.Movie("Toy Story", "Toys coming to life", "http://www.imdb.com/title/tt0114709/", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar_b = media.Movie("Avatar", "See Pocahontas", "https://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

caddyshack_b = media.Movie("Avatar", "A story of a groundskeeper and his nemesis, the gopher", "https://www.amazon.com/Caddyshack-Chevy-Chase/dp/B003PJGD5Y", "https://www.youtube.com/watch?v=x9Nl39uWEYk")


#caddyshack.show_trailer()

#print(caddyshack.storyline)

movies = [toy_story, avatar, caddyshack, toy_story_b, avatar_b, caddyshack_b]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)

print(media.Movie.__name__)

print (media.Movie.__module__)
