import requests
from bs4 import BeautifulSoup
import urllib.request


def download_img(img):
    try:
        if img.get('src') != None:
            image_url = img['src']

        elif img.get('data-src') != None:
            image_url = img['data-src']

        image_name = image_url.split('/')[-1]

        print("""
Download image ...
[%s]
        """ % image_name)

        urllib.request.urlretrieve(image_url, "./images/{}".format(image_name))

    except KeyError:
        print("""
Error download ...
[%s]
        """ % img)


def main():
    for i in range(1, 168, 48):
        response = requests.get(
            'https://listado.mercadolibre.com.co/_Desde_{}__Tienda_sony'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        # image_containers = soup.find_all(class_="image-content")
        image_containers = soup.select('.item-link img')
        for img in image_containers:
            download_img(img)


if __name__ == "__main__":
    main()
