from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget
# disable notifications
options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
browser = webdriver.Firefox(firefox_options=options)

#open the webpage
browser.get("http://www.facebook.com")

#target username and password
username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pass")))

#enter username and password
username.clear()
username.send_keys("lordxfive20@gmail.com")
password.clear()
password.send_keys("Fear26726400")

#target the login button and click it
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "login"))).click()

#We are logged in!

#wait 5 seconds to allow your new page to load
time.sleep(5)
images = [] 

browser.get("https://www.facebook.com/media/set/?set=a.111292253939688&type=3")
time.sleep(5)
    
#scroll down
#increase the range to sroll more
#example: range(0,10) scrolls down 650+ images
for j in range(0,1):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

#target all the link elements on the page
    anchors = browser.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    #narrow down all links to image links only
    anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
    print('Found ' + str(len(anchors)) + ' links to images')

#extract the [1]st image element in each link
    for a in anchors:
        browser.get(a) #navigate to link
        time.sleep(5) #wait a bit
        img = browser.find_elements_by_tag_name("img")
        images.append(img[0].get_attribute("src"))

print('I scraped '+ str(len(images)) + ' images!')
print("-----------------------------------------")
print(images)

#create directory
path = os.getcwd()
path = os.path.join(path, "FB_SCRAPED")

#create the directory
os.mkdir(path)

#download images
counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

print("\n successfuly finihsed !")