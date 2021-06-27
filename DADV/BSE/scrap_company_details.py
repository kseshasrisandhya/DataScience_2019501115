import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

driver = webdriver.Chrome()

initial_url = 'https://www.bseindia.com/corporates/List_Scrips.aspx'
driver.get(initial_url)
time.sleep(4)

segment = '//*[@id="ContentPlaceHolder1_ddSegment"]'
driver.find_element_by_xpath(segment).send_keys('Equity')

status = '//*[@id="ContentPlaceHolder1_ddlStatus"]'
driver.find_element_by_xpath(status).send_keys('Active')


click_button = '//*[@id= "ContentPlaceHolder1_btnSubmit"]'
driver.find_element_by_xpath(click_button).click()


def process_html(html_content):
    code = []
    name = []
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', id="ContentPlaceHolder1_gvData")
    # class = "TTRow_left"
    for link in table.find_all('tr'):
        i = 0
        security_code = 0
        security_name = ''
        for ele in link.find_all('td', {"class": "TTRow_left"}):
            i += 1
            if(i == 1):
                security_code = ele.text
            if(i == 3):
                security_name = ele.text
                break
        if(security_code != 0 and security_name != ''):
            code.append(security_code)
            name.append(security_name)
    return code, name


security_code_details = []
security_name_details = []
for i in range(17):
    # Write logic to extract first page details
    # Extract first page logic here
    if(i == 16):
        code, name = process_html(driver.page_source)
        security_code_details.extend(code)
        security_name_details.extend(name)
        for k in range(9, 13):
            page_xpath = '//*[@id="ContentPlaceHolder1_gvData"]/tbody/tr[1]/td/table/tbody/tr/td['+str(
                k)+']/a'
            driver.find_element_by_xpath(page_xpath).click()
            # Extract logic here
            time.sleep(2)
            code, name = process_html(driver.page_source)
            security_code_details.extend(code)
            security_name_details.extend(name)
            print(len(security_code_details))
            print(len(security_name_details))
            print("---------------------------------------------")
    else:
        code, name = process_html(driver.page_source)
        security_code_details.extend(code)
        security_name_details.extend(name)
        print(len(security_code_details))
        print(len(security_name_details))
        print("--------------------------------------------------------")
        for j in range(2, 14):
            if(i == 0 and j == 11):
                page_xpath = '//*[@id="ContentPlaceHolder1_gvData"]/tbody/tr[1]/td/table/tbody/tr/td['+str(
                    j)+']/a'
                driver.find_element_by_xpath(page_xpath).click()
                time.sleep(2)
                print("hello")
                break
            elif(i != 0 and j in [2, 3]):
                continue
            else:
                page_xpath = '//*[@id="ContentPlaceHolder1_gvData"]/tbody/tr[1]/td/table/tbody/tr/td['+str(
                    j)+']/a'
                driver.find_element_by_xpath(page_xpath).click()
                # Extract logic here
                time.sleep(2)
                code, name = process_html(driver.page_source)
                security_code_details.extend(code)
                security_name_details.extend(name)
                print(len(security_code_details))
                print(len(security_name_details))
                print("---------------------------------------------")

dict_companies = {}
for i in range(len(security_code_details)):
    dict_companies[security_code_details[i]] = security_name_details[i]

for i in dict_companies:
    print(i, dict_companies[i])

with open('companies.pickle', 'wb') as handle:
    pickle.dump(dict_companies, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('companies_data.csv', 'w') as f:
    for key in dict_companies.keys():
        f.write("%s, %s\n" % (key, dict_companies[key]))
