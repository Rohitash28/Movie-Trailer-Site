"""Stores the details of  six movies and organizes them on the website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, which include the movies title, storyline,
    poster image link, link to the trailer and the movies theatrical release date."""
    future  = media.Movie("Back to the Future",
                          "Marty McFly is accidentally sent 30 years into the past in a time-traveling DeLorean.",
                          "http://www.coverwhiz.com/content/Back-To-The-Future.jpg",
                          "https://www.youtube.com/watch?v=qvsgGtivCgs",
                          "July 3rd, 1985")

    avengers = media.Movie("Avengers",
                          "Earth's mightiest heroes must come together and learn to fight as a team.",
                          "https://images-na.ssl-images-amazon.com/images/I/61bINjWK62L.jpg",
                          "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                          "May 4th, 2012")

    johnwick = media.Movie("John Wick",
                           "An ex-hitman comes out of retirement to track down the gangsters that took everything from him.",
                           "https://s-media-cache-ak0.pinimg.com/originals/a1/d0/69/a1d069c9c4461577a6e93d792cc123ba.jpg", # noqa
                           "https://www.youtube.com/watch?v=2AUmvWm5ZDQ",
                           "October 24, 2014")

    deadpool = media.Movie("Deadpool",
                         "A fast-talking mercenary subjected to a rogue experiment on a quest for revenge.",
                         "http://www.impawards.com/2016/posters/deadpool_ver9_xxlg.jpg",
                         "https://www.youtube.com/watch?v=ONHBaC-pfsk",
                         "Feb 12th, 2016")

    wintersol = media.Movie("Captain America: The Winter Soldier",
                           "Steve Rogers teams up with Black Widow to battle an assassin known as the Winter Soldier.",
                           "http://www.impawards.com/2014/posters/captain_america_the_winter_soldier_ver8.jpg",
                           "https://www.youtube.com/watch?v=tbayiPxkUMM",
                           "April 4th, 2014")

    Logan = media.Movie("Logan",
                          "Logan's attempts to hide from the world but when a young mutant arrived they are pursued by dark forces.",
                          "http://www.impawards.com/2017/posters/logan.jpg",
                          "https://www.youtube.com/watch?v=Div0iP65aZo",
                          "March 3rd, 2017")

    # Store the Movie objects in a list.
    movies = [future, avengers, johnwick, deadpool, wintersol, Logan]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()

