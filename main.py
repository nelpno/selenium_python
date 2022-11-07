from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path=GeckoDriverManager().install())

# object of ChromeOptions class
o = Options()
fp = webdriver.FirefoxProfile('C:/Users/Cas/AppData/Roaming/Mozilla/Firefox/Profiles/oh2je6x7.default-release')

# adding specific Chrome Profile Path
# o.add_experimental_option('detach', True)
# o.add_argument('user-data-dir=C:/Users/Cas/AppDat/Local/Google/Chrome/User Data')
# o.add_argument('profile-directory=Default')
# set chromedriver.exe path
driver = webdriver.Firefox(options=o, service=service, firefox_profile=fp)
# maximize browser
driver.maximize_window()
# launch URL
driver.get("https://business.facebook.com/ads/manager/billing_history/summary/?act=704083103754311")
# get browser title
print(driver.title)
# close browser

