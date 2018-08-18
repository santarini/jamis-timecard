#import schedule
import time
import datetime
import re
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

#surfacebook and work computer webdriver path
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver.set_window_size(1900, 1900)
driver.set_window_position(0, 0)
driver.get('https://dawson8a.onelogin.com/login')

#link to iframe: https://dawson.jamisprime.com/etime/TimeCardEdit.aspx?hdFormWonder=_0Arkk6UA-Ix0

userName = driver.find_element_by_id('user_email')
userName.send_keys('dawson email')
password = driver.find_element_by_id('user_password')
password.send_keys('dawson pass')
loginButton = driver.find_element_by_id('user_submit')
loginButton.click()
time.sleep(2)
securityQ1 = driver.find_element_by_xpath("(//input[@class='security-answer'])[1]")
securityQ1.send_keys('sec q 1')
securityQ2 = driver.find_element_by_xpath("(//input[@class='security-answer'])[2]")
securityQ2.send_keys('sec q 2)
loginButton.click()
time.sleep(2)

driver.get('https://dawson8a.onelogin.com/client/apps/select/87598317')
time.sleep(1)

timeAndExp = driver.find_element_by_xpath('//*[@id="panelT_modulesBar_ul"]/li[5]/div/div')
timeAndExp.click()
time.sleep(1)

timeCard = driver.find_element_by_xpath('//*[@id="panelL_menuPanel_sp1_tree1_node_0_0"]/span')
timeCard.click()
time.sleep(2)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

#period = driver.find_element_by_id('ctlTimeCardSelector_ddlDate')
#period.click()

optionList = []

select_fr = Select(driver.find_element_by_id("ctlTimeCardSelector_ddlDate"))
for option in select_fr.options:
    optionList.append(option.text)


#####

dateList = []

today = datetime.date.today()

#we figure out which list contians dates and plug those into a list
r = re.compile("\d\d/\d\d/\d\d\d\d - \d\d/\d\d/\d\d\d\d")
newlist = list(filter(r.match, optionList))

#we figure out the index ref number for each list element and create a dictionary 
for element in newlist:
    subList = [optionList.index(element)]
    dateStr = element.split("(")[0].split("-")[0].rstrip()
    dateStart = datetime.datetime.strptime(dateStr, '%m/%d/%Y').date()
    for x in range (0, 7):
        subList.append((dateStart + datetime.timedelta(days = x)).strftime('%Y-%m-%d'))
    dateList.append(subList)

for sublist in dateList:
    if str(today) in sublist:
        correctOption = sublist[0]

#####

###select by index
select_fr.select_by_index(correctOption)

##
### select by visible text
##select_fr.select_by_visible_text('Banana')
##
### select by value 
##select_fr.select_by_value('1')
##

#option1 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[1]')
#option3 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[2]')
#option3 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[3]')
#openCard = driver.find_elements_by_xpath("//*[contains(text(), '(Open)')]")
#openCard.click()

time.sleep(3)

jobNumberDropDown = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]')
jobNumberDropDown.click()

###blank
##jobNumber1 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]/option[1]')
###holiday
##jobNumber2 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]/option[2]')
###Sick
##jobNumber3 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]/option[3]')
###vacation
##jobNumber4 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]/option[4]')

#work
jobNumber6 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlJobDescription"]/option[6]')
jobNumber6.click()

earningCodeDropDown = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlPayCode"]')
earningCodeDropDown.click()

###holiday
##earningCode2 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlPayCode"]/option[2]')
#regular
earningCode3 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlPayCode"]/option[3]')
###sick
##earningCode4 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlPayCode"]/option[4]')
###vacation
##earningCode5 = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_ddlPayCode"]/option[5]')
earningCode3.click()

monday = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_txtDay2"]')
tuesday = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_txtDay3"]')
wednesday = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_txtDay4"]')
thursday = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_txtDay5"]')
friday = driver.find_element_by_xpath('//*[@id="rptTimeCardEdit__ctl1_txtDay6"]')
monday.send_keys('8')
tuesday.send_keys('8')
wednesday.send_keys('8')
thursday.send_keys('8')
friday.send_keys('8')

submitButton = driver.find_element_by_id('ibtnSubmit')
submitButton.click()

time.sleep(3)

continueButton = driver.find_element_by_id('ibtnContinue')
#continueButton.click()

driver.save_screenshot("TimeCardConfirmation.png")

driver.get('https://mail.google.com/mail/u/0/#inbox')

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

loginField = driver.find_element_by_id('identifierId')
nextButton = driver.find_element_by_id('identifierNext')
loginField.send_keys('gmail login')
nextButton.click()
time.sleep(3)

passwordField = driver.find_element_by_name('password')
passwordField.send_keys('gmail pass')
nextButton = driver.find_element_by_id('passwordNext')
nextButton.click()

time.sleep(5)
page_body = driver.find_element_by_tag_name('body')

#create new message
page_body.send_keys('c')

#define the "recipient" field
time.sleep(3)
recipient = driver.find_element_by_name('to')
recipient.send_keys('reciving adrs')

#define the "subject line" field
subject = driver.find_element_by_name('subjectbox')
timenow = datetime.datetime.now().strftime("%I:%M:%S %p")
datenow = datetime.datetime.now().strftime("%Y-%m-%d")
subject.send_keys("Timecard Submitted" + Keys.TAB + timenow + " " + datenow + " for week of " + str(today) + ".")

time.sleep(2)

attachButton = driver.find_element_by_xpath('//*[@data-tooltip = "Attach files"]')
attachButton.click()

time.sleep(3)

##clipboard.copy("C:\\Users\\m4k04\\Desktop\\TimeCardConfirmation.png")
##time.sleep(3)
##clipboard.paste()

pyautogui.typewrite(r"C:\Users\m4k04\Desktop\TimeCardConfirmation.png")
pyautogui.typewrite(['enter'])

time.sleep(3)

sendButton = driver.find_element_by_xpath('//*[@data-tooltip="Send ‪(Ctrl-Enter)‬"]')
sendButton.click()

driver.quit()

print("Done.")
