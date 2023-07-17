from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
import time

@given('I am on the useinsider.com website')
def open_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://useinsider.com/")

@when('I accept the cookies and  select "Career" from the Company menu in the navigation bar')
def click_careers_button(context):
    accept_all_button = context.driver.find_element(By.ID, "wt-cli-accept-all-btn")
    context.driver.execute_script("arguments[0].click()", accept_all_button)
    company_button = context.driver.find_element(By.ID, "navbarDropdownMenuLink")
    context.driver.execute_script("arguments[0].click()", company_button)
    carrers_button = context.driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/ul[1]/li[5]/div/div[2]/a[2]")
    context.driver.execute_script("arguments[0].click()",carrers_button)

@then('I should see the Career page opened and Life At Insider, Locations and Teams blocks are opened or not')
def assert_the_careers_page(context):
    time.sleep(5)
    assert "https://useinsider.com/careers/" in context.driver.current_url
    life_at_insider_section = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/section[4]")
    our_location_section = context.driver.find_element(By.ID, "career-our-location")
    job_list_section = context.driver.find_element(By.ID, "career-find-our-calling")

#scenario 2
@given('I am on the "Career" page')
def career_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    carrers_page = context.driver.get("https://useinsider.com/careers/")

@when('I click "See all teams" button')
def click_see_all_teams_button(context):
    wait = WebDriverWait(context.driver, 4)
    see_all_teams_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/a")))
    context.driver.execute_script("arguments[0].click()",see_all_teams_button)

@then('I should see the Quality Assurance job is appeared')
def assert_qa_section_appeared(context):
    wait = WebDriverWait(context.driver, 3)
    qa_jobs = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/section/div/div/a")))

@when('I click "Quality Assurance" and I click "See all QA jobs"')
def click_quality_assurance(context):
    wait = WebDriverWait(context.driver,3)
    quality_assurance_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@href="https://useinsider.com/careers/quality-assurance/"]')))
    context.driver.execute_script("arguments[0].click()",quality_assurance_button)
    see_all_qa_jobs = wait.until(EC.presence_of_element_located((By.XPATH,'//a[@href="https://useinsider.com/careers/open-positions/?department=qualityassurance"]')))
    see_all_qa_jobs.click()

@then('I should see the "Open Positions" page is opened')
def assert_open_positions_page(context):
    assert "https://useinsider.com/careers/open-positions/?department=qualityassurance" in context.driver.current_url

# Web tarayıcısını kapat
def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()