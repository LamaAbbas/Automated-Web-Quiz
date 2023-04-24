import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def main():
    # Setting scraper to its initial position
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(r"user-data-dir=C:\Users\lamaa\AppData\Local\Google\Chrome\User Data\Default")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(r"C:\\chromedriver.exe"), options=options)

    URL = 'https://www.wizard101.com/game/trivia'
    trivia_page = '/quiz/trivia/game/kingsisle-trivia'
    driver.get(URL)
    get_back_to_page(driver, trivia_page)

    login(driver)

    # Going through each trivia link
    ki_wanted_text = driver.find_elements(By.XPATH, "//a[@href]")

    for element in ki_wanted_text:

        link = element.get_attribute("href")

        # Opening the first desired trivia
        if "pirate101-adventure" in link:
            run_p101_adventuring(driver, link)
        elif "wizard101-adventuring" in link:
            run_w101_adventuring(driver, link)
        # elif "wizard101-conjuring" in trivia_url:
        #     run_w101_conjuring(driver, trivia_url)
        # elif "wizard101-magical" in trivia_url:
        #     run_w101_magical(driver, trivia_url)
        # elif "wizard101-marleybone" in trivia_url:
        #     run_w101_marleybone(driver, trivia_url)
        # elif "wizard101-mystical" in trivia_url:
        #     run_w101_mystical(driver, trivia_url)
        # elif "wizard101-spellbinding" in trivia_url:
        #     run_w101_spellbinding(driver, trivia_url)
        # elif "wizard101-spells" in trivia_url:
        #     run_w101_spells(driver, trivia_url)
        # elif "wizard101-wizard-city" in trivia_url:
        #     run_w101_city(driver, trivia_url)
        # elif "wizard101-zafaria" in trivia_url:
        #     run_w101_zafaria(driver, trivia_url)

        # get_back_to_page(driver, trivia_page)
            
    return 0

def get_back_to_page(driver, link_url):
    l = driver.find_element("xpath", '//a[@href="{}"]'.format(link_url))
    driver.execute_script("arguments[0].click();", l)

def login(driver):
    username = 'cat2005omar'
    password = 'La20ooma!'

    # username = 'CutiestLulu2000'
    # password = 'Lamoushy2000'

    time.sleep(1)

    enter_user = driver.find_element("id", "loginUserName")
    enter_pass = driver.find_element("id", "loginPassword")
    submit = driver.find_element("xpath", "//input[@type='submit']")

    enter_user.send_keys(username)

    time.sleep(1)

    enter_pass.send_keys(password)

    time.sleep(1)

    driver.execute_script("arguments[0].click();", submit) 

    time.sleep(1)
    return 0

def quiz_completion(driver):
    # Press complete
    l = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", l)
    time.sleep(5)

    # Handle modal dialogue
    # iframe switch
    iframe = driver.find_element(By.NAME, "jPopFrame_content")
    driver.switch_to.frame(iframe)
    
    time.sleep(3)

    l = driver.find_element(By.CLASS_NAME, "buttonsubmit")
    driver.execute_script("arguments[0].click();", l)

    driver.switch_to.default_content()

    time.sleep(1)

    l = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", l)

def run_p101_adventuring(driver, trivia_url):

    # P101 Adventring
    l = driver.find_element("xpath", '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", l)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element("class name", "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements("class name", "answerText")
        buttons = driver.find_elements("name", "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Scurvy" in question_list:
                current_answer = 'Captain Dan'
            elif "Mancha?" in question_list:
                current_answer = 'Donkey Hotay'
            elif "Claw" in question_list:
                current_answer = 'Buster Crab'
            elif "Sheriff" in question_list:
                current_answer = 'Rooster Cogburn'
            elif "owner" in question_list:
                current_answer = 'One Eyed Jack'
            elif "Kraken" in question_list:
                current_answer = 'Skinny Pete'
            elif "Monkey?" in question_list:
                current_answer = 'Gortez'

        elif "What" in question_list:
            if "Musketeer" in question_list:
                current_answer = "Ol' Fish Eye"
            if "Windstone" in question_list:
                current_answer = 'Violet'
            elif "Privateer" in question_list:
                current_answer = 'The Commodore'
            elif "class" in question_list:
                current_answer = 'Buccaneer'
            elif "Magnificent" in question_list:
                current_answer = 'The Wild Bunch'
            elif "Frogfather" in question_list:
                current_answer = 'Spices'
            elif "Spymaster?" in question_list:
                current_answer = 'Deacon'

        elif "Where" in question_list:
            if "refuge" in question_list:
                current_answer = "Corsair's Channel"
            elif "companion?" in question_list:
                current_answer = 'On board the Erebus'
            elif "parent's" in question_list:
                current_answer = 'Jonah Town'

        elif "How" in question_list:
            current_answer = '3'

        elif "General" in question_list:
            current_answer = 'A Chicken'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        l = driver.find_element("id", "nextQuestion")
        driver.execute_script("arguments[0].click();", l)

        time.sleep(5)

    quiz_completion(driver)
    return 0

def run_w101_adventuring(driver, trivia_url):
    l = driver.find_element("xpath", '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", l)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element("class name", "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements("class name", "answerText")
        buttons = driver.find_elements("name", "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Bear" in question_list:
                current_answer = 'Valgard Goldenblade'
            if "Helephant?" in question_list:
                current_answer = 'Lyon Lorestriker'

        elif "Which" in question_list:
            if "Lore" in question_list:
                current_answer = 'Fire Dragon'
            if "Anchor" in question_list:
                current_answer = 'Rasik Anchor Stone'
            if "Aztecan" in question_list:
                current_answer = 'Philosoraptor'

        elif "What" in question_list:
            if "Royal" in question_list:
                current_answer = 'The Krokonomicon'
            if "rank" in question_list:
                current_answer = 'Damage + DoT'
            if "Ribbon" in question_list:
                current_answer = 'Time Flux'
            if "Lady" in question_list:
                current_answer = 'Trick question, she has a sword.'
            if "Professor" in question_list:
                current_answer = 'Pasta Arrabiata'
            if "determines" in question_list:
                current_answer = 'Where they come from and their school of focus.'
            if "secret" in question_list:
                current_answer = 'Order of the Fang'
            if "Gurtok" in question_list:
                current_answer = 'Balance'
            if "unique" in question_list:
                current_answer = 'There are scorch marks on the ceiling'
            if "dance" in question_list:
                current_answer = 'The bee dance'
            if "Dark" in question_list:
                current_answer = 'Shadow'

      
        elif "match" in question_list:
            current_answer = '5 minutes'
        
        elif "Shaka" in question_list:
            current_answer = 'The Greatest Living Zebra Warrior'

        elif "unmodified" in question_list:
            current_answer = '900-1000 Fire damage + 300 Fire damage to all enemies'

        elif "Ravens" in question_list:
            current_answer = 'The Everwinter, to cover the world in ice:'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        l = driver.find_element("id", "nextQuestion")
        driver.execute_script("arguments[0].click();", l)

        time.sleep(5)

    quiz_completion(driver)
    return 0

def run_w101_conjuring(driver, trivia_url):
    return 0

def run_w101_magical(driver, trivia_url):
    return 0

def run_w101_marleybone(driver, trivia_url):
    return 0

def run_w101_mystical(driver, trivia_url):
    return 0

def run_w101_spellbinding(driver, trivia_url):
    return 0

def run_w101_spells(driver, trivia_url):
    return 0

def run_w101_city(driver, trivia_url):
    return 0

def run_w101_zafaria(driver, trivia_url):
    return 0



main()
