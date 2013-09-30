# import os 
# root_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
# print os.path.realpath(__file__)
# print os.path.dirname(os.path.realpath(__file__))
# print os.path.split(os.path.dirname(os.path.realpath(__file__)))
# print root_dir
# print os.getcwd()

timestamp = 1372759811

import time
print time.strftime('%Y-%m-%d %X', time.localtime(timestamp))
print time.localtime(timestamp)
print "============================"

print "time to timestamp"

import datetime
dateC = datetime.datetime.now() 
timestamp = time.mktime(dateC.timetuple())
print "python timestamp:", timestamp