import time
import random
import winsound
import threading
import json
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
  

def open_browser(login_details):
    frequency = 2000 

    # Assists in avoiding timed out requests from duplicate user agents, preventing detection
    user_agents = ["Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/68.0.3029.110 Safari/638.3",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/99.0.4844.61 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/638.36", 
	                "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/638.36",
                    "Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/638.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/638.36"
                    ]
    this_user = random.choice(user_agents)
    print(this_user)
    
    # Setting scraper to its initial position
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("user-agent=" + this_user)
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = webdriver.Chrome(options = options)
    # Masks to prevent detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    x = random.uniform(1, 2)
    
    time.sleep(x)

    # Navifating from the start of the site
    URL = 'https://www.wizard101.com/game/trivia'
    driver.get(URL)

    time.sleep(x * 2)
    driver.execute_script("window.scrollTo(0, 1000)") 
    time.sleep(x * 1.5)

    get_back_to_page(driver)
    
    login(driver, login_details)

    # unpacking JSON
    f = open('quizes.json')
    data = json.load(f)

    # Going through each trivia link
    ki_wanted_text = driver.find_elements(By.XPATH, "//a[@href]")
    try:
        # Looping through each link to find the ones we care about
        for elements in range(len(ki_wanted_text)):
            y = random.uniform(1, 2)
            ki_wanted_text = driver.find_elements(By.XPATH, "//a[@href]") 
            link = ki_wanted_text[elements].get_attribute("href")
            # Try this out
            # driver.execute_script("ki_wanted_text.scrollIntoView()")
            for quiz_name in data:
                if quiz_name in link:
                    time.sleep(x * y)
                    process_quiz(driver, link, data, quiz_name)
                    break
            
    except NoSuchElementException:
        duration = 2000
        winsound.Beep(frequency, duration)
        input("Problem with {}".format(threading.current_thread().name))
    
    print("Completed")
    duration = 1000
    winsound.Beep(frequency, duration)
    time.sleep(2)
    
    driver.quit()       
    return 0

def get_back_to_page(driver):
    x = random.uniform(1, 2)
    time.sleep(x)

    link_url = '/quiz/trivia/game/kingsisle-trivia'
    button = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(link_url))
    driver.execute_script("arguments[0].click();", button)

def login(driver, login_details):
    x = random.uniform(1, 2)
    time.sleep(x)

    enter_user = driver.find_element(By.ID, "loginUserName")
    enter_pass = driver.find_element(By.ID, "loginPassword")
    submit = driver.find_element(By.XPATH, "//input[@type='submit']")

    enter_user.send_keys(login_details[0])

    time.sleep(x * 2)

    enter_pass.send_keys(login_details[1])

    time.sleep(x * 1.5)

    driver.execute_script("arguments[0].click();", submit) 

    time.sleep(x * 1.25)
    return 0

def process_quiz(driver, link, data, quiz_name):

    time.sleep(0.5)

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(link))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion").text

        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        for pair in data[quiz_name]:
            for key in pair:
                if  key == question:
                    current_answer = pair[key]

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])
       
        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        x = random.uniform(6, 8)
        time.sleep(x)

    quiz_completion(driver)
    return 0

def quiz_completion(driver):
    # Press complete
    button = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", button)

    # Handle modal dialogue
    # iframe switch
    iframe = driver.find_element(By.NAME, "jPopFrame_content")
    driver.switch_to.frame(iframe)
    
    x = random.uniform(1, 3)
    time.sleep(x)

    submit = driver.find_element(By.CLASS_NAME, "buttonsubmit")
    driver.execute_script("arguments[0].click();", submit)

    # If CAPTCHA occurs
    try:
        captcha_iframe = driver.find_element(By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']")
        driver.switch_to.frame(captcha_iframe)
        captcha = driver.find_element(By.CLASS_NAME, "rc-imageselect-challenge")
        frequency = 2000
        duration = 600
        winsound.Beep(frequency, duration)
        print("CAPTCHA detected for {}.".format(threading.current_thread().name), end=" ")
        input("Press ENTER when you've submitted the CAPTCHA: ")
        print("Proceeding! \n")

        driver.switch_to.parent_frame()
    except NoSuchElementException:
        print("No CAPTCHA found.")
    
    driver.switch_to.default_content()
    time.sleep(x * 2)

    # "Take another quiz"
    button = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", button)

    get_back_to_page(driver)

if __name__=="__main__":            

    load_dotenv() 
    accounts = (int) (os.getenv("NUM_OF_ACCOUNTS"))
    # tuples of ("username","password")
    login_list = list()

    for i in range(1, accounts+1):
        username = os.getenv("LOGIN_USERNAME_"+ (str) (i))
        password = os.getenv("LOGIN_PASSWORD_"+ (str) (i))
        login_list.append((username, password))

    threads = list()

    for i in range(len(login_list)):
        thread = threading.Thread(name=login_list[i][0], target=open_browser, args=(login_list[i],))
        thread.start()
        time.sleep(5)
        threads.append(thread)

    for thread in threads:
        thread.join()