
# Import Dependencies

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import time
import regex as re
from string import ascii_uppercase
from my_functions import get_num_clicks, get_data
#########################################################


# Initialize the data & lists
officer_name = []
officer_rank = []
officer_command = []
officer_shield = []
officer_appt_date = []
officer_arrests_total = []
officer_dept_rcgntn = []

data = [officer_name, officer_rank,officer_command,officer_shield,officer_appt_date,
        officer_arrests_total,officer_dept_rcgntn]

# Loop for each letter of the alphabet
for letter in ["a"]:
    # Open up table html
    url = f"https://oip.nypdonline.org/view/1004/@SearchName=SEARCH_FILTER_VALUE&@LastNameFirstLetter={letter}//%7B%22hideMobileMenu%22:true%7D/true/true"
    driver = webdriver.Chrome() # Open Chrome
    driver.get(url) # Go to NYPD page
    time.sleep(10) # Wait a few for everything to load

    # CALL FUNCTION TO FIND HOW MANY PAGES NEED TO BE CLICKED
    num_clicks = get_num_clicks(driver)
    type(num_clicks)

    for click in range(1,2):
        # CALL FUNCTION TO GRAB DATA
        data = get_data(driver,data)
        # GO TO NEXT PAGE
        next_page_handle = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[3]/a[3]/span")
        next_page_handle.click()
        time.sleep(10)
    
    # Once done collecting for the letter, quit and go to the next url
    driver.quit()

print("done")

# Unpack the data
officer_name = data[0]
officer_rank = data[1]
officer_command = data[2]
officer_shield = data[3]
officer_appt_date = data[4]
officer_arrests_total = data[5]
officer_dept_rcgntn = data[6]

# Create a dictionary with data
dict = {"Officer Name": officer_name, "Rank": officer_rank, "Command": officer_command, "Shield": officer_shield, "Appointed Date": officer_appt_date,
        "Total Arrests": officer_arrests_total,"Department Recognitions": officer_dept_rcgntn}

# Turn dictionary into dataframe & save to CSV
df = pd.DataFrame(dict)
print(df)
path = "./output.csv"
df.to_csv(path)