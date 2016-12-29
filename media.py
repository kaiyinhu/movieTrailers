import webbrowser

class Movie():
  """This is the Movie() class
     which includes class init function and the playTrailer function
  """
  def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
  # Function that open url using webbrowser, if that's a video link, 
  # the video will be displayed by the browser 
  def playTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
