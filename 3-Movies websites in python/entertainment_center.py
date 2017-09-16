#objects

import fresh_tomatoes
import media

#------------------First object = toy_story-------------------
toy_story = media.Movie("Toy story",
                         "A story of a boy and his toys that come to life",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                         )

#print (toy_story.storyline)

#try this:
#print (toy_story.poster_image_url)

#------------------Second object = avatar-------------------

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=vGNGGBzaNQ0",
                    )

#print (avatar.storyline)    #A marine on an alien planet
#avatar.show_trailer()


#------------------Third object = the martian-------------------

the_martian = media.Movie("The Martian",
                     "When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=ej3ioOneTy8",
                    )

#print (the_martian.storyline)    
#the_martian.show_trailer()

#------------------Fourth object = The Dark Knight------------------

dark_knight = media.Movie("The Dark Knight",
                     "With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                    )

#print (dark_knight.storyline)    
#dark_knight.show_trailer()

#------------------Fifth object = The Revenant-------------------

the_revenant = media.Movie("The Revenant",
                     "While exploring the uncharted wilderness in 1823, frontiersman Hugh Glass (Leonardo DiCaprio) sustains life-threatening injuries from a brutal bear attack.",
                     "https://i.ytimg.com/vi/NyRD_8HKRMY/movieposter.jpg",
                     "https://www.youtube.com/watch?v=LoebZZ8K5N0",
                    )

#print (the_revenant.storyline)    
#the_revenant.show_trailer()

#------------------Sixth object = Noah------------------

noah = media.Movie("Noah",
                     "When God decides that mankind has become too sinful and must be wiped off the Earth, he chooses Noah (Russell Crowe), a pious man, for a great task",
                     "https://resizing.flixster.com/LeXK5nzGZHhU3EAyceBmNJlIi_Q=/206x305/v1.bTsxMTE3OTU4MjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",
                     "https://www.youtube.com/watch?v=_OSaJE2rqxU",
                    )

#print (noah.storyline)   
#noah.show_trailer()

#-----------------------------------------------------

movies = [toy_story, avatar, the_martian, dark_knight ,the_revenant,noah ]
fresh_tomatoes.open_movies_page(movies)

#to access variable
#print(media.Movie.valid_ratings)
#print(media.Movie.VALID_RATINGS)

#to access doc variable
print(media.Movie.__doc__)


