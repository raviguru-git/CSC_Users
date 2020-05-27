from selenium import  webdriver
import  unittest
import sys
import  os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from  Pages.login_page import  LoginPage
from Pages.tenant_page import  TenantPage
from Pages.nsm_home_page import HomePage
from Pages.Common.Lib import lib
from Pages.Common.tablecheck import TableCheck
import  time
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\OFFICE_DATA\\Automation\\UI7\\input\\webdrivers\\chromedriver")
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

    def test_validation_nsm_users_gui(self):
        driver = self.driver
        driver.get("https://cloud.sonicwall.com")
        login = LoginPage(driver)
        login.enter_username("abc@sonicwall.com") # Not provided actual username here for security reasons but script works seamlessly.
        login.click_button("nextButton")
        login.enter_password("P******")   # Not provided actual password here for security reasons but script works seamlessly..
        login_button = driver.find_element_by_id("loginButton")
        driver.execute_script("arguments[0].click()",login_button)
        time.sleep(12)

        tenant_page = TenantPage(driver,"Ravi_Sprint28")
        tenant_page.select_tenant()
        tenant_page.click_UTM()

        nsm_page=HomePage(driver)
        nsm_page.click_on_tab("CSC Users",False)
        nsm_page.click_on_tab("Users",True)
        time.sleep(5)
        print(nsm_page.get_column_info())
        row_data=nsm_page.get_results()
        print(row_data)
        print(nsm_page.get_user(row_data))
        user_from_nsm=nsm_page.get_user(row_data)
        expected_users=['Ravi Guruprasad', 'Raja Rock', 'Ravi Guru','Tom Harry']

        if nsm_page.validate_users(user_from_nsm,expected_users):
            print("Users from NSM Page matches with expected Result:", "Testcase PASSED")
        else:
            print("Users from NSM Page doesn't match with expected Result:", "Testcase FAILED")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")







if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\OfficeData\\SELENIUMProjects\\CSC_Users\\Pages\\Reports\\'))






