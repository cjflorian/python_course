current_movies = {'the grinch': '11:00 am',
                 'Rudolph': '1:00 pm',
                 'Frosty the snowman': '3:00 pm',
                 'Chrismtas vacatios': '5:00 pm'}

print('where showin the followin movies:')
for key in current_movies:
    print(key)

movie = input('what the movie would yo line th showtime for?')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)
