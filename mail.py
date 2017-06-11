from selenium import webdriver
import time
email=input("Enter Email ID : ")
word=input("Enter password : ")
rec=input("Enter recepient Email ID : ")
sub=input("Enter the Subject : ")
msg=input("Enter the Message : ")
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True

driver = webdriver.Firefox(capabilities=caps)

webpage = "https://mail.google.com/mail/u/0/#inbox?compose=new" # edit me

driver.get(webpage)

lbox1=driver.find_element_by_class_name("RCum0c")
lbox1.send_keys(email)

submit1 = driver.find_element_by_id("identifierNext")
submit1.click()


time.sleep(5)

submit1 = driver.find_element_by_id("passwordNext")
submit1.click()

lbox2=driver.find_element_by_class_name("RCum0c")
lbox2.send_keys(word)

time.sleep(5)


submit1 = driver.find_element_by_id("passwordNext")
submit1.click()

time.sleep(5)

submit2 = driver.find_element_by_class_name("z0")
submit2.click()

time.sleep(10)

sbox = driver.find_element_by_class_name("vO")
sbox.send_keys(rec)

sbox2 = driver.find_element_by_class_name("aoT")
sbox2.send_keys(sub)

sbox1 = driver.find_element_by_id(":n8")
sbox1.send_keys(msg)

submit = driver.find_element_by_id(":jo")
submit.click()
