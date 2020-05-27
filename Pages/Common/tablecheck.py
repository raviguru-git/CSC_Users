# Author : Ravi Guruprasad

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import  webdriver

class TableCheck:

    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(self,driver,15)


    def get_column_info(self):
        column_info=[]
        columns = self.driver.find_elements_by_xpath("//div/span[@class='sw-table-header__col__cell__wrapper__cont__text']")
        for column in columns:
            column_info.append(str(column.text))
        return  column_info

    def get_results(self,index=None):
        columns= self.get_column_info()
        data={}
        staleelement=True

        while staleelement:
            try:
                #print("while block")
                elements = self.driver.find_elements_by_xpath(
                    "//div[@class='sw-table__wrapper sw-flexbox__flex sw-flexbox sw-flexbox--column']/div[2]/div[1]/div/div[contains(@class,'sw-table-row')]{}"
                                                                 .format("[{}]".format(index) if index else ""))
                staleelement=False
            except Exception:
                staleelement=True



        for element in elements:
            currentindex=  elements.index(element) + 1 if not index else index
            parsed_data = {}
            for column in columns:
                value = element.find_element_by_xpath("//div[contains(@class,'sw-table-row')][{}]"
                                                      "/div[contains(@class,'sw-table-row__cell')][{}]".format(currentindex, columns.index(column) + 4)).text
                parsed_data.update({column: str(value)})
            data.update({currentindex: parsed_data})
        return data

    def get_number_of_results(self):
        return len(self.driver.find_elements_by_xpath("//div[@class='sw-table__wrapper sw-flexbox__flex sw-flexbox sw-flexbox--column']/div[2]/div[1]/div/div[contains(@class,'sw-table-row')]"))











