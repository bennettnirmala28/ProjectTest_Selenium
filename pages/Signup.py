from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.ElementUtil import ElementUtil

driver = webdriver.Firefox()
driver.get ("https://automationexercise.com/")

class Signupform(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
signup_form = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()
name = driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Nirmala")
emailaddress = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("nims44@yopmail.com")
Signup_button = driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()

#Enter Account Information
Title = driver.find_element(By.XPATH,"//input[@id='id_gender2']").click()
Password = driver.find_element(By.ID,"password").send_keys ("Nirmala@123")
day_field = driver.find_element(By.ID,"days")
day_field.send_keys("15")
month_field = driver.find_element(By.ID,"months")
month_field.send_keys("June")
year_field = driver.find_element(By.ID,"years")
year_field.send_keys("2000")

#Address Information
First_name = driver.find_element(By.ID, "first_name").send_keys ("Smart")
Last_name= driver.find_element(By.ID, "last_name").send_keys ("erp")
Company = driver.find_element(By.ID, "company").send_keys ("Smarterp PVT. LTP.")
Address = driver.find_element(By.ID, "address1").send_keys ("NH4, P.O.Box no. 54, Smarterp,")
country_field = driver.find_element(By.ID,"country")
country_field.send_keys("India")
state_field = driver.find_element(By.ID,"state")
state_field.send_keys("Karnataka")
city_field = driver.find_element(By.ID,"city")
city_field.send_keys("Bengaluru")
zipcode_field = driver.find_element(By.ID,"zipcode")
zipcode_field.send_keys("560099")
mobile_number_field = driver.find_element(By.ID,"mobile_number")
mobile_number_field.send_keys("9987704478")
create_account=driver.find_element(By.XPATH,"//button[normalize-space()='Create Account']").click()

#Verify 'ACCOUNT CREATED!' and Click 'Continue' Button:
print("Congratulations! Your new account has been successfully created!You can now take advantage of member privileges to enhance your online shopping experience with us.")
continue_btn = driver.find_element(By.XPATH,"//a[normalize-space()='Continue']").click()

#Verify 'Logged in as username' at Top:
loggedin_message = driver.find_element(By.XPATH, "//li[10]//a[1]").text
print("Logged in as Nirmala")