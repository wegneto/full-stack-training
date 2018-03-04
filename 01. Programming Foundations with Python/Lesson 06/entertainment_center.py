import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life", 
						"https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

gladiator = media.Movie("Gladiator",
						"Maximus rises through the ranks of the gladiatorial arena to avenge the murders of his family and his emperor.",
						"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
						"https://www.youtube.com/watch?v=owK1qxDselE")

first_blood = media.Movie("First Blood",
						"A Vietnam War veteran uses all his training and aggression on the battlefield when he is arrested and tortured by police officers.",
						"https://upload.wikimedia.org/wikipedia/en/d/d6/First_blood_poster.jpg",
						"https://www.youtube.com/watch?v=pD3mC-182L8")

conan = media.Movie("Conan The Barbarian",
						"The story of a young barbarian who seeks vengeance for the death of his parents.",
						"https://upload.wikimedia.org/wikipedia/en/8/81/Conan_the_Barbarian_by_Renato_Casaro.jpg",
						"https://www.youtube.com/watch?v=xwdYd_RdLCQ")

dark_knight = media.Movie("The Dark Knight",
						"Batman faces the Joker.",
						"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

movies = [toy_story, avatar, gladiator, first_blood, conan, dark_knight]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)