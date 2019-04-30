'''
this program is designed by Code-ex
instabot V.1.2
you will need a ram of 4gb and enough processor to run this program 
this program will create mass instagram accaounts for you just start and watch 

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import random



cont_running = True

while cont_running ==True: #while loop keeps repeating process
driver = webdriver.Chrome('chromedriver_win32')
driver.get(' https://www.instagram.com') #url
driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + "n")
driver.get(' https://www.instagram.com')
element=driver.find_element_by_css_selector("body")
element.send_keys(Keys.CONTROL+'t')
read=open('logins.txt', 'a')



email = ' instaaccountscreator'
fullname = ' Axe daniel screwel'
username='massaccounts'	# type your username
value = random.randint(10, 100000290)
password= 'noviceprogrammer' #type your password
read.write(username + password)
read.close()
inputElement = driver.find_element_by_name('emailOrPhone').send_keys(email, + value, "@gmail.com")
time.sleep(3)
inputElement = driver.find_element_by_name('fullName').send_keys(fullname)
time.sleep(3)
inputElement= driver.find_element_by_name('username' ) .send_keys(username, + value) #dont worry about this what ever you put as username above will be executed here
time.sleep(3)
inputElement= driver.find_element_by_name('password').send_keys(password) #the same as password
time.sleep(4)
driver.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[1]/div/form/div[7]/div/button').click() # this is the login field path
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click() #to enter profile
