#Importing selenium and its webdriver/webdriver manager to enable automation
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


#Importing time to allow us to make the program wait for the save/unsave functions to update on the website
import time

#Importing pandas to deal with the CSV file
import pandas as pd

file_path = ('C:\\Users\\wanna\\Desktop\\Links.csv')

df = pd.read_csv(file_path)
CurrentPage = df.CurrentPage
CurrentPageValue = df.CurrentPage
xpath =df.XPATH
TargetLink = df.TargetLink

#creating a variable for the chrome driver's settings and adding my chrome profile to it so when it opens it will launch signed in as me with all my site cookies
chrome_options = webdriver.ChromeOptions()

#launching that driver and maximizing the window
driver=webdriver.Chrome(chrome_options)
driver.maximize_window()

site_url="http://127.0.0.1:5500"

lineBreak = '---------------------------------------------------------------------------------------------'

print(lineBreak)

for each in CurrentPage:
    try:
        #print(lineBreak)
        #print (CurrentPage)
       # print (TargetLink)
        print(f"Clicking on the {CurrentPageValue}'s {TargetLink} link.")
        driver.find_element(By.XPATH, f"{xpath}").click
        print(driver.title)
    except:
        print("Something went wrong on the last link...")




driver.quit()

# try:
#     driver.get(site_url)
#     print("Home page openned")
#     print(driver.title)
#     print(lineBreak)
#     print("Clicking on the Home Page's Community link:")
#     element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]/span[1]").click()
#     print(driver.title)    
#     print("Clicking on the Community Page's Home link:")
#     element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]").click()
#     print(driver.title)
#     print("Clicking on the Home Page's About link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Clicking on the About Page's Home link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Returning to the Community Page:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Clicking on the Community Page's About link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Clicking on the About Page's Community link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Clicking on the Community Page's Logo link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Returning to the About Page:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
#     print("Clicking on the About Page's Logo link:")
#     element = driver.find_element(By.XPATH,)    
#     print(driver.title)
# except:
#     print("Something went wrong during the test...")
# time.sleep(5)


#.click()
#driver.title