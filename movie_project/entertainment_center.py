import media
import fresh_tomatoes

# This feeds into media.py the movie's information
fast_and_furious = media.Movie("The Fast and the Furious",
                               "A story about illegal street racing",
                               "https://i.sharefa.st/8TFpgq0Pnv10.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=ZsJz2TJAPjw")  # NOQA

# how to run just the storyline or trailer.
# print (fast_and_furious.storyline)
# fast_and_furious.show_trailer()
minions = media.Movie("Minions",
                      "A movie about evil helpers "
                      "trying to take over the world",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=Wfql_DoHRKc")  # NOQA
# print(minions.storyline)
# minions.show_trailer()

mulan = media.Movie("Mulan",
                    "A movie about a girl trying to save "
                    "her father and China.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Movie_poster_mulan.JPG/220px-Movie_poster_mulan.JPG",  # NOQA
                    "https://www.youtube.com/watch?v=wAbGAkkOgcM")  # NOQA
# print(mulan.storyline)
# mulan.show_trailer()

lilo_and_stitch = media.Movie("Lilo and Stitch",
                              "A movie about aliens creations "
                              "and the meaning of family in Hawaii",
                              "http://www.gstatic.com/tv/thumb/movieposters/29095/p29095_p_v8_aa.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=hu9bERy7XGY")  # NOQA
# print(lilo_and_stitch.storyline)
# lilo_and_stitch.show_trailer()
nerve = media.Movie("Nerve",
                    "A movie about a deathly game of truth and dare",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUzOTg1OTM4NV5BMl5BanBnXkFtZTgwMTg2Mjg0OTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Tyk2_bzca3E")  # NOQA
# print(nerve.storyline)
# nerve.show_trailer()

a_walk_to_remember = media.Movie("A Walk to Remember",
                                 "A lovestory about a dying girl "
                                 "befriending a bully",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/d/dc/A_Walk_to_Remember_Poster.jpg/220px-A_Walk_to_Remember_Poster.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=EgdoQ8Oxu2E")  # NOQA
# print(a_walk_to_remember)
# a_walk_to_remember.show_trailer()

movies = [fast_and_furious, minions, mulan,
          lilo_and_stitch, nerve, a_walk_to_remember]
fresh_tomatoes.open_movies_page(movies)
