# Author : Ravi Guruprasad
from  selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from Pages.Common.tablecheck import TableCheck
from Pages.Common.Lib import lib
from selenium.webdriver.support import  expected_conditions as ec

class HomePage(TableCheck,lib):


    def __init__(self,driver):
        self.driver =driver
        #self.subtab = subtab
        self.driver.set_page_load_timeout(40)
        self.wait = WebDriverWait(self.driver,35)
        #self.tab_csc_users = "8"

    def __tabs(self,tab_name,subtab=None):
        if subtab == True:
            return self.driver.find_element(By.XPATH, "(//span[contains(text(), '" + tab_name + "')])[2]")
        else:
            return self.driver.find_element(By.XPATH, "//span[contains(text(), '" + tab_name + "')]")


       # return self.find_element(By.Xpath,"(//div[@class='sw-nav-item__content sw-flexbox sw-flexbox--center-items sw-flexbox__flex'])"+[self.tab_csc_users]+')

    def click_on_tab(self,tab_name,subtab):
        if subtab == True:
            self.__tabs(tab_name,subtab).click()
        else:
            self.__tabs(tab_name,False).click()

    def column_data(self):
        print("Inside column_data")
        # col_data = self.driver.find_elements(By.XPATH, "(//div[@class='sw-table-row__cell__wrapper sw-flexbox__flex sw-flexbox sw-flexbox--center-items'])")
        col_data = self.driver.find_elements(By.XPATH, "(//div[@data-raw-entry-index])")
        rData = []
        for webElement in col_data:
            rData.append(webElement)
            print(webElement)
        return rData







