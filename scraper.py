from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dateutil.parser import parse
import time
import pandas as pd
review = []
a= True
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365")
time.sleep(1)
scroll_element = driver.find_element_by_id('product-reviews')
driver.execute_script("arguments[0].scrollIntoView();",scroll_element)
time.sleep(1)
click_element = driver.find_element_by_class_name("ReviewsHeaderWYR-seeAll").click()
time.sleep(1)
select = Select(driver.find_element_by_class_name("field-input--compact"))
select.select_by_value('submission-desc')
i = 1
print("please wait")
while True:
    time.sleep(1)
    reviews_element = driver.find_elements_by_class_name("review")
    print(f"Scraping {i} page",end="\n")
    for element in reviews_element:
        dtime = parse(element.find_element_by_class_name("review-date-submissionTime").get_attribute("content"))
        if dtime.year==2020 and dtime.month<12:
            a = False
            break
        review_date = element.find_element_by_class_name("review-date-submissionTime").text
        reviewer_name = element.find_element_by_class_name("review-footer-userNickname").text
        try:
            review_title = element.find_element_by_class_name("review-title").text
        except: 
            review_title= None
        review_body = element.find_element_by_class_name("review-text").text
        review_rating = len( element.find_elements_by_class_name("star-rated"))
        review.append([review_date,reviewer_name,review_title,review_body,review_rating])
    if a==False:
        break
    myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'paginator-btn-next')))
    driver.find_element_by_class_name("paginator-btn-next").click()
    i+=1
driver.close()
print("Scraping finished")  
df = pd.DataFrame(review)
df.columns = ["Review date","Reviewer name","Review title","Review body","Rating"]
print("Saving data to output.csv file")
df.to_csv("output.csv")
print("output.csv file is ready")

