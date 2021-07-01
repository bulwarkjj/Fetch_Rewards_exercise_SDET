from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time


path = r'C:\Users\matt\Desktop\chromedriver.exe'  # path to chrome webdriver
driver = webdriver.Chrome(path)
driver.get(r"http://ec2-54-208-152-154.compute-1.amazonaws.com/")
driver.maximize_window()
alert = Alert(driver)

"""
ToDo: List up the bowls and gold bars since they are constants, make the list for bowls left and right.
compare the elements till I find the fake gold bar
	To fulfill requested steps 1-13 from the assigment I split gold bars into to equal lists to splat the left 
bowl with the lower end of gold bars and splat the right bowl with the higher end of gold bars to find the 
heavier side, then continued comparing sides as they shrunk while adding the median till finding the fake
gold bar. 
	To fulfill requested steps 14 & 15 I printed the required information and added some flavor to make it
	easier to read
	
!!possible failed deliverable!!
Sometimes the alert box wouldn't pop up even when I increased wait times to 10 seconds.  I don't know how 
to address that specific problem and I couldn't find solutions that worked when I researched the issue. 
I used a try/except block to handle the error. 
"""
leftbowl = []
rightbowl = []
goldbars = []

for i in range(9):
	leftbowl.append(driver.find_element_by_id(f'left_{i}'))
	rightbowl.append(driver.find_element_by_id(f'right_{i}'))
	goldbars.append(driver.find_element_by_id(f'coin_{i}'))

#  get a list of the weights to print out at the end
weighings = []
for i in range(9):
	weighings.append(driver.find_element_by_xpath(f'//*[@id="coin_{i}"]').get_attribute('data-value'))


low = 0
high = len(goldbars) - 1

while low < high:
	mid = int(low + ((high - low) / 2))
	# table reset
	driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[1]").click()
	a = 0
	for i in range(low, mid):
		# inputting to the left table
		leftbowl[a].send_keys(i)
		a += 1
	a = 0
	for i in range(mid + 1, high + 1):
		# inputting into the right table
		rightbowl[a].send_keys(i)
		a += 1

	# Weight the item
	driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[2]").click()
	time.sleep(5)
	# getting the result after weight
	result = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/button").text
	# print(result)

	if a == 1:
		if result == "<":
			goldbars[low].click()
			time.sleep(5)
			try:
				print(alert.text)
				alert.accept()
			except NoAlertPresentException:
				print("No alert popped up, but you found it.")
			print(f"Found the fake gold, it is number: {low}")
			break
		elif result == ">":
			goldbars[high].click()
			time.sleep(5)
			try:
				print(alert.text)
				alert.accept()
			except NoAlertPresentException:
				print("No alert popped up, but you found it.")
			print(f"Found the fake gold, it is number: {high}")
			break

	if result == "=":
		leftbowl[mid].click()
		time.sleep(5)
		try:
			print(alert.text)
			alert.accept()
		except NoAlertPresentException:
			print("No alert popped up, but you found it.")
		print(f"Found the fake gold, it is number: {mid}")
		break
	elif result == ">":
		low = mid
	else:
		high = mid

for index, weight in enumerate(weighings):
	print(f"Gold bar {index} weighs: {weight}")
time.sleep(5)

driver.quit()
