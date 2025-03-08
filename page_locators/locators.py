from selenium.webdriver.common.by import By

class PageLocators:
    name=(By.XPATH, "//*[@id='feedbackForm']/label[1]")
    password=(By.XPATH, "//*[@id='feedbackForm']/label[2]")
    checkbox_milk=(By.ID, 'drink2')
    checkbox_coffee=(By.ID, 'drink3')
    radiobutton_yellow=(By.ID, 'color3')
    select_auto=(By.CSS_SELECTOR, "#automation > option:nth-child(2)")
    email=(By.ID, 'email')
    message=(By.NAME, 'message')
    submit=(By.CSS_SELECTOR, '#submit-btn')
    tools=(By.CSS_SELECTOR, "#feedbackForm > ul")