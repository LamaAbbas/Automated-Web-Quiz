import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def main():
    # Setting scraper to its initial position
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(r"user-data-dir=C:\Users\lamaa\AppData\Local\Google\Chrome\User Data\Default")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(r"C:\\chromedriver.exe"), options=options)
    

    URL = 'https://www.wizard101.com/game/trivia'
    driver.get(URL)
    get_back_to_page(driver)

    login(driver)

    # Going through each trivia link
    ki_wanted_text = driver.find_elements(By.XPATH, "//a[@href]")
    done = False
    # for element in ki_wanted_text:
    for i in range(0, 96):
        ki_wanted_text = driver.find_elements(By.XPATH, "//a[@href]")
        link = ki_wanted_text[i].get_attribute("href")
        
        # Opening the first desired trivia
        if "pirate101-adventure" in link:
            run_p101_adventuring(driver, link)
        elif "wizard101-adventuring" in link:
            run_w101_adventuring(driver, link)
        elif "wizard101-conjuring" in link:
            run_w101_conjuring(driver, link)
        elif "wizard101-magical" in link:
            run_w101_magical(driver, link)
        elif "wizard101-marleybone" in link:
            run_w101_marleybone(driver, link)
        elif "wizard101-mystical" in link:
            run_w101_mystical(driver, link)
        elif "wizard101-spellbinding" in link:
            run_w101_spellbinding(driver, link)
        elif "wizard101-spells" in link:
            run_w101_spells(driver, link)
        elif "wizard101-wizard-city" in link:
            run_w101_city(driver, link)
        elif "wizard101-zafaria" in link:
            run_w101_zafaria(driver, link)
            
    driver.quit()
    return 0


def get_back_to_page(driver):
    link_url = '/quiz/trivia/game/kingsisle-trivia'
    button = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(link_url))
    driver.execute_script("arguments[0].click();", button)


def login(driver):
    username = 'cat2005omar'
    password = 'La20ooma!'

    # username = 'CutiestLulu2000'
    # password = 'Lamoushy2000'

    # username = 'Lamoushy2000'
    # password = 'La20ooma!'

    time.sleep(1)

    enter_user = driver.find_element(By.ID, "loginUserName")
    enter_pass = driver.find_element(By.ID, "loginPassword")
    submit = driver.find_element(By.XPATH, "//input[@type='submit']")

    enter_user.send_keys(username)

    time.sleep(1)

    enter_pass.send_keys(password)

    time.sleep(1)

    driver.execute_script("arguments[0].click();", submit) 

    time.sleep(1)
    return 0


def quiz_completion(driver):
    # Press complete
    button = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", button)

    # Handle modal dialogue
    # iframe switch
    iframe = driver.find_element(By.NAME, "jPopFrame_content")
    driver.switch_to.frame(iframe)
    
    time.sleep(2)

    submit = driver.find_element(By.CLASS_NAME, "buttonsubmit")
    driver.execute_script("arguments[0].click();", submit)

    # time.sleep(10)
    # if CAPTCHA occurs
    try:
        time.sleep(5)
        # captcha = driver.find_element(By.ID, "rc-imageselect")
        # captcha = driver.find_element(By.CLASS_NAME, "rc-imageselect-instructions")
        captcha = driver.find_element(By.CLASS_NAME, "rc-imageselect-challenge")
        print("CAPTCHA detected.")
        input("Press ENTER when you've submitted the CAPTCHA: ")
        print("Proceeding!")
    except NoSuchElementException:
        print("No CAPTCHA found.")
    
    driver.switch_to.default_content()

    time.sleep(1)

    # "Take another quiz"
    button = driver.find_element(By.CLASS_NAME, "kiaccountsbuttongreen")
    driver.execute_script("arguments[0].click();", button)

    get_back_to_page(driver)


