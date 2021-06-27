import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from multiprocessing import Pool


directory = os.getcwd() + os.path.sep + 'company_details'
preferences = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": directory,
    "directory_upgrade": True
}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', preferences)
driver = webdriver.Chrome(
    executable_path="F:/Data_Visualisation/BSE/chromedriver", options=options)


with open('companies.pickle', 'rb') as handle:
    dict_companies = pickle.load(handle)

list_of_companies = list(dict_companies.keys())


directory = 'F:/Data_Visualisation/BSE/company_details'
print(len(os.listdir(directory)))

with open('remaining.pickle', 'rb') as handle:
    remain_comp = pickle.load(handle)


def find_remain_company():
    remain_company = []
    for comp in list_of_companies:
        file_path = directory + '/' + comp+'.csv'
        if(os.path.exists(file_path) == False):
            remain_company.append(comp)

    with open('remaining.pickle', 'wb') as handle:
        pickle.dump(remain_company, handle, protocol=pickle.HIGHEST_PROTOCOL)


def remove_company():
    rem_company = []
    for company in os.listdir(directory):
        if((os.path.getsize(directory + '/' + company)/1024) < 15):
            rem_company.append(company)

    for comp_id in rem_company:
        company = directory + '/' + comp_id
        print("comp_id", os.path.getsize(company)/1024)
        os.remove(company)


def download_company_data(company_id):
    url = 'https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?flag=0'
    driver.get(url)
    time.sleep(2)
    xpath_search = '//*[@id = "ContentPlaceHolder1_smartSearch"]'
    driver.find_element_by_xpath(xpath_search).send_keys(company_id)
    time.sleep(3)
    driver.find_element_by_xpath(xpath_search).send_keys(Keys.RETURN)

    from_xpath = '//*[@id = "ContentPlaceHolder1_txtFromDate"]'
    driver.find_element_by_xpath(from_xpath).click()
    click_year = '//*[@id = "ui-datepicker-div"]/div/div/select[2]'
    driver.find_element_by_xpath(click_year).click()
    driver.find_element_by_xpath(click_year).send_keys(2016)
    click_month = '//*[@id = "ui-datepicker-div"]/div/div/select[1]'
    driver.find_element_by_xpath(click_month).click()
    driver.find_element_by_xpath(click_month).send_keys('Apr')
    click_day = '//*[@id = "ui-datepicker-div"]/table/tbody/tr[1]/td[6]/a'
    driver.find_element_by_xpath(click_day).click()

    to_xpath = '//*[@id="ContentPlaceHolder1_txtToDate"]'
    driver.find_element_by_xpath(to_xpath).click()
    click_year = '//*[@id="ui-datepicker-div"]/div/div/select[2]'
    driver.find_element_by_xpath(click_year).click()
    driver.find_element_by_xpath(click_year).send_keys(2021)
    click_month = '//*[@id="ui-datepicker-div"]/div/div/select[1]'
    driver.find_element_by_xpath(click_month).click()
    driver.find_element_by_xpath(click_month).send_keys('Apr')
    click_day = '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[5]/a'
    driver.find_element_by_xpath(click_day).click()

    submit_xpath = '//*[@id = "ContentPlaceHolder1_btnSubmit"]'
    driver.find_element_by_xpath(submit_xpath).click()

    time.sleep(2)

    download_xpath = '//*[@id = "ContentPlaceHolder1_btnDownload"]/i'
    driver.find_element_by_xpath(download_xpath).click()
    time.sleep(4)
    return company_id


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(download_company_data, remain_comp[1401:]))
