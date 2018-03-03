import media

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life", 
						"https://pt.wikipedia.org/wiki/Toy_Story#/media/File:Movie_poster_toy_story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print(avatar.storyline)

avatar.show_trailer()