from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o= ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

## using ID locator for Username
user = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
user.send_keys("standard_user")


## using XPAth for Password
pas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password"]')))
pas.send_keys("secret_sauce")

logi = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="login-button"]')))
logi.click()

ttl = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[. = "Products"]')))
print(f"Page Title: {ttl.text}")

pr_nn = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
for n in pr_nn:
    print("Product Name:", n.text)

pp_pr = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
for p in pp_pr:
    print("Product Price:", p.text)

ad_ca = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//button[@class="btn btn_primary btn_small btn_inventory "])[4]')))
ad_ca.click()


driver.quit()
