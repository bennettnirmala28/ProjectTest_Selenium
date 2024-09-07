from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.ElementUtil import ElementUtil


#Click 'Proceed To Checkout':
proceed_button = driver.find_element(By.XPATH,"//a[normalize-space()='Proceed To Checkout']").click()
print("The Product is displayed")

#Verify Delivery Address:
deliveryaddress_details=driver.find_element(By.XPATH,"//ul[@id='address_delivery']//li[3]").text
print("Smart erp,Smarterp PVT. LTP.,NH4, P.O.Box no. 54, Smarterp,India,Karnataka,Bengaluru,560099,9987704478")

#Verify Billing Address:
billingaddress_details=driver.find_element(By.XPATH,"//ul[@id='address_invoice']//li[3]']").text
print("Smart erp,Smarterp PVT. LTP.,NH4, P.O.Box no. 54, Smarterp,India,Karnataka,Bengaluru,560099,9987704478")

