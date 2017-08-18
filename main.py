from getpass import getpass
from subprocess import call
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
password = getpass("Password: ")
email = "zconnelly13@gmail.com"
memrise_url = "https://www.memrise.com/course/1588576/random/edit/database/2577054/?page=%s"  # noqa
dir_path = os.path.dirname(os.path.realpath(__file__))

# Login and Get to the Project Page
driver = webdriver.Chrome()
driver.get("https://www.memrise.com/course/1559979/harry-potter-und-das-verwunschene-kind/edit/#l_5884845")  # noqa
elem = driver.find_element_by_css_selector('a[href="/login/"]')
elem.click()
elem = driver.find_element_by_css_selector('a[href="/join/google-oauth2/"]')  # noqa
elem.click()
elem = driver.find_element_by_css_selector('input[type="email"]')
elem.send_keys(email)
elem.send_keys(Keys.RETURN)
time.sleep(5)
elem = driver.find_element_by_css_selector('input[type="password"]')
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(5)


for page in range(1, 4):
    driver.get(memrise_url % str(page))  # noqa
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
        file_path = '%s/audio/%s.mp4' % (dir_path, str(i))  # noqa
        file_input.send_keys(file_path)
        i = i + 1
    time.sleep(5)
