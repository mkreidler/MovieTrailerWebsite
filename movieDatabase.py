
import media
import fresh_tomatoes

# The following is the list of movies and their accompanying information,
# see media.py for the types of information and order about each movie listed
theGrandBudapestHotel = media.Movie(
    "Grand Budapest Hotel",
    "The adventures of Gustave H, a legendary concierge and Zero Moustafa,"
    " the lobby boy who becomes his most trusted friend.",
    "Bill Murray, Jason Schwartzman, Adrien Brody, Tilda Swinton,"
    "Edward Norton, Willem Dafoe",
    "http://ia.media-imdb.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
    "https://vimeo.com/119754714")

moonriseKingdom = media.Movie(
    "Moonrise Kingdom",
    "A pair of young lovers flee their New England town, which causes"
    " a local search party to fan out to find them.",
    "Edward Norton, Bill Murray, Tilda Swinton, Jason Schwartzman",
    "http://ia.media-imdb.com/images/M/MV5BMTEwMTc3NDkzOTJeQTJeQWpwZ15BbWU3MDI4NTAwNzc@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=7N8wkVA4_8s",
    "https://vimeo.com/77749860")

fantasticMrFox = media.Movie(
    "Fantastic Mr. Fox",
    "An urbane fox cannot resist returning to his farm raiding ways and"
    " then must help his community survive the farmers' retaliation.",
    "Jason Schwartzman, Bill Murray, Owen Wilson, Willem Dafoe",
    "http://ia.media-imdb.com/images/M/MV5BMTcwODE2NTI3Nl5BMl5BanBnXkFtZTcwMjUwOTY5Mg@@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=n2igjYFojUo",
    "https://vimeo.com/77745711")

theDarjeelingLimited = media.Movie(
    "The Darjeeling Limited",
    "A year after their father's funeral, three brothers travel across"
    " India in an attempt to bond with each other.",
    "Owen Wilson, Adrien Brody, Jason Schwartzman, Bill Murray,"
    " Anjelica Huston",
    "http://ia.media-imdb.com/images/M/MV5BMTM0MTQ4MTgwOF5BMl5BanBnXkFtZTcwMDA3MDU1MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=aO1bYukdvLI",
    "https://vimeo.com/77556248")

theLifeAquatic = media.Movie(
    "The Life Aquatic",
    "Oceanographer Steve Zissou rallies a crew including a journalist"
    " and a man who may or may not be his son.",
    "Bill Murray, Owen Wilson, Anjelica Huston, Willem Dafoe",
    "http://ia.media-imdb.com/images/M/MV5BMTYzODYzNzg2MF5BMl5BanBnXkFtZTcwMTkzOTQzMw@@._V1_SY317_CR1,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=yh401Rmkq0o",
    "https://vimeo.com/77368356")

theRoyalTenenbaums = media.Movie(
    "The Royal Tenenbaums",
    "An estranged family of former child prodigies reunites when their"
    " father announces he is terminally ill.",
    "Anjelica Huston, Luke Wilson, Owen Wilson, Bill Murray",
    "http://ia.media-imdb.com/images/M/MV5BMjA0MjcwNDgzNl5BMl5BanBnXkFtZTgwNzMwODQxMTE@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=EJBqsVFx84M",
    "https://vimeo.com/77194778")

rushmore = media.Movie(
    "Rushmore",
    "The extracurricular king of Rushmore preparatory school is put on"
    " academic probation.",
    "Jason Schwartzman, Bill Murray, Luke Wilson",
    "http://ia.media-imdb.com/images/M/MV5BMjE2OTc3OTk2M15BMl5BanBnXkFtZTgwMjg2NjIyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=GxCNDpvGyss",
    "https://vimeo.com/77015707")

bottleRocket = media.Movie(
    "Bottle Rocket",
    "Focusing on a trio of friends and their elaborate plan to pull"
    " off a simple robbery and go on the run.",
    "Luke Wilson, Owen Wilson",
    "http://ia.media-imdb.com/images/M/MV5BMTI2NDY4Mzc1Nl5BMl5BanBnXkFtZTcwNzUyNDk5MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=hspUSez-rYY",
    "https://vimeo.com/76874277")

# Runs fresh_tomatoes.py, which generates the webpage
movies = [
    theGrandBudapestHotel,
    moonriseKingdom,
    fantasticMrFox,
    theDarjeelingLimited,
    theLifeAquatic,
    theRoyalTenenbaums,
    rushmore,
    bottleRocket
    ]
fresh_tomatoes.open_movies_page(movies)