def run_p101_adventuring(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
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
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_adventuring(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Bear" in question_list:
                current_answer = 'Valgard Goldenblade'
            elif "Helephant?" in question_list:
                current_answer = 'Lyon Lorestriker'

        elif "Which" in question_list:
            if "lore" in question_list:
                current_answer = 'Fire Dragon'
            elif "Anchor" in question_list:
                current_answer = 'Rasik Anchor Stone'
            elif "Aztecan" in question_list:
                current_answer = 'Philosoraptor'

        elif "What" in question_list:
            if "Royal" in question_list:
                current_answer = 'The Krokonomicon'
            elif "rank" in question_list:
                current_answer = 'Damage + DoT'
            elif "Ribbon" in question_list:
                current_answer = 'Time Flux'
            elif "Lady" in question_list:
                current_answer = 'Trick question, she has a sword.'
            elif "Professor" in question_list:
                current_answer = 'Pasta Arrabiata'
            elif "determines" in question_list:
                current_answer = 'Where they come from and their school of focus.'
            elif "secret" in question_list:
                current_answer = 'Order of the Fang'
            elif "Gurtok" in question_list:
                current_answer = 'Balance'
            elif "unique" in question_list:
                current_answer = 'There are scorch marks on the ceiling'
            elif "dance" in question_list:
                current_answer = 'The bee dance'
            elif "Dark" in question_list:
                current_answer = 'Shadow'
      
        elif "match" in question_list:
            current_answer = '5 minutes'
        
        elif "Shaka" in question_list:
            current_answer = 'The Greatest Living Zebra Warrior'

        elif "unmodified" in question_list:
            current_answer = "900 � 1000 Fire Damage + 300 Fire Damage to entire team"

        elif "Ravens" in question_list:
            current_answer = 'The Everwinter, to cover the world in ice:'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_conjuring(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Council" in question_list:
                current_answer = 'Cyrus Drake'
            elif "King" in question_list:
                current_answer = 'Pyat MourningSword'
            elif "Bill" in question_list:
                current_answer = 'Sarah Tanner'

        elif "What" in question_list:
            if "Flameright" in question_list:
                current_answer = 'Advanced Flameology'
            elif "weather" in question_list:
                current_answer = 'Half moon/moon'
            elif "Dolittle" in question_list:
                current_answer = "Genuine Imitation Golden Ruby"
            elif "Grendel" in question_list:
                current_answer = 'Thulinn'
            elif "Dragonspyre" in question_list:
                current_answer = '33'

        elif "How" in question_list:
            current_answer = 'Three'
        
        elif "Which" in question_list:
            current_answer = 'Ellen'

        elif "Destreza" in question_list:
            current_answer = 'A Gorgon'

        elif "Kirby" in question_list:
            current_answer = 'Death'

        elif "Halley" in question_list:
            current_answer = 'Aztecosaurologist'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_magical(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "prophesizes" in question_list:
                current_answer = 'Morganthe'
            elif "Registrar" in question_list:
                current_answer = 'Mrs. Dowager'
            elif "sells" in question_list:
                current_answer = 'Valentina Heartsong'
            elif "Nameless" in question_list:
                current_answer = 'Sir Malory'
            elif "guards" in question_list:
                current_answer = 'Private Stillson'

        elif "What" in question_list:
            if "color" in question_list:
                current_answer = 'Red'
            elif "diminish" in question_list:
                current_answer = 'Flame Gems'
            elif "pink" in question_list:
                current_answer = 'Heart'
            elif "lose" in question_list:
                current_answer = 'Blue Oysters'
            elif "floating" in question_list:
                current_answer = 'Basic Wizarding & Proper Care of Familiars'
            elif "library" in question_list:
                current_answer = 'Book on the Wumpus'

        elif "How" in question_list:
            current_answer = '12'
        
        elif "Which" in question_list:
            if "battle" in question_list:
                current_answer = 'Wand'
            elif "Oni" in question_list:
                current_answer = 'Ruby'
            elif "locations" in question_list:
                current_answer = 'Digmore Station'
            elif "standing" in question_list:
                current_answer = "Fire"

        elif "Why" in question_list:
            if "afraid" in question_list:
                current_answer = 'Witches'
            elif "pixies" in question_list:
                current_answer = 'Rattlebones corrupted them'

        elif "Zafaria" in question_list:
            current_answer = 'Gorillas, Zebras, Lions'

        elif "balance" in question_list:
            current_answer = 'Niles'

        elif "originally" in question_list:
            current_answer = 'Avalon'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_marleybone(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "criminal" in question_list:
                current_answer = 'Meowiarty'
            elif "officer" in question_list:
                current_answer = 'Officer Digmore'

        elif "What" in question_list:
            if "Herold" in question_list:
                current_answer = 'Ancient Myths for Parliament'
            elif "lose" in question_list:
                current_answer = 'The Stray Cats'
            elif "initials" in question_list:
                current_answer = 'XX'
            elif "common" in question_list:
                current_answer = "O'Leary"
            elif "transports" in question_list:
                current_answer = 'Hot Air Balloons'
            elif "flying" in question_list:
                current_answer = 'Newspapers'
            elif "beverage" in question_list:
                current_answer = 'Root Beer'
            elif "Major" in question_list:
                current_answer = 'Sylvester Quimby Talbot III'
            elif "day" in question_list:
                current_answer = 'Night'
            elif "artifacts" in question_list:
                current_answer = 'Krokotopian'
            elif "Statues" in question_list:
                current_answer = 'Saint Bernard and Saint Hubert'
            elif "clock" in question_list:
                current_answer = '1:55'
            elif "Abigail" in question_list:
                current_answer = "Policeman's Ball"
            elif "color" in question_list: 
                current_answer = 'Red'

        elif "How" in question_list:
            current_answer = 'Three'
        
        elif "Which" in question_list:
            if "street" in question_list:
                current_answer = 'Fleabitten Ave'
            elif "folks" in question_list:
                current_answer = 'Clancy Pembroke'
            elif "stained" in question_list:
                current_answer = 'A Tennis Ball'

        elif "Arthur" in question_list:
            current_answer = 'Dog'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_mystical(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "tells" in question_list:
                current_answer = 'Harold Argleston'
            elif "Tomb" in question_list:
                current_answer = "Hetch Al'Dim"
            elif "permission" in question_list:
                current_answer = 'Sergent Major Talbot'
            elif "River" in question_list:
                current_answer = 'Charon'
            elif "Gladiator" in question_list:
                current_answer = 'Dimachaerus'  
            elif "Emperor" in question_list:
                current_answer = 'Noboru Akitame'
            elif "asks" in question_list:
                current_answer = 'Eloise Merryweather'
            elif "Falynn" in question_list:
                current_answer = 'Sir Malick de Logres'
            elif "haunts" in question_list:
                current_answer = 'Nosferabbit'
            elif "guard" in question_list:
                current_answer = 'The Knights of the Silver Rose'

        elif "What" in question_list:
            if "travel" in question_list:
                current_answer = 'Ice Archway'
            elif "Ponce" in question_list:
                current_answer = 'The Water of Life'

        elif "Which" in question_list:
            current_answer = "Jaques the Scatcher"

        elif "Where" in question_list:
            current_answer = 'Wizard City'

        elif "Zenzen" in question_list:
            current_answer = 'Grandfather'
        
        elif "Axaya" in question_list:
            current_answer = 'The Badge of Leadership'
        
        elif "Hrundle" in question_list:
            current_answer = 'Wintertusk'
        
        elif "Professor" in question_list:
            current_answer = 'Telegraph Box'

        elif "Pigswick" in question_list: ######################################## BROKEN #########################################
            current_answer = "Equilibrium"
        
        elif "Spider" in question_list:
            current_answer = 'Zafaria'


        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_spellbinding(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Horn" in question_list:
                current_answer = 'Belloq'
            elif "precious" in question_list:
                current_answer = 'Takeda Kanryu'
            elif "pain" in question_list:
                current_answer = 'Aiuchi'
            elif "Gorgon" in question_list:
                current_answer = 'Phorcys'
            elif "shield" in question_list:
                current_answer = 'Mavra Flamewing'
            elif "Haraku" in question_list:
                current_answer = 'Binh Hoa'
            elif "first" in question_list:
                current_answer = 'Sophia DarkSide'
            elif "harpsicord" in question_list:
                current_answer = 'Gretta Darkkettle'
            elif "oughta" in question_list:
                current_answer = 'Mugsy'
            elif "healing" in question_list:
                current_answer = 'Binh Hoa'
            elif "broken," in question_list:
                current_answer = 'Clanker'
            elif "Korio" in question_list:
                current_answer = 'Priya the Dryad'

        elif "What" in question_list:
            if "badge" in question_list:
                current_answer = 'Yojimbo'
            elif "plant" in question_list:
                current_answer = 'Cultivated Woodsmen'
            elif "Silenus" in question_list:
                current_answer = 'Glorious Golden Archon'
        
        elif "Where" in question_list:
            current_answer = "Skythorn Tower"

        elif "twice" in question_list:
            current_answer = 'Shrubberies'

        elif "Horned" in question_list:
            current_answer = 'Gisela'
        
        elif "Swallows" in question_list:
            current_answer = 'Zafaria and Marleybone'

        elif "enlisted" in question_list:
            current_answer = 'The Black Sun Necromancers'


        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_spells(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "balance" in question_list:
                current_answer = 'Alhazred'
            if "Life" in question_list:
                current_answer = 'Sabrina Greenstar'

        elif "What" in question_list:
            if "Star" in question_list:
                current_answer = 'Auras'
            elif "Sun" in question_list:
                current_answer = 'Enchantment'
            elif "Ice," in question_list:
                current_answer = 'Elemental'
            elif "Enya" in question_list:
                current_answer = '80'
            elif "isn't" in question_list:
                current_answer = 'Ebon Ribbons'
            elif "Forsaken" in question_list:
                current_answer = '375 damage plus a hex trap'
            
        elif "How" in question_list:
            if "Von's" in question_list:
                current_answer = '9'
            elif "Stormzilla?" in question_list:
                current_answer = '5'
        
        elif "Which" in question_list:
            if "polymorphed" in question_list:
                current_answer = 'Pie in the sky'
            elif "vitae" in question_list:
                current_answer = 'Entangle'
            elif "over" in question_list:
                current_answer = 'Power Link'
        
        elif "If" in question_list:
            if "Tempest" in question_list:
                current_answer = 'Ptera'
            elif "supercharge" in question_list:
                current_answer = '110%'

        elif "Mildred" in question_list:
            current_answer = 'Dispels'

        elif "Cassie" in question_list:
            current_answer = 'Prism'

        elif "Mortis" in question_list:
            current_answer = 'Tranquilize'

        elif "specializes" in question_list:
            current_answer = 'Minions'

        elif "Ether" in question_list:
            current_answer = 'Life and Death attacks'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_city(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "sang" in question_list:
                current_answer = 'Bartleby'
            elif "mill" in question_list:
                current_answer = 'Sohomer Sunblade'
            elif "Life" in question_list:
                current_answer = 'Sylvia Drake'
            elif "Fire" in question_list:
                current_answer = 'Dalia Falmea'
            elif "Princess" in question_list:
                current_answer = 'Lady Oriel'
            elif "resides" in question_list:
                current_answer = 'Lady Oriel'

        elif "What" in question_list:
            if "Tallstaff" in question_list:
                current_answer = 'Ravenwood Bulletin'
            elif "bridge" in question_list:
                current_answer = 'Rainbow Bridge'
            elif "school" in question_list and "colors" in question_list:
                current_answer = 'Tan and Maroon'
            elif "Tree" in question_list:
                current_answer = 'Kelvin'
            elif "Myth" in question_list:
                current_answer = 'Blue and Gold'
            elif "Creativity?" in question_list:
                current_answer = 'Storm'
            elif "grandfather" in question_list:
                current_answer = 'Bartleby'
            elif "Fodder" in question_list:
                current_answer = 'A spade'
            elif "stockpiling" in question_list:
                current_answer = 'Broccoli'
            elif "Gemstone" in question_list:
                current_answer = 'Citrine'
            elif "Malorn" in question_list:
                current_answer = 'Death'
            elif "Colossus" in question_list:
                current_answer = 'Pixiecrown'
            elif "full" in question_list:
                current_answer = 'Diego Santiago Quariquez Ramirez the Third'
        
        elif "Where" in question_list:
            current_answer = 'Fairegrounds'

        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


def run_w101_zafaria(driver, trivia_url):

    trivia = driver.find_element(By.XPATH, '//a[@href="{}"]'.format(trivia_url))
    driver.execute_script("arguments[0].click();", trivia)

    current_answer = ''
    for i in range(0, 13):
        question = driver.find_element(By.CLASS_NAME, "quizQuestion")
        question_list = question.text.split()
        
        answers = driver.find_elements(By.CLASS_NAME, "answerText")
        buttons = driver.find_elements(By.NAME, "checkboxtag")
        answer_dict = {}
        for i in range(0, 4):
            answer_dict[answers[i].text] = buttons[i]

        if "Who" in question_list:
            if "Hannibal" in question_list:
                current_answer = 'Mago and Sobaka'
            elif "missing" in question_list:
                current_answer = 'Tiziri Silvertusk'
            elif "Zebu" in question_list:
                current_answer = 'Zaffe Zoffer'

        elif "What" in question_list:
            current_answer = 'You never can tell with them!'
        
        elif "Goodheart" in question_list:
            current_answer = 'Rasik Pridefall'

        elif "Reginal" in question_list:
            current_answer = 'Mondli Greenhoof'

        elif "legendary" in question_list:
            current_answer = 'The Sword of the Duelist'

        elif "Jambo" in question_list:
            current_answer = 'Hello.'

        elif "Baobab" in question_list:
            current_answer = 'A Council of three councilors'
        
        elif "assassin" in question_list:
            current_answer = 'Karl the Jackal'
        
        elif "Esop" in question_list:
            current_answer = 'Djembe Drum'
        
        elif "Unathi" in question_list:
            current_answer = 'A councilor of Baobab'
        
        elif "Ravagers" in question_list:
            current_answer = 'Nergal the Burned Lion'
        
        elif "local" in question_list:
            current_answer = 'Msizi Redband'
        
        elif "Rasik" in question_list:
            current_answer = 'An Olyphant from Stone Town.'
        
        elif "Bandits" in question_list:
            current_answer = 'Baobab Market'

        elif "Koyate" in question_list:
            current_answer = 'Being a thief'
        
        elif "Inyanga" in question_list:
            current_answer = 'Fire feather'
        
        elif "Belloq" in question_list:
            current_answer = 'The Sook'


        if current_answer in answer_dict:
            driver.execute_script("arguments[0].click();", answer_dict[current_answer])

        time.sleep(1)

        # Click next
        next = driver.find_element(By.ID, "nextQuestion")
        driver.execute_script("arguments[0].click();", next)

        time.sleep(5)

    quiz_completion(driver)
    return 0


main()
