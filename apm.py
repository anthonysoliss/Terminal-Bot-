from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/Users/anthonysolis/labs/chromedriver')
driver.get('https://termpoint.apmterminals.com/')
# Accounts
username = driver.find_element_by_name('Login_Nm')
username.send_keys('mlexpress2003')
password = driver.find_element_by_name('Login_Pwd')
password.send_keys('MLXS2003')
password.send_keys(Keys.RETURN)
driver.implicitly_wait(30)


schedule = driver.find_element_by_xpath('//a[contains(@href,"/ScheduleAppointment")]').click()


while True:
	try:
		appointment = driver.find_element_by_class_name("search").click()
		appointment_type_md = driver.find_element_by_name('MD').click() # Empty dropoff
		c_number = driver.find_element_by_name('containerName').send_keys('TLLU57')
		submit = driver.find_element_by_xpath("//button[@class='ui primary button components__StyledButton-yks008-0 jAPNmA']").click()
		date = driver.find_element_by_id('calendar0').click()
		date_day = driver.find_element(By.XPATH, '//span[text()="15"]').click()
		slot_time = driver.find_element_by_id('ipgrid_0_slot').click()
		time_slot = driver.find_element(By.XPATH, '//span[text()="08:00 - 12:00"]').click()
	except NoSuchElementException:
		driver.refresh()
	else:
		appointment = driver.find_element_by_class_name("search").click()
		appointment_type_md = driver.find_element_by_name('MD').click() # Empty dropoff
		c_number = driver.find_element_by_name('containerName').send_keys('TLLU57')
		submit = driver.find_element_by_xpath("//button[@class='ui primary button components__StyledButton-yks008-0 jAPNmA']").click()
		date = driver.find_element_by_id('calendar0').click()
		date_day = driver.find_element(By.XPATH, '//span[text()="15"]').click()
		slot_time = driver.find_element_by_id('ipgrid_0_slot').click()
		time_slot = driver.find_element(By.XPATH, '//span[text()="08:00 - 12:00"]').click()
		# appointment = driver.find_element(By.XPATH, '//span[text()="Schedule appointment"]').click()
		break



