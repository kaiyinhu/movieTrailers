from media import Movie
import fresh_tomatoes

"""Those are the movie selections as instances of the Movie() class 
    """
passenger = Movie("Passenger", "https://goo.gl/KQ5QG0", 
	        "https://goo.gl/a8NAHV")
inception = Movie("Inception", "https://goo.gl/Moh3D8", 
	        "https://goo.gl/FQUlCQ")
independence_day = Movie("Independence Day", "https://goo.gl/X5lQoj", 
	        "https://goo.gl/nqrI1G")
interstellar = Movie("Interstellar", "https://goo.gl/DXIJ6j", 
	        "https://goo.gl/DBF7Jj")
mib = Movie("Men in Black", "https://goo.gl/Q5B76J", 
	        "https://goo.gl/N9wRG2")
theMatrix = Movie("The Matrix", "https://goo.gl/wheVzX", 
	        "https://goo.gl/aD1JtT")

# Movie list that contains all movie instances
movie = [passenger, inception, independence_day, interstellar, mib, theMatrix]

# Function to generate html file as output
fresh_tomatoes.open_movies_page(movie)
