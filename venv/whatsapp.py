from selenium import webdriver
from itertools import cycle
import time
import os

numbers = ["1","2","3","5","6"]

changes = input("Any changes?: Y if yes ")
changedst = ""

if changes == "Y" or changes == "y":
    changedst = input("Enter room index from this list [1,2,3,5,6] : ")

if not os.path.exists('log.txt'):
    with open('log.txt','w') as f:
        f.write('1')
with open('log.txt','r') as f:
    if changedst != "":
        roomnum = changedst
    else:
        st = int(f.read())
        roomnum = st

with open('log.txt','w') as f:

    if changedst != "":
        f.write(str(int(changedst)+1))
    else:
        if st == 5:
            st = 0
        else:
            st += 1
        f.write(str(st))


def associatedRoom(st):
    room = {
        0: numbers[0],
        1: numbers[1],
        2: numbers[2],
        3: numbers[3],
        4: numbers[4],
    }
    return room.get(st, "Invalid")

if changedst == "":
    correctroomnum = associatedRoom(roomnum)
else:
    correctroomnum = associatedRoom(int(changedst))

driver = webdriver.Chrome(r'C:\Users\ojasw\PycharmProjects\WhatsappCleaning\chromedriver_win32\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

enter = input("Press enter to continue: ")
username = 'testing'
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(username))
user.click()



msg = f"Helloooo :)) Just a reminder that Room {correctroomnum} is in charge of trash/kitchen cleaning this week."

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