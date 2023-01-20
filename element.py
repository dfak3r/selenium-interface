from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        #Run driver for 100 sec until
        #lamda finds the element using 'locator'
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        #Run driver for 100 sec until
        #lambda finds the element using 'locator'
        #return the element with the value defined by basepageelement
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")