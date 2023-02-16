from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from time import sleep
import os
from datetime import datetime, timedelta

driver = webdriver.Chrome()
url = 'https://www.wunderground.com/history/daily/us/tx/austin/KAUS/date/2018-7-19'
driver.get(url)
df = pd.read_csv('sample_data.csv')
location_names = df['location'].tolist()
temp_date_str = df['date'].tolist()
if not os.path.exists('files'):
    os.mkdir('files')


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
    print(driver.current_url)
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
    print(today_url)
    # today
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
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "w") as file:
        file.write(data)

    # yesterday
    driver.get(yesterday_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)
    # weekly

    driver.get(lastweek_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)

    # monthly
    driver.get(lastmonth_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)

    '''''''''''''''''''''''''''''''''''''get lastyear data '''''''''''''''''''''''''''''''''''''

    # driver = webdriver.Chrome()
    driver.get(lastyear_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)
        # driver = webdriver.Chrome()
        # last 2 year
    driver.get(last2year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)

    driver.get(last3year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)

    driver.get(last4year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA) + "\n"
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)
    driver.get(last5year_url)
    sleep(10)
    tbodies = driver.find_elements(By.CSS_SELECTOR, "tbody")
    DATA = []
    for i in range(10):
        try:
            element = tbodies[i].text.strip()
            DATA.append(element)
        except:
            pass
    data = "\n".join(DATA)
    with open(f"files/{location}_{tdate}.txt", "a") as file:
        file.write(data)
