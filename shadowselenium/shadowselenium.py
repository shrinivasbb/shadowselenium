from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common import by
from selenium.common.exceptions import NoSuchElementException
from shadowselenium.jstrace import JSTrace
import logging

class ShadowElement:
    
    def __init__(self,driver):
        self.driver=driver

    def find_shadow_element_by_css(self, shadowHostcss, cssSelector):
        logging.info("Verifying specific Shadow Element found under Shadow-Root using CSS Selector")
        obj = self.driver.execute_script(JSTrace.js_one_element.replace("param1", shadowHostcss)
                                                               .replace("param2", cssSelector))
        try: 
            obj.is_displayed()
            logging.info("Passed")
            return obj
        except Exception as e:
            logging.info("Failed")
            raise Exception(f"No Element(s) found with the CSS selectors {e}")
       
    def find_element_under_shadow_root_by_css(self,shadowHostelement, cssSelector):
        logging.info("Verifying specific Shadow Element found under Shadow-Root using WebElement")
        obj = self.driver.execute_script(JSTrace.js_one_webelement.replace("param2", cssSelector),shadowHostelement)
        try: 
            obj.is_displayed()
            logging.info("Passed")
            return obj
        except Exception as e:
            logging.info("Failed")
            raise Exception(f"No Element(s) found with the CSS selectors {e}")
         

    def find_shadow_elements_by_css(self, shadowHostcss, cssSelector):
        obj = self.driver.execute_script(JSTrace.js_all_elements.replace("param1", shadowHostcss)
                                                                .replace("param2", cssSelector))
        try: 
            obj[0].is_displayed()
            return obj
        except Exception as e:
            raise Exception(f"No Element(s) found with the CSS selectors {e}")

    def find_elements_under_shadow_root_by_css(self,shadowHostelement, cssSelector):
        obj = self.driver.execute_script(JSTrace.js_all_webelement.replace("param2", cssSelector),shadowHostelement)
        try: 
            obj[0].is_displayed()
            return obj
        except Exception as e:
            raise Exception(f"No Element(s) found with the CSS selectors {e}")

    def find_all_shadow_elements_by_css(self, shadowHostcss):
        obj = self.driver.execute_script(JSTrace.js_all_elements.replace("param1", shadowHostcss)
                                                                .replace("param2",'*'))
        try: 
            obj[0].is_displayed()
            return obj
        except Exception as e:
            raise Exception(f"No Element(s) found with the CSS selectors {e}")

    def find_all_elements_under_shadow_root_by_css(self,shadowHostelement):
        obj = self.driver.execute_script(JSTrace.js_all_webelement.replace("param2",'*'),shadowHostelement)
        try: 
            obj[0].is_displayed()
            return obj
        except Exception as e:
            raise Exception(f"No Element(s) found with the CSS selectors {e}")

    