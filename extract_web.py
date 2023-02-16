from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, timedelta
import openpyxl

driver = webdriver.Chrome()
workbook = openpyxl.load_workbook("Weather_data_sample.xlsx")
sheet = workbook.active
url = 'https://www.wunderground.com/history/daily/us/tx/austin/KAUS/date/2018-7-19'
driver.get(url)
df = pd.read_csv('sample_data.csv')
location_names = df['location'].tolist()
temp_date_str = df['date'].tolist()

temp_date = [datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%-m-%-d") for date_str in temp_date_str]


def get_yesterday(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    yesterday = date - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')


def get_last_week(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    last_week = date - timedelta(weeks=1)
    return last_week.strftime('%Y-%m-%d')


def get_last_month(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    last_month = date.replace(day=1) - timedelta(days=1)
    return last_month.strftime('%Y-%m-%d')


def get_last_year(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    last_year = date.replace(year=date.year - 1)
    return last_year.strftime('%Y-%m-%d')


def get_two_years_ago(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    two_years_ago = date.replace(year=date.year - 2)
    return two_years_ago.strftime('%Y-%m-%d')


def get_last_three_years(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    three_years_ago = date.replace(year=date.year - 3)
    return three_years_ago.strftime('%Y-%m-%d')


def get_last_four_years(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    three_years_ago = date.replace(year=date.year - 4)
    return three_years_ago.strftime('%Y-%m-%d')


def get_last_five_years(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    three_years_ago = date.replace(year=date.year - 5)
    return three_years_ago.strftime('%Y-%m-%d')


for location, tdate in zip(location_names, temp_date):
    search_location = driver.find_element(By.ID, 'wuSearch')
    search_location.clear()
    search_location.send_keys(location)
    sleep(2)
    search_location.send_keys(Keys.RETURN)
    sleep(10)
    base_url = driver.current_url
    today_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{tdate}'
    yesterday_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_yesterday(tdate)}'
    lastweek_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_last_week(tdate)}'
    lastmonth_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_last_month(tdate)}'
    lastyear_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_last_year(tdate)}'
    last2year_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_two_years_ago(tdate)}'
    last3year_url = base_url.replace('/weather/', '/history/daily/').rstrip(
        '/') + f'/date/{get_last_three_years(tdate)}'
    last4year_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_last_four_years(tdate)}'
    last5year_url = base_url.replace('/weather/', '/history/daily/').rstrip('/') + f'/date/{get_last_five_years(tdate)}'

    '''''''''''''''''''''''''''''''''''''get thatday data '''''''''''''''''''''''''''''''''''''
    print('Collecting that day data')
    driver.get(today_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get day before data '''''''''''''''''''''''''''''''''''''
    print('Collecting the day before of that day data')
    driver.get(yesterday_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get lastweek data '''''''''''''''''''''''''''''''''''''
    print('Collecting a week before of that day data')
    driver.get(lastweek_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get lastmonth data '''''''''''''''''''''''''''''''''''''
    print('Collecting a month before of that day data')
    driver.get(lastmonth_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get lastyear data '''''''''''''''''''''''''''''''''''''
    print('Collecting a year before of that day data')
    driver.get(lastyear_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    '''''''''''''''''''''''''''''''''''''get last2year data '''''''''''''''''''''''''''''''''''''
    print('Collecting two years before of that day data')
    driver.get(last2year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    
    '''''''''''''''''''''''''''''''''''''get last3year data '''''''''''''''''''''''''''''''''''''
    print('Collecting three years before of that day data')
    driver.get(last3year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get last4year data '''''''''''''''''''''''''''''''''''''
    print('Collecting four years before of that day data')
    driver.get(last4year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass

    '''''''''''''''''''''''''''''''''''''get last5year data '''''''''''''''''''''''''''''''''''''
    print('Collecting five years before of that day data')
    driver.get(last5year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    ROW = 4
    dict_list = []
    for line in DATA:
        try:
            components = line.split()
            if not ':30' in components[0]:
                extract_data = components[2], components[4], components[6], components[8], components[9], components[
                    11], \
                    components[13], components[15], components[17]
                dict_list.append(extract_data)
        except:
            None
    START = 7
    for i, data in enumerate(dict_list):
        for j, value in enumerate(data):
            sheet.cell(row=ROW, column=START + j, value=value)
        START += j + 1
    print(location, tdate)
    workbook.save("Weather_data_sample.xlsx")
    ROW += 1
    print('Next ROW',ROW)