import urllib.request
import random


def download_web_image(url):
    image_name = random.randrange(1,1000)
    file_name = str(image_name) + ".jpg"
    urllib.request.urlretrieve(url, file_name)

download_web_image("http://www.gstatic.com/tv/thumb/tvbanners/184483/p184483_b_v7_ak.jpg")