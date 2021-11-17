# pip3 install selenium undetected_chromedriver pandas
import undetected_chromedriver.v2 as uc
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
emails = pd.read_csv('import.csv').emails.tolist()
driver = uc.Chrome()
time.sleep(3)
driver.get('https://www.ip-adress.com/verify-email-address')
o=[]
try:
	for index, email in enumerate(emails):
		try:
			WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]')))
			driver.find_element(By.XPATH,'//input[@name="email"]').clear()
			driver.find_element(By.XPATH,'//input[@name="email"]').send_keys(email)
			driver.execute_script("document.getElementsByTagName('button')[1].click()")
			WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="result"]/p')))
			result = driver.find_element(By.XPATH,'//*[@id="result"]/p').text
			driver.execute_script("document.getElementsByTagName('summary')[0].click()")
			details = driver.find_element(By.XPATH,'//pre').text
			print(f"{index} | {email} | {re.sub(r'.+ is ','',result)}")
			o.append({
				'email':email,
				'result':result,
				'details':details,
				'is_valid':re.sub(r'.+ is ','',result)
				})
		except:
			o.append({
				'email':email,
				'result':None,
				'details':None,
				'is_valid':None
				})
finally:
	pd.DataFrame(o).to_csv('results.csv',index=False)
