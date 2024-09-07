from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


#Add Products to Cart:
Product_element = driver.find_element(By.XPATH,"//a[@href='/products']").click()
add_item1 = driver.find_element(By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]").click()
Continue_Shopping_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Continue Shopping']").click()
add_item2=driver.find_element(By.XPATH,"//div[5]//div[1]//div[1]//div[2]//div[1]//a[1]").click()
Continue_Shopping_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Continue Shopping']").click()
add_item3=driver.find_element(By.XPATH,"//div[11]//div[1]//div[1]//div[2]//div[1]//a[1]").click()
Continue_Shopping_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Continue Shopping']").click()
add_item4=driver.find_element(By.XPATH,"//div[22]//div[1]//div[1]//div[2]//div[1]//a[1]").click()
Continue_Shopping_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Continue Shopping']").click()

#Click 'Cart' Button:
view_cart = driver.find_element(By.XPATH,"//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()

#Verify that Cart Page is Displayed:
cart_page=driver.find_element(By.XPATH, "//div[@id='cart_info']").text
print("The Product is displayed")
