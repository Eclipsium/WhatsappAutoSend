# Created by Eclipsum - 31.10.2018 13:34
# PyCharm
# -*- coding: UTF-8 -*-

from selenium.webdriver.common.keys import Keys
import pickle
import localstorage
import time
from selenium import webdriver
from datetime import datetime


try:
    import local_settings as s

except(ImportError):
    import settings as s


def job():

    # Start ChtomeWebDriver
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    # open local storage
    storage = localstorage.LocalStorage(driver)

    # Autorizate
    if s.save_session:
        try:
            local_dump = pickle.load(open("local.pkl", "rb"))
            for key, value in local_dump.items():
                storage.set(key, value)
            print('\nLocalStorage is loaded!\nIf your session isn`t restore - delete local.pkl and restart script again\n')
            driver.refresh()

        except(FileNotFoundError):
            input('Can`t load local.pkl file. Please, scan QR code and press ENTER\n')
            local_dump = storage.items()
            pickle.dump(local_dump, open("local.pkl", "wb"))
            print('Save session!\n')

    else:
        input('Saved session is Disable. You can enable this in settings.py\n'
              'Scan QR code and press ENTER\n')

    # wait to load site
    time.sleep(s.time_to_sleep)

    for user in s.send_to:
        send_to_user = driver.find_elements_by_xpath('//span[@title = "{}"]'.format(user))
        send_to_user[0].click()
        msg_box = driver.find_elements_by_class_name('copyable-text')
        msg_box[-1].click()
        msg_box[-1].send_keys(s.msg, Keys.ENTER)

    print(' Message send!\n',datetime.now())
    driver.close()

