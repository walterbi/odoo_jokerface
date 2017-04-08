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

    driver.get('http://jokerface.vn/collections/all')

    main_block = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'main_menu'))
    )
    print str(datetime.now()) + ' main block found.'

    main_menu = main_block.find_elements_by_tag_name('a')
    print str(datetime.now()) + ' tag a found.'
    for elm_main_menu in main_menu:
        try:
            attr_title = elm_main_menu.get_attribute('title')
            print attr_title
        except NoSuchAttributeException:
            print '---' + elm_main_menu.get_attribute('innerHTML')


def SubCatClone():

    driver.get('http://jokerface.vn/collections/all')

    main_block = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'main_menu'))
    )
    print str(datetime.now()) + ' main block found.'

    main_class = main_block.find_elements_by_class_name('sub_menu')
    print str(datetime.now()) + ' sub menu found.'
    for elm_main_class in main_class:
        elm_a = elm_main_class.find_elements_by_tag_name('a')
        for elm in elm_a:
            print elm.get_attribute('innerHTML')


if __name__ == '__main__':

    driver = webdriver.Chrome()

    SeriesClone()
    # CatClone()
    # SubCatClone()

    os.system('pkill chromedriver')
