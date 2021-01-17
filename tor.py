# from selenium import webdriver
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# binary = FirefoxBinary(r"C:\Program Files (x86)\TorBrowser\Browser\firefox.exe")
# profile = FirefoxProfile(r"C:\Program Files (x86)\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default")
#
# driver = webdriver.Firefox(profile, binary)
# driver.get("http://stackoverflow.com")
# driver.save_screenshot("screenshot.png")
# driver.quit()

# import unittest
# from time import sleep
# from tbselenium.tbdriver import TorBrowserDriver
#
#
# class TestSite(unittest.TestCase):
#     def setUp(self):
#         # Point the path to the tor-browser_en-US directory in your system
#         tbpath = '/home/kdas/.local/tbb/tor-browser_en-US/'
#         self.driver = TorBrowserDriver(tbpath, tbb_logfile_path='test.log')
#         self.url = "https://check.torproject.org"
#
#     def tearDown(self):
#         # We want the browser to close at the end of each test.
#         self.driver.close()
#
#     def test_available(self):
#         self.driver.load_url(self.url)
#         # Find the element for success
#         element = self.driver.find_element_by_class_name('on')
#         self.assertEqual(str.strip(element.text),
#                          "Congratulations. This browser is configured to use Tor.")
#         sleep(2)  # So that we can see the page
#
#
# if __name__ == '__main__':
#     unittest.main()

# from tbselenium.tbdriver import TorBrowserDriver
# with TorBrowserDriver(r"\\C:\\Program Files (x86)\\Tor Browser\\Browser\\TorBrowser") as driver:
#     driver.get("https://www.google.com")

import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

tbb_dir = "/path/to/TorBrowserBundle/"
tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
    driver.load_url("https://check.torproject.org")

tor_process.kill()
