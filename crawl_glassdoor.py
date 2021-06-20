import time
import random
from tqdm import tqdm
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')

def crawl_company(sCompanyName,numPages=100):
    with open(sCompanyName+'.txt','w',encoding='utf-8') as f:
        sUrl = "https://www.glassdoor.com.hk/Reviews/" + \
        sCompanyName + \
        "-Reviews-E6036.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng"
        driver.get(sUrl)
        driver.find_element_by_css_selector(
            '[class="d-flex align-items-center justify-content-center p-0 m-0 HeaderStyles__signInButton"]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "userEmail")))
        email = driver.find_element_by_id("userEmail")
        email.send_keys("rohit@octobabel.io")
        pas = driver.find_element_by_id("userPassword")
        pas.send_keys("uVXph_KB38_hvvd")
        pas.submit()
        for i in tqdm(range(2,numPages+1)):
            time.sleep(random.randint(3,20))
            soup=BeautifulSoup(driver.page_source, 'html.parser')
            reviews=soup.find_all('li', attrs= {'class':"noBorder empReview cf pb-0 mb-0"})
            for review in reviews:
                rating=-1
                ratingHTML=review.find('span',attrs={'class':"ratingNumber mr-xsm"})
                if ratingHTML is not None:
                    rating=ratingHTML.text
                pros=''
                prosHTML = review.find('span', attrs={'data-test': "pros"})
                if prosHTML is not None:
                    pros = prosHTML.text
                cons = ''
                consHTML = review.find('span', attrs={'data-test': "cons"})
                if consHTML is not None:
                    cons = consHTML.text
                adviceManagement = ''
                adviceManagementHTML = review.find('span', attrs={'data-test': "advice-management"})
                if adviceManagementHTML is not None:
                    cons = adviceManagementHTML.text
                reviewDict={
                    'rating':rating,
                    'pros':pros,
                    'cons':cons,
                    'adviceManagement': adviceManagement
                }
                f.write(json.dumps(reviewDict)+'\n')
            sUrl = "https://www.glassdoor.com.hk/Reviews/" + \
                   sCompanyName + \
                   "-Reviews-E6036_P" + str(i) + \
                                      ".htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng"
            driver.get(sUrl)
            f.flush()

if __name__ == "__main__":
    crawl_company('Amazon')