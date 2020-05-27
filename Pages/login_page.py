# Author : Ravi Guruprasad

class LoginPage:

    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_id ="username"
        self.nextbutton_id="nextButton"
        self.password_textbox_id="password"
        self.loginbutton_id="loginButton"


    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_name(self.password_textbox_id).clear()
        self.driver.find_element_by_name(self.password_textbox_id).send_keys(password)

    def click_button(self,button):
        self.driver.find_element_by_id(button).click()
