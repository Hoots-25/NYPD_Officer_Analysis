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