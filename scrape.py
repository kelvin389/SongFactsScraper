from selenium import webdriver
from selenium.webdriver.common.by import By

data_to_get = [
    ("numbers", "https://www.songfacts.com/category/songs-with-numbers-in-the-title"),
    ("sfx", "https://www.songfacts.com/category/songs-containing-sound-effects"),
    ("for_other", "https://www.songfacts.com/category/songs-that-were-written-for-other-artists"),
    ("banjo", "https://www.songfacts.com/category/songs-featuring-a-banjo"),
]

# tuple(str: data_name, list: list of data entires)
data = []

driver = webdriver.Firefox()
for data_name, data_link in data_to_get:
    this_data = []

    driver.get(data_link)
    elements = driver.find_elements(By.XPATH, "//ul[contains(@class, 'browse-list-purple space-bot')]/li")
    if not elements:
        print("captcha detected. exiting")
        driver.close()
        exit(1)
    for e in elements:
        if e.text:
            this_data.append(e.text)

    data.append((data_name, this_data))

driver.close()

print(data)
