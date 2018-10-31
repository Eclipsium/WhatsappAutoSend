# Created by Eclipsum - 31.10.2018 17:09
# PyCharm
# -*- coding: UTF-8 -*-

import schedule
import time


try:
    import local_settings as s

except(ImportError):
    import settings as s

print('\nStart schedule... \n')

while True:
    schedule.run_pending()
    time.sleep(1)


