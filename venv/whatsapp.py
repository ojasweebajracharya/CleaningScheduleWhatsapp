from selenium import webdriver
from itertools import cycle
import time


numbers = ["1","2","3","4","5","6"]

pool = cycle(numbers)

roomnum = next(pool)
print(roomnum)

driver = webdriver.Chrome(r'C:\Users\ojasw\PycharmProjects\WhatsappCleaning\chromedriver_win32\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

time.sleep(8)
username = 'testing'
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(username))
user.click()



msg = f"Helloooo :)) Just a reminder that Room {roomnum} is in charge of trash/kitchen cleaning this week."

msg_box = driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@data-tab="6"]')
msg_box.send_keys(msg)
button = driver.find_element_by_xpath('//button[@class="_2Ujuu"]')
button.click()

# selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
# selected_contact.click()
# inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
# input_box = driver.find_element_by_xpath(inp_xpath)
#
# input_box.send_keys(text + Keys.ENTER)
#
# driver.quit()