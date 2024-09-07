from selenium import webdriver
from selenium.webdriver.common.by import By






#Click 'Delete Account' Button:
delete_account= driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()

#Verify 'ACCOUNT DELETED!' and Click 'Continue' Button:
print("Your account has been permanently deleted!You can create new account to take advantage of member privileges to enhance your online shopping experience with us.")
continue_delete_button= driver.find_element(By.XPATH,"//a[normalize-space()='Continue']").click()
