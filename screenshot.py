import pyscreenshot as ImageGrab
from selenium import webdriver


driver = webdriver.Firefox()
url = "http://www.koreabaseball.com/Schedule/GameCenter/Main.aspx"
# print(driver.get_window_size())
driver.maximize_window()
driver.get(url)

im = ImageGrab.grab(bbox=(400, 685, 1264, 800))
im.show()

driver.close()