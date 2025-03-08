from page_locators.locators import PageLocators

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://practice-automation.com/form-fields/'
driver = webdriver.Chrome()
driver.get(link)
action = ActionChains(driver)

name = driver.find_element(*PageLocators.name)
name.send_keys('Ivan')

password = driver.find_element(*PageLocators.password)
password.send_keys('123')

checkbox_milk = driver.find_element(*PageLocators.checkbox_milk).click()
action.scroll_to_element(checkbox_milk)
action.click(checkbox_milk)

checkbox_coffee = driver.find_element(*PageLocators.checkbox_coffee)
action.scroll_to_element(checkbox_coffee)
action.click(checkbox_coffee)

radiobutton_yellow = driver.find_element(*PageLocators.radiobutton_yellow)
action.scroll_to_element(radiobutton_yellow)
action.click(radiobutton_yellow)

select_auto = driver.find_element(*PageLocators.select_auto)
action.scroll_to_element(select_auto)
action.click(select_auto)

tools = driver.find_elements(*PageLocators.tools)
spisok = []
for i in tools:
    spisok.append(i.text)
myspisok = [x.split('\n') for x in spisok][0]
number = len(myspisok)
longest = max(myspisok, key=len)

email = driver.find_element(*PageLocators.email)
action.scroll_to_element(select_auto)
action.click(select_auto)
email.send_keys('name@example.com')

message = driver.find_element(*PageLocators.message)
message.send_keys(str(number) + "\n" + longest)

submit = driver.find_element(*PageLocators.submit)
action.scroll_to_element(submit)
action.click(submit)

driver.quit()