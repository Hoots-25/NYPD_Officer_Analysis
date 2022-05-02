# Import Dependencies

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import time
import regex as re
from string import ascii_uppercase
from my_functions import get_num_clicks, get_num_rows, get_ethnicity, csv_writer
#########################################################

# Loop for each letter of the alphabet
for letter in ascii_uppercase:
    # Open up table html
    url = f"https://oip.nypdonline.org/view/1004/@SearchName=SEARCH_FILTER_VALUE&@LastNameFirstLetter={letter}//%7B%22hideMobileMenu%22:true%7D/true/true"
    driver = webdriver.Chrome() # Open Chrome
    driver.get(url) # Go to NYPD page
    time.sleep(10) # Wait a few for everything to load

    # CALL FUNCTION TO FIND HOW MANY PAGES NEED TO BE CLICKED
    num_clicks = get_num_clicks(driver)

    # Loop for each page
    for click in range(1,num_clicks):
        num_rows = get_num_rows(driver)
        
        # Loop for each name on each page
        for row in range(1,100):
            
            # Find the new frame element
            frame_element = driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]")
            # Click on the frame element
            frame_element.click()
            time.sleep(8)

            # Switch the the new frame
            new_frame = driver.find_element_by_tag_name("iframe")
            driver.switch_to.frame(new_frame)

            # CALL FUNCTION TO GRAB ETHNICITY
            data = get_ethnicity(driver)

            # Write to CSV
            csv_writer(data)

            # Switch back to the previous content (YOU MUST DO THIS BEFORE CLOSING THE FRAME)
            driver.switch_to.default_content()
            time.sleep(2)
            # Close the frame
            close_icon = driver.find_elements_by_class_name("icon-close")
            print(close_icon)
            close_icon[1].click()
            time.sleep(4)

        # GO TO NEXT PAGE
        next_page_handle = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[3]/a[3]/span")
        next_page_handle.click()
        time.sleep(15)
    
    # Once done collecting for the letter, quit and go to the next url
    driver.quit()
    print(f"Done with: {letter}.")