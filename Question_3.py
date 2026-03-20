from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.shine.com/registration/")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@id="id_file"]').send_keys(r"C:\Users\ADITYA\Downloads\Aditya Paliwal Resume.pdf")

driver.quit()