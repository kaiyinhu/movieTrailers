from media import Movie
import fresh_tomatoes
passenger = Movie("Passenger", "https://s.yimg.com/uu/api/res/1.2/PYj0LDFHcRQtbHguMfzDYg--/aD03MjA7dz0xMjgwO3NtPTE7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-us/video/video.clevvernews.alloy.com/61c1b3d2377a317e84d0dffddee3fe0e", "https://www.youtube.com/watch?v=7BWWWQzTpNU")
inception = Movie("Inception", "https://upload.wikimedia.org/wikipedia/en/1/18/Inception_OST.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
independence_day = Movie("Independence Day", "http://cdn.traileraddict.com/content/ff/independenceday-poster.jpg", "https://www.youtube.com/watch?v=O3a0kv1sJxg")
interstellar = Movie("Interstellar", "https://bfox.files.wordpress.com/2014/11/interstellar-movie.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw")
mib = Movie("Men in Black", "http://aetherforce.com/wp-content/uploads/2015/01/Men-in-Black-Theme-Song-5.jpg", "https://www.youtube.com/watch?v=HYUd7AOw_lk")
theMatrix = Movie("The Matrix", "https://upload.wikimedia.org/wikipedia/en/9/9a/The_Matrix_soundtrack_cover.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8")

movie = [passenger, inception, independence_day, interstellar, mib, theMatrix]

fresh_tomatoes.open_movies_page(movie)
