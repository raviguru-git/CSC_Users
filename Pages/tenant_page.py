# Author : Ravi Guruprasad

from selenium.webdriver.common.by import By

import  time
class TenantPage:

    def __init__(self,driver,tenant_name):
        self.driver = driver
        self.tenant_name = tenant_name
        self.UTM_id ="NGMGMT"



    def  select_tenant(self):
         ele=self.driver.find_element(By.XPATH, '//div[@title="' + self.tenant_name + '"]')
         time.sleep(8)
         eleFound=self.driver.execute_script("arguments[0].scrollIntoView();",ele)
         time.sleep(2)
         self.driver.execute_script("arguments[0].click();",ele)

    def click_UTM(self):
        curr_ele=self.driver.find_element(By.XPATH,'//md-card[@id="NGMGMT"]')
        curr_ele.click()


