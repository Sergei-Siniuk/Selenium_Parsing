from settings import *
from parsing import *
import time



for page in range(1, 3):
    url = f"https://www.russiadiscovery.ru/tours/trekkingi/?page={page}"
    driver.get(url)
    block = driver.find_element(By.CLASS_NAME, "tourListUl")
    posts = block.find_elements(By.TAG_NAME, "li")
    print(type(block))

    for post in posts:
        title = titles(post)
        txt = text(post)
        price = prices(post)
        print(title, text, price, sep="\n")

time.sleep(20)
