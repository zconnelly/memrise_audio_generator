from getpass import getpass
from subprocess import call
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Login and Get to the Project Page
password = getpass("Password: ")
driver = webdriver.Chrome()
driver.get("https://www.memrise.com/course/1559979/harry-potter-und-das-verwunschene-kind/edit/#l_5884845")  # noqa
elem = driver.find_element_by_css_selector('a[href="/login/"]')
elem.click()
elem = driver.find_element_by_css_selector('a[href="/join/google-oauth2/?next=/home/"]')  # noqa
elem.click()
elem = driver.find_element_by_css_selector('input[type="email"]')
elem.send_keys("zconnelly13@gmail.com")
elem.send_keys(Keys.RETURN)
time.sleep(5)
elem = driver.find_element_by_css_selector('input[type="password"]')
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(5)


for page in range(1, 4):
    driver.get("https://www.memrise.com/course/1588576/random/edit/database/2577054/?page=%s" % str(page))  # noqa
    # driver.get("https://www.memrise.com/course/1588512/der-songtext/edit/database/2576989/?page=%s" % str(page))  # noqa
    # driver.get("https://www.memrise.com/course/1588458/kinderbucher/edit/database/2576930/?page=%s" % str(page))  # noqa
    # driver.get("https://www.memrise.com/course/1584764/erwachsen-werd-ich-vielleicht-spater/edit/database/2573062/?page=%s" % str(page))  # noqa
    # driver.get("https://www.memrise.com/course/1584719/das-tagebuch-von-edward-dem-hamster/edit/database/2573008/?page=%s" % str(page))  # noqa
    # driver.get("https://www.memrise.com/course/1559979/harry-potter-und-das-verwunschene-kind/edit/database/2547033/?page=%s" % str(page))  # noqa
    things = driver.find_elements_by_css_selector(
        'tr[class="thing"]')
    i = 0
    for thing in things:
        word = thing.find_element_by_css_selector('td[data-key="1"]').text
        call(['say -v "Anna" "%s" -o audio/%s.mp4' % (word, str(i))],
             shell=True)
        file_input = thing.find_element_by_css_selector('input[type="file"]')
        file_path = '/Users/zacmimi/personal_projects/memrise_audio_generator/audio/%s.mp4' % str(i)  # noqa
        file_input.send_keys(file_path)
        i = i + 1
    time.sleep(5)
