"""
INSIDER AUTOMATION TASK
1-Visit useinsider.com and check Insider home page is opened or not
2-Select More menu in navigation bar, select "Carrers" and check Career page
3-its locations, Teams and Life at Insider blocks are opened or not
4-Click "See all teams" select Quality Assurance, click "See all QA jobs"
5-filter jobs by location - Istanbul, Turkey and department- Quality Assurance, check presence of jobs list
6-Check that all jobs' position contains "Quality Assurance", department contaions
7-Quality assurance, location contains "Istanbul, Turkey," and "Apply Now"  button
8-Click "Apply Now" button and check that this action redirects us to Lever Application form page
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import time

driver = webdriver.Chrome()
driver.maximize_window()
WebDriverWait(driver,15)

driver.get("https://useinsider.com/")

assert "https://useinsider.com/" in driver.current_url
wait = WebDriverWait(driver,10)

accept_all_button = driver.find_element(By.ID,"wt-cli-accept-all-btn")
driver.execute_script("arguments[0].click()",accept_all_button)

company_button = driver.find_element(By.ID,"navbarDropdownMenuLink")
driver.execute_script("arguments[0].click()",company_button)

carrer_button = driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/ul[1]/li[5]/div/div[2]/a[2]")
driver.execute_script("arguments[0].click()",carrer_button)

assert "https://useinsider.com/careers/" in driver.current_url

elements = [
    (By.XPATH, "/html/body/div[1]/div/div/section[4]", "life_at_insider_section"),
    (By.ID, "career-our-location", "our_locations_section"),
    (By.ID, "career-find-our-calling", "job_list")
]
for element in elements:
    locator = element[0]
    locator_value = element[1]
    element_name = element[2]
    if driver.find_elements(locator, locator_value):
        pass
    else:
        print("{} alan bulunamadı".format(element_name))

see_all_teams_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/a")
driver.execute_script("arguments[0].click()",see_all_teams_button)

quality_assurance_jobs = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="https://useinsider.com/careers/quality-assurance/"]')))
driver.execute_script("arguments[0].click()",quality_assurance_jobs)

see_all_qa_jobs = wait.until(EC.presence_of_element_located((By.XPATH,'//a[@href="https://useinsider.com/careers/open-positions/?department=qualityassurance"]')))
see_all_qa_jobs.click()

filter_jobs_locations = wait.until(EC.element_to_be_clickable((By.ID,"select2-filter-by-location-container")))
filter_jobs_locations.click()

time.sleep(2)

istanbul_turkey_location = wait.until(EC.presence_of_element_located((By.XPATH,'//option[@class="job-location istanbul-turkey"]')))
istanbul_turkey_location.click()

try:
    qa_jobs_list = driver.find_element(By.ID,"career-position-list")
    qa_jobs_list.click()
except (NoSuchElementException, InvalidSelectorException):
    print("QA Jobs List alanı gözükmemektedir..")

time.sleep(3)
try:  # bu alan için herhangi bir veri yanlış olduğunda hangisi olduğunu söylemesi veya herhangi bir locator yanlış olduğunda hangisinin olduğunu söylemesi eklenebilir !
    qa_jobs_title = driver.find_element(By.XPATH, '//span[@class="position-department text-large font-weight-600 text-primary"]')
    location_istanbul_turkey = driver.find_element(By.XPATH,'//div[@class="position-location text-large"]')

    if qa_jobs_title.text == "Quality Assurance" and location_istanbul_turkey.text == "Istanbul, Turkey":
        pass
    else:
        print("Bir Seçenek QA departman değil veya Lokasyon İstanbul Turkey değil")
except (NoSuchElementException, InvalidSelectorException):
    print("İlgili locatorda sorun var")

view_role_button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div[2]/div[3]/div/a")
driver.execute_script("arguments[0].click()",view_role_button)

current_window = driver.current_window_handle       #şu anki pencereye geri gelebilmek için tagliyor diyebiliriz
wait.until(EC.number_of_windows_to_be(2))           # 2 adet pencere açılana kadar bekle
new_window = driver.window_handles[-1]              # en son açılan pencereyi tanımladık
driver.switch_to.window(new_window)                 # En son açılan pencereye geç
new_window_url = driver.current_url                 # geçtiğimiz pencerenin url sini aldık
expected_url = "https://jobs.lever.co/useinsider/0ba4065b-955a-4661-ad4a-f32479f63757"
if new_window_url != expected_url:
    print("Yanlış Sayfaya Yönlendirildi, Yönlendirdiği sayfa adresi: {}\nBeklenen sayfa adresi: {}".format(new_window_url,expected_url))
else:
    pass

click_apply_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="postings-btn template-btn-submit shamrock" and @href="https://jobs.lever.co/useinsider/0ba4065b-955a-4661-ad4a-f32479f63757/apply"]')))
driver.execute_script("arguments[0].click()",click_apply_button)
time.sleep(5)