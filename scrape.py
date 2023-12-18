from selenium import webdriver
from selenium.webdriver.common.by import By

data_to_get = [
    ("numbers", "https://www.songfacts.com/category/songs-with-numbers-in-the-title"),
    ("sfx", "https://www.songfacts.com/category/songs-containing-sound-effects"),
    ("for_other", "https://www.songfacts.com/category/songs-that-were-written-for-other-artists"),
    ("banjo", "https://www.songfacts.com/category/songs-featuring-a-banjo"),
]

# key: data_name, data: list of data entries
data = {}

driver = webdriver.Firefox()
for data_name, data_link in data_to_get:
    this_data = []

    driver.get(data_link)
    elements = driver.find_elements(By.XPATH, "//ul[contains(@class, 'browse-list-purple space-bot')]/li")
    if not elements:
        print("captcha detected. exiting. visit songfacts.com on your own browser and complete the captcha before running again.")
        driver.close()
        exit(1)
    for e in elements:
        if e.text:
            this_data.append(e.text)

    data[data_name] = this_data

driver.close()

for d in data_to_get:
    name = d[0]
    print(name)
    
    for song in data[name]:
        print("\t", song)
