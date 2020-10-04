from selenium import webdriver

driverPath = r"C:\chromedriver_win32\chromedriver.exe"
driverCall = webdriver.Chrome(executable_path=driverPath)

driver.get("http://python.org")
driver.close()