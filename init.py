from sites import imdb, tmdb
import os
from urllib.request import urlretrieve

#delete all images in the images folder
def deletar(path):
    dir = os.listdir(path)
    for file in dir:
        os.remove(str(path)+str(file))

#save images
def save_images(images, number):
    for link in images:
        if link:
            number += 1
            urlretrieve(link, "images/" + str(number) + ".jpg")


#number to start renaming images
number = 0

print('Example IMDB link: https://www.imdb.com/title/tt2741602/episodes?season=1&ref_=tt_eps_sn_1')
print('Example TMDB link: https://www.themoviedb.org/tv/46952-the-blacklist/season/1')
print('')

linkManual = str(input("TMDB or IMDB link in the right season: "))


if "themoviedb.org" in linkManual:
    print("\nLink from tmdb")
    deletar('images/')
    print('Processing...')
    images = tmdb(linkManual)

elif "imdb.com" in linkManual:
    print("\nLink from imdb")
    deletar('images/')
    print('Processing...')
    images = imdb(linkManual)

else:
    print('invalid link')

save_images(images, number)

print('''
Work Finished!

Subscribe in my youtube channel :)
https://www.youtube.com/channel/UCL36QmtY94U4N98QpGwYtzw
''')