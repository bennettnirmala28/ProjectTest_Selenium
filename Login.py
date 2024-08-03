
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  
driver.get ("https://automationexercise.com/")

#Signup - filling in the form
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

#Add Products to Cart:
Product_element = driver.find_element(By.XPATH,"//a[@href='/products']").click()
add_item1=driver.find_element(By.XPATH,"//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]").click()
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

#Click 'Proceed To Checkout':
proceed_button = driver.find_element(By.XPATH,"//a[normalize-space()='Proceed To Checkout']").click()
print("The Product is displayed")

#Verify Delivery Address:
deliveryaddress_details=driver.find_element(By.XPATH,"//ul[@id='address_delivery']//li[3]").text
print("Smart erp,Smarterp PVT. LTP.,NH4, P.O.Box no. 54, Smarterp,India,Karnataka,Bengaluru,560099,9987704478")

#Verify Billing Address:
billingaddress_details=driver.find_element(By.XPATH,"//ul[@id='address_invoice']//li[3]']").text
print("Smart erp,Smarterp PVT. LTP.,NH4, P.O.Box no. 54, Smarterp,India,Karnataka,Bengaluru,560099,9987704478")

#Click 'Delete Account' Button:
delete_account= driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()

#Verify 'ACCOUNT DELETED!' and Click 'Continue' Button:
print("Your account has been permanently deleted!You can create new account to take advantage of member privileges to enhance your online shopping experience with us.")
continue_delete_button= driver.find_element(By.XPATH,"//a[normalize-space()='Continue']").click()





 

     
       


        
        

   




      

   