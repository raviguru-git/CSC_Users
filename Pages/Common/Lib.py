# Author : Ravi Guruprasad

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import  webdriver
import re
from selenium import  webdriver

class lib:

    def __init__(self,driver):
        self.driver=driver


    def get_user(self,x):
        user = []

        for k in x:

            for users in x[k]:

                if users == "FULL NAME":
                    user.append(x[k][users])
        return user

    def validate_users(self,l1, l2):
        check = False
        if all(item in l1 for item in l2):
            check = True
            return check
        else:
            check = False
            return check

