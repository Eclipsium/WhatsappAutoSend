# Created by Eclipsum - 31.10.2018 13:27
# PyCharm
# -*- coding: UTF-8 -*-

from main import job
import schedule


send_to = ['some user', 'some user2'] #group or user. Selection by innerHtml
msg = 'Test message' #send current msg
save_session = True #if you wanna save and load session, else = False
time_to_sleep = 20 #Wait to load page(sec)



'''Schedule for send at this time'''

schedule.every(4).days.at("9:00").do(job)
schedule.every(4).days.at("13:00").do(job)
schedule.every(4).days.at("19:00").do(job)

