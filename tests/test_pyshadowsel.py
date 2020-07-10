from shadowselenium import __version__
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .import ShadowElement
import pytest
import logging

# log=logging.getLogger('log')
# log.setLevel()
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://shrinivasbb.github.io/ShadowDomSite')
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

class TestShadowDOM(BaseTest):

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_get_shadow_element_using_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            sdom.find_shadow_element_by_css("shadow-hostnav", ".nav-link").click()
            self.driver.find_element_by_css_selector("div.alert span").click()
        except Exception as e:
            pytest.fail(e,pytrace=True)

    def test_get_shadow_element_using_webelement_and_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elemz = self.driver.find_element_by_tag_name("shadow-hostnav")
            sdom.find_element_under_shadow_root_by_css(elemz, ".nav-link").click()
            self.driver.find_element_by_css_selector("div.alert span").click()
        except Exception as e:
            pytest.fail(e,pytrace=True)

    def test_dont_get_shadow_element_using_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elemz = self.driver.find_element_by_tag_name("shadowhostnav")
            sdom.find_shadow_element_by_css(elemz, ".nav-link").click()
            self.driver.find_element_by_css_selector("div.alert span").click()
        except Exception as e:
            pass

    def test_dont_get_shadow_element_using_webelement_and_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elemz = self.driver.find_element_by_tag_name("shadow-hostnav")
            sdom.find_element_under_shadow_root_by_css(elemz, ".navlink").click()
            self.driver.find_element_by_css_selector("div.alert span").click()
        except Exception as e:
            pass

    def test_get_shadow_elements_using_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elem=sdom.find_shadow_elements_by_css("shadow-hostnav", ".nav-link")
            assert len(elem)==3
        except Exception as e:
            pytest.fail(e,pytrace=True)

    def test_get_shadow_elements_using_webelement_and_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elemz = self.driver.find_element_by_tag_name("shadow-hostnav")
            elem = sdom.find_elements_under_shadow_root_by_css(elemz, ".nav-link")
            assert len(elem)==3
        except Exception as e:
            pytest.fail(e,pytrace=True)

    def test_get_all_shadow_elements_using_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elem=sdom.find_all_shadow_elements_by_css("shadow-hostnav")
            assert len(elem)==14
        except Exception as e:
            pytest.fail(e,pytrace=True)

    def test_get_all_shadow_elements_using_webelement_and_css_selectors(self):
        try:
            sdom = ShadowElement(self.driver)
            elemz = self.driver.find_element_by_tag_name("shadow-hostnav")
            elem = sdom.find_all_elements_under_shadow_root_by_css(elemz)
            assert len(elem)==14
        except Exception as e:
            pytest.fail(e,pytrace=True)