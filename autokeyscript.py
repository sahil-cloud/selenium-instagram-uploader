# !~~~ATTENTION~~~!
# This file should be added to the scripts of autokey.
# It can be done by using Autokey main window.
# Save this script as image_select
# This automation is suited for spacefm where ctrl-l activates the address bar and then searches image_name in that directory 
# change according to your file manager

import time

image_path = '/path/to/your/image/folder/'
image_name = '/image/name/no/need/to/file/extension'

keyboard.send_keys('<ctrl>+l')
keyboard.send_keys(image_path)

keyboard.send_keys('<enter>')
time.sleep(3)

#keyboard.send_keys('<ctrl>+f')
keyboard.send_keys(image_name)
keyboard.send_keys('<enter>')

 # search for the person to like the posts
 search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
# # the person you want to search
search.send_keys('barkhasingh0308')
sleep(2)
find = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
 search.send_keys(Keys.RETURN)
 find.click()
sleep(3)

 driver.execute_script("window.scrollTo(0, 600)")
 sleep(3)

# # steps to like all posts
post = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
 post.click()
 sleep(5)

# # we do 1st time by manually then in the loop
like1 = driver.find_element_by_xpath(
'/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like1.click()
 sleep(3)
 nextpic1 = driver.find_element_by_xpath(
    '/html/body/div[4]/div[1]/div/div/a')
 nextpic1.click()
 sleep(4)

while True:
   like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
   like.click()
   sleep(3)
   nextpic = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
   nextpic.click()
   sleep(4)

#  for liking all the posts  }}


# for sending message to someone
inbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
inbox.click()
sleep(5)

send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
send.click()
sleep(3)

# write the username of the person you want to send msg
ip = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
# enter the person you want to send msg
ip.send_keys('') 
sleep(3)

person = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div/div')
# print(person)
person.click()

submit = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div')
submit.click()
sleep(5)

text = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
text.send_keys('Aur kya krra hai')
text.send_keys(Keys.RETURN)
