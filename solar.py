# import requests
# import selenium
import os
import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
# from googlemaps import GoogleMaps

class solarCalculator():
    def init(self):
        pass
    
    def get_full_url(self, latitude, longitude):
        base_url = "https://sunroof.withgoogle.com/building/"
        return base_url + str(latitude) + '/' + str(longitude) + '/' + '#?f=buy'


    def get_data(self, latitude, longitude):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        # driver = webdriver.Chrome(options=op)
        driver = webdriver.Chrome('/Users/kwitv/Documents/CodingProjects/HackHarvard2022/Harvardhacks2022/chromedriver', options=op)
        driver.get(self.get_full_url(latitude, longitude))

        html = driver.page_source

        main_data = {
            'num_hours_solar': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[1]/div[2]/md-card[1]/ul/li[1]/div[2]").text,
            'sqft_avail': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[1]/div[2]/md-card[1]/ul/li[2]/div[2]").text,
            'savings': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[1]/div[2]/md-card[2]/div[1]/div[1]").text
        }
            

        envirionmental_impact = {
            'carbon-dioxide': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[2]/md-card/md-card-content/div/place-metrics-cell[1]/div[2]").text,
            'passenger-cars': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[2]/md-card/md-card-content/div/place-metrics-cell[2]/div[2]").text,
            'tree-seedlings': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[2]/md-card/md-card-content/div/place-metrics-cell[3]/div[2]").text
        }


        cost = {
            'upfront-with-incentives': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[3]/md-card/md-card-content/div/cost-cell[1]/div[1]").text,
            '20-year-benefits-': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[3]/md-card/md-card-content/div/cost-cell[2]/div[1]").text,
            # '20-year-savings': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[3]/md-card/md-card-content/div/cost-cell[3]/div[1]").text,
            'years-til-payback': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[3]/md-card/md-card-content/div/cost-cell[4]/div[1]").text,
            'up-front-cost-of-installation': driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[3]/md-card/md-card-content/show-more/div/table/tbody/tr[1]/td[2]/span").text,
        }
        # envirionmental_impact = driver.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[2]/md-card/md-card-content/div")
        # # print("env", envirionmental_impact.text)
        # for impact in envirionmental_impact.find_elements(By.CLASS_NAME, "place-metrics-cell has-icon"):
        #     print(impact.text)
        #     print(1)

        # print(envirionmental_impact)

        # bs = BeautifulSoup(html)
        # print(bs)
        # bsobject = bs.find_element(By.XPATH, "/html/body/div[1]/address-view/div[1]/div/div/section[2]/div/md-content[2]/md-card/md-card-content/div")
        # for tag in bsobject.find_all("div", {"class": "place-metrics-cell has-icon"}):
        #     print(tag.text)

        driver.close()
        
        data_dict = {
            "main_date": main_data,
            "envirionmental_impact": envirionmental_impact,
            "cost": cost
        }

        print(data_dict)
        return data_dict

    def send_data(self): 
        elemNumHours, sqft_avail, savings = self.get_data()

        json_out = {'elemNumHours': elemNumHours, 
            'sqft_avail': sqft_avail, 
            'savings': savings}

        return json_out # todo ad 

        # function for monthly electricity












