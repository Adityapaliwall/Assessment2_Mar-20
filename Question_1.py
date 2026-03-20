from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o= ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.prokabaddi.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '//span[. = "Standings"]').click()

ta_na = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[3]')
mpl = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[4]')
won = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[5]')
lost = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[6]')
sc_di = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[7]')
pts = driver.find_element(By.XPATH, '(//p[. = "Jaipur Pink Panthers"]/../../../..//p)[13]')

print(f"Name of the Team: {ta_na.text}")
print(f"Matches Played = {mpl.text}")
print(f"Won = {won.text}")
print(f"Lost = {lost.text}")
print(f"Score Difference = {sc_di.text}")
print(f" Points = {pts.text}")

driver.quit()
