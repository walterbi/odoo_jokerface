#!/usr/bin/python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import os, time, sys
from datetime import datetime


def SeriesClone():

    driver.get('http://jokerface.vn/collections/all')
    main_block = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'filter-wrapper'))
    )
    print str(datetime.now()) + ' finding main block of category.'

    a_elms = main_block.find_elements_by_tag_name('a')
    print str(datetime.now()) + ' all tag a found.'

    for a_elm in a_elms:
        print a_elm.get_attribute('innerHTML').split('(')[0][:-1]


def CatClone():


if __name__ == '__main__':

    driver = webdriver.Chrome()

    # SeriesClone()

    os.system('pkill chromedriver')