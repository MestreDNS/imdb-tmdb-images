from bs4 import BeautifulSoup
from urllib.request import urlopen
import request


def tmdb(linkManual):
    html_page = urlopen(linkManual)
    soup = BeautifulSoup(html_page.read(), "html5lib")
    only_images = []
    for img in soup.findAll('img'):
        only_images.append(img.get('data-src'))
    return only_images


def imdb(linkManual):
    html_page = request.get(linkManual)
    soup = BeautifulSoup(html_page.text, "html.parser")
    images = []
    only_images = []
    for img in soup.findAll(class_='zero-z-index'):
        images.append(img.get('src'))

    for img in images:
        if 'None' not in str(img):
            only_images.append(img)

    return only_images
