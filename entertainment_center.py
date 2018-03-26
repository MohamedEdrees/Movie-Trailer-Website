import fresh_tomatoes
import media

mr_robot = media.Movie("MR.ROBOT",  # title
                       # poster url
                       "https://goo.gl/e4DEto",
                       # youtube trailer url
                       "https://www.youtube.com/watch?v=xIBiJ_SzJTA")

despicable_me = media.Movie("Despicable Me",
                            "https://goo.gl/fuKMCn",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

interstellar = media.Movie("Interstellar",
                           "https://goo.gl/Eog8K7",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

limitless = media.Movie("Limitless",
                        "https://goo.gl/YDA3UQ",
                        "https://www.youtube.com/watch?v=jOLqNOfzus4")

now_you_see_me = media.Movie("Now You See Me",
                             "https://goo.gl/4cDmDj",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

the_croods = media.Movie("The Croods",
                         "https://goo.gl/wy9jnN",
                         "https://www.youtube.com/watch?v=4fVCKy69zUY")
# List Of Films.
movies = [mr_robot,
          interstellar,
          limitless,
          now_you_see_me,
          the_croods,
          despicable_me]
# Create Dynamic Web page with the inputs films.
fresh_tomatoes.open_movies_page(movies)
print ("The Web Page Generated, The Website Will Open NOW!")
