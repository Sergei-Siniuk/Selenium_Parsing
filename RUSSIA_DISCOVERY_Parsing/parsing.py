from selenium.webdriver.common.by import By


def titles(response):
    title = response.find_element(By.CLASS_NAME, "tourList__title") \
            .find_element(By.TAG_NAME, "a").get_attribute("href")
    return title


def text(response):
    text = response.find_element(By.CLASS_NAME, "tourList__title") \
            .find_element(By.TAG_NAME, "a").text
    return text


def prices(response):
    price = response.find_element(By.CLASS_NAME, "tourList__footer")\
        .find_element(By.CLASS_NAME, "tourList__price")\
        .find_element(By.CLASS_NAME, "selection").text

    return f"{price} - руб"