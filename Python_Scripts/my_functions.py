## Pull Basic Data Function
# Need Selenium Webdriver to access elements
def get_data(driver, basic_data):

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    officer_name = basic_data[0]
    officer_rank = basic_data[1]
    officer_command = basic_data[2]
    officer_shield = basic_data[3]
    officer_appt_date = basic_data[4]
    officer_arrests_total = basic_data[5]
    officer_dept_rcgntn = basic_data[6]

    for i in range (1,100):
        officer_name.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[1]").text)
        officer_rank.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[2]").text)
        officer_command.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[3]").text)
        officer_shield.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[4]").text)
        officer_appt_date.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[5]").text)
        officer_arrests_total.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[6]").text)
        officer_dept_rcgntn.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[7]").text)
    
    updated_data = [officer_name, officer_rank,officer_command,officer_shield,officer_appt_date,officer_arrests_total,officer_dept_rcgntn]
    return updated_data

#####################################################################
#####################################################################
## Calculate how many clicks are needed per letter
# Needs regex & Selenium Webdriver
def get_num_clicks(driver):
    
    # Import Dependencies
    import regex as re 
    from selenium import webdriver

    pager_info = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[3]/span").text
    pager_info = re.findall(r'\d+(?:,\d+)?',f"{pager_info}") # Regex to isolate the numbers
    num_rows = int(pager_info[-1].replace(',','')) # Take the last value, remove the comma & turn the string to an integer
    num_clicks = (-(-num_rows//100)) - 1 # Knowing there are 100 entries/page, get number of clicks and round up and subtract 1
    
    return num_clicks

#####################################################################
#####################################################################
## Calculate how many rows there are per page
# Needs regex & Selenium Webdriver
def get_num_rows(driver):
    
    # Import Dependencies
    import regex as re 
    from selenium import webdriver
    pager_info = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/report-wrapper/report/div/div/div[2]/div/div/div[3]/span").text
    pager_info = re.findall(r'\d+(?:,\d+)?',f"{pager_info}")
    beg = int(pager_info[0])
    end = int(pager_info[1])
    num_rows = end - beg + 1

    return num_rows
#####################################################################
def get_ethnicity(driver):
    ethnicity = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]").text
    officer_name = officer_name = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text

    ethnicity_results = [officer_name, ethnicity]
    return ethnicity_results
#####################################################################
def csv_writer(data):
    from csv import writer
    
    with open('ETHNICITY.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(data)  
        # Close the file object
        f_object.close()

    return "Complete"




#####################################################################

# GET DETAILED DATA #

#####################################################################
def get_officer_data(driver, data):

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    # Get Ethnicity
    ethnicity_results = get_ethnicity(driver)    
    # Get Rank & Shield History
    rank_results = get_rank_and_shield(driver)
    # Get Department Recognitions
    awards_results = get_awards(driver)
    # Get Training
    training_results= get_training(driver)
    # Get Diciplinary History
    diciplinary_results = get_diciplinary_history(driver)
    #  Get Arrests Processed
    arrests_results = get_arrests(driver)
    # Write to CSV




#####################################################################

# NESTED FUNCTIONS #

#####################################################################

#####################################################################
    def get_rank_and_shield(driver):
        try:
            # Click Button
            driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/report-header/div/span/span/button[1]").click()
            time.sleep(3)

            # Get Rank & Shield History 
            officer_name = []
            date = []
            title = []
            shield_no = []
            rows = int(len(driver.find_elements_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr")))

            for row in range(1,rows + 1):
                officer_name.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text)
                date.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[1]").text)
                title.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[2]").text)
                shield_no.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[3]").text)


            rank_results =  [officer_name, title, date, shield_no]
        except:
            print(f"{officer_name[0]} No Records")

        return rank_results
#####################################################################
#####################################################################
    def get_arrests(driver):
        try:
            #Get Length of rows of table
            rows = len(driver.find_elements_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr"))

            type = []
            amount = []
            officer_name = []

            for row in (1, rows):
                # Get Officer Name
                officer_name.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text)
                # Get Arrest Type
                type.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[1]").text)
                # Get Number of Arrests per Type
                amount.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[2]").text)

            arrests_results =  [officer_name, type,  amount]
        except:
            print(f"{officer_name} No Arrests")

        return arrests_results
#####################################################################
#####################################################################
# Department Recgns & Awards 
    def get_awards(driver):
        try:
            
            # Click the button
            driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/report-header/div/span/span/button[2]").click()
            time.sleep(2)

            officer_name = []
            date = []
            award = []
            rows = int(len(driver.find_elements_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr")))

        
            for row in range(1,rows + 1):
                officer_name.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text)
                date.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[1]").text)
                award.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{row}]/td[2]").text)
                
        except:
            print(f"{officer_name} No Recognitions")

        awards_results =  [officer_name, date, award]

        return awards_results

#####################################################################
#####################################################################
    def get_training(driver):
        import regex as re 
        from selenium import webdriver

        # Get Training Summary
        # Click the button
        driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/report-header/div/span/span/button[3]").click()
        time.sleep(2)

        date = []
        training = []
        officer_name = []

        # Get Number of clicks
        pager_info = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[3]/span").text
        pager_info = re.findall(r'\d+(?:,\d+)?',f"{pager_info}") # Regex to isolate the numbers
        num_rows = int(pager_info[-1].replace(',','')) # Take the last value, remove the comma & turn the string to an integer
        num_clicks = (-(-num_rows//100)) - 1 # Knowing there are 100 entries/page, get number of clicks and round up and subtract 1

        for click in range(1,num_clicks + 2):
            # Get Num Rows
            pager_info = driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[3]/span").text
            pager_info = re.findall(r'\d+(?:,\d+)?',f"{pager_info}")
            beg = int(pager_info[0])
            end = int(pager_info[1])
            items = end - beg + 1

            for item in range(1,items + 1):
                # Get Training
                officer_name.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text)
                date.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{item}]/td[1]").text)
                training.append(driver.find_element_by_xpath(f"/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[2]/table/tbody/tr[{item}]/td[2]").text)

            if click < num_clicks + 1:
                # Go to next page
                driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div/div[2]/div/div/div[3]/a[3]").click()
                time.sleep(2)
            else:
                end

            training_results = [officer_name, date, training]
        return training_results

    def get_diciplinary_history(driver):
        # Click on Diciplinary History
        driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/report-header/div/span/span/button[4]").click()
        officer_name = []
        date = []
        charges = []
        allegations = []

        try:
            officer_name.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[1]/report-wrapper/report/div/div/div[2]/div/div[1]").text)
            date.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[1]").text)
            charges.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]").text)
            allegations.append(driver.find_element_by_xpath("/html/body/section/div/div/section/div/div/div[2]/div/div/div[2]/report-wrapper/report/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[3]").text)

        except:
            print("No Diciplinary History")

        diciplinary_results = [officer_name,date,charges,allegations]
        return diciplinary_results
    
    def write_to_csv(results):

        
        # Write to CSV
         
        return 0

    ethnicity_results
    awards_results
    rank_results
    arrests_results
    training_results
    diciplinary_results

    return 0