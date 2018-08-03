#import schedule
import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select

#surfacebook and work computer webdriver path
driver = webdriver.Chrome('C:\Program Files\Python\Python36\chromedriver.exe')
driver.get('https://dawson8a.onelogin.com/login');

#link to iframe: https://dawson.jamisprime.com/etime/TimeCardEdit.aspx?hdFormWonder=_0Arkk6UA-Ix0

userName = driver.find_element_by_id('user_email')
userName.send_keys('user_email')
password = driver.find_element_by_id('user_password')
password.send_keys('PASS$')
loginButton = driver.find_element_by_id('user_submit')
loginButton.click()
time.sleep(2)
securityQ1 = driver.find_element_by_xpath("(//input[@class='security-answer'])[1]")
securityQ1.send_keys('Q1')
securityQ2 = driver.find_element_by_xpath("(//input[@class='security-answer'])[2]")
securityQ2.send_keys('Q2')
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

##select_fr = Select(driver.find_element_by_id("ctlTimeCardSelector_ddlDate"))
##select_fr.select_by_index(2)

#option1 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[1]')
#option2 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[2]')
option3 = driver.find_element_by_xpath('//*[@id="ctlTimeCardSelector_ddlDate"]/option[3]')
option3.click()

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

continueButton = driver.find_element_by_id('ibtnContinue')
#continueButton.click()


driver.close()

print("Done.")

##schedule.every().day.at("09:00").do(job,'It is 09:00')
##
##while True:
##    schedule.run_pending()
##    #time.sleep(60) # wait one minute
