# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:10:31 2018

@author: lil
"""

from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


######################################################################################################
os.chdir('/Users/xiaochuanli')#work dict
savepath = '/Users/xiaochuanli/indeed'
today = time.strftime('%Y-%m-%d')

########################################################################################################
good = ['Python','data', 'SQL', 'investment', 'travel', 'AWS', 'quantitative', 'analytical', 'master', 'MSc',\
        'modelling']
bad = ['5+', 'C++', 'sales', 'CPA', 'Java']
########################################################################################################
baseURL = 'https://www.indeed.ca/'
loginEmail = 'XXXXXXXXX'
password = 'XXXXXX'
#########################################################################################################
#Chrome setting
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : savepath}#set download path here
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "/Users/xiaochuanli/chromedriver"#path to chromedriver

########################################################################################################
#Start webdriver, Login to website
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.get(baseURL)


def login():#log in to Indeed.ca
    driver.find_element_by_xpath("//*[@id='desktopGlobalHeader']/nav/ul[2]/li[2]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='signin_email']").clear()
    driver.find_element_by_xpath("//input[@id='signin_email']").send_keys(loginEmail)#enter username
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='signin_password']").clear()
    driver.find_element_by_xpath("//input[@id='signin_password']").send_keys(password)#enter password
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='loginform']/button").click()#click login button
    time.sleep(2)
    #driver.find_element_by_xpath("//*[@id='jobsLink']").click()#click on job search
    time.sleep(2)

def searcher(keyword, city):#Search job and location
    driver.find_element_by_xpath("//*[@id='text-input-what']").clear()
    driver.find_element_by_xpath("//*[@id='text-input-what']").send_keys(keyword)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='text-input-where']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='text-input-where']").clear()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='text-input-where']").send_keys(city)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='whatWhere']/form/div[3]/button").click()
    time.sleep(2)
    
def list_job():#get job titles/id on the webpage to a list
    #driver.find_element_by_xpath("//*[@id='refineresults']").click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    ids = soup.find_all("h2", attrs={"class":"jobtitle"})
    idList = []
    for job_id in ids:
        idList.append(job_id.get('id'))
    return idList


def scorer(goodWords, badWords, textString):#search job summary and assign a score
    Score = 0
    for word in goodWords:
        if word in textString:
            Score += 1
    for word in badWords:
        if word in textString:
            Score -= 1
    return(Score)
    
    
        
def match(input_list):#get job title, job score and job url
    titleList = []
    #companyList = []
    scoreList = []
    urlList = []
    for job_id in input_list:
        element = driver.find_element_by_xpath("//*[@id='%s']/a"%job_id)
        ActionChains(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        title = soup.find('title').text
        #title = soup.find('b', attrs={'class':'jobtitle'}).text
        titleList.append(title)
        #company = soup.find('span', attrs={'class':'company'}).text
        #companyList.append(company)
        try:
            summary = soup.find('span', attrs={'id':'job_summary'}).text
        except:
            summary = soup.find('div', attrs={'class':'jobsearch-JobComponent-description icl-u-xs-mt--md'}).text
        score = scorer(good, bad, summary)
        scoreList.append(score)
        url = 'www.indeed.ca'+soup.find('link', attrs={'rel':'alternate'}).get('href')
        #if title.endswith('.ca'):
            #url = 'www.indeed.ca'+soup.find('link', attrs={'rel':'alternate'}).get('href')
            #url = url.replace('/m','',1)
        #else:
            #url = 'www.ca.indeed.com'+soup.find('link', attrs={'rel':'alternate'}).get('href')
            #url = url.replace('/m','',1)
        urlList.append(url)
        driver.close()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])
    return titleList, scoreList, urlList
        
    
def main(keyword, city, pages):#main function
    login()
    searcher(keyword, city)
    try:
        driver.find_element_by_xpath("//*[@id='refineresults']/div[3]/span/a").click()
    except:
        driver.find_element_by_xpath("//*[@id='refineresults']/div[2]/span/a").click()
    time.sleep(2)
    titleResult = []
    scoreResult = []
    urlResult = []
    for i in range(pages):
        page = list_job()
        titles, scores, urls = match(page)
        titleResult.extend(titles)
        scoreResult.extend(scores)
        urlResult.extend(urls)
        driver.find_element_by_class_name("np").click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath("*[@id='popover-link-x']").click()
            break
        except:
            print('No pop-up')
        time.sleep(1)
        #driver.find_element_by_xpath("//*[@id='resultsCol']/a[10]/span/span").click()#next page
    data = pd.DataFrame({'Job Title': titleResult,
                         'Job Score': scoreResult,
                         'Job URL': urlResult})
    data = data.sort_values(by=['Job Score'], ascending=False)
    writer = pd.ExcelWriter('%s_Summary_%s.xlsx'%(keyword,today))
    data.to_excel(writer, index=False)
    writer.save()
    
main('Quantitative', 'Toronto, ON', 2)

        
    
