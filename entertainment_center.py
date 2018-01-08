import fresh_tomatoes
import media

the_holy_grail = media.Movie(
    "Monty Python and The Holy Grail",
    "1975",
    "932 AD, King Arthur travel throughout Britain searching men to"
    " join the Knights of the Round Table. To find the Holy Grail.",
    "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",  # NOQA
    "https://youtu.be/urRkGvhXc8w")

and_now_for_something_completely_different = media.Movie(
    "And Now for Something Completely Different",
    "1971",
    "And Now for Something Completely Different is a 1971 British sketch"
    " comedy film based on the television comedy series Monty Python's Flying"
    " Circus featuring sketches from the first two series."",
    "https://upload.wikimedia.org/wikipedia/en/e/ee/ANFSCD_poster.jpg",
    "https://youtu.be/IDtepG8EvHE")

life_of_brian = media.Movie("Monty Python's Life of Brian",
    "1979",
    "Brian Cohen was born in a stable next door to the one Jesus was born,"
    "Brian grows up an idealistic young man who resents the Roman occupation.",
    "https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg",
    "https://youtu.be/TKPmGjVFbrY")

live_at_the_hollywood_bowl = media.Movie(
    "Monty Python Live at the Hollywood Bowl",
    "1982",
    "Monty Python Live at the Hollywood Bowl is a 1982 British concert"
    " comedy film starring the Monty Python comedy troupe.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/MontyPythonHollywoodBowlPoster.jpg",  # NOQA
    "https://youtu.be/3Fg3-Ma-HA8")

the_meaning_of_life = media.Movie(
    "Monty Python's The Meaning of Life",
    "1983",
    "A group of fish in a posh restaurant's tank swim together casually, "
    "until they look at the customers outside of the tank and see their friend"
    " Howard being eaten. This leads them to question the meaning of life.",
    "https://upload.wikimedia.org/wikipedia/en/9/91/Meaningoflife.jpg",
    "https://youtu.be/LH8aTeouR4Y")

live_mostly = media.Movie(
    "Monty Python Live (Mostly)",
    "2014",
    "In 2013, the Pythons lost a legal case to the producer of Holy Grail."
    "To pay these, a reunion show was proposed.",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Monty_Python_Live_%28Mostly%29.jpg/440px-Monty_Python_Live_%28Mostly%29.jpg",  # NOQA
    "https://youtu.be/yBcYuwlWFRM")

movies = [
    the_holy_grail, and_now_for_something_completely_different, life_of_brian,
    live_at_the_hollywood_bowl, the_meaning_of_life, live_mostly]

fresh_tomatoes.open_movies_page(movies)
