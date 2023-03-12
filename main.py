# Import libraries and packages for the project
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import csv




# 2: Search for the profile we want to crawl


def returnProfileInfo(user_url):
    print('- imported packages')

    # user_url = 'https://www.linkedin.com/in/alexander-lonstein-b84a6069/'

    # Login to Linkedin

    # Open Chrome and Access Linkedin login site
    # option = webdriver.ChromeOptions()
    # # 添加启动选项，指定为无界面模式
    # option.add_argument('--headless')
    # driver = webdriver.Chrome(options=option)
    driver = webdriver.Chrome()
    sleep(2)
    url = 'https://www.linkedin.com/login'
    driver.get(url)
    sleep(2)
    url = 'https://www.linkedin.com/login'
    driver.get(url)
    print('- initialized a driver')
    sleep(2)

    # Task 1.2: Import username and password
    credential = open('login.txt')
    line = credential.readlines()

    email = line[0]
    password = line[1]
    print('- imported the login credentials')
    sleep(2)

    eml = driver.find_element(by=By.ID, value="username")
    eml.send_keys(email)
    passwd = driver.find_element(by=By.ID, value="password")
    passwd.send_keys(password)
    loginbutton = driver.find_element(by=By.XPATH, value="//*[@id=\"organic-div\"]/form/div[3]/button")
    loginbutton.click()
    sleep(40)

    print('- Login Linkedin success')

    url_ex = user_url
    driver.get(url_ex)
    sleep(2)
    source = BeautifulSoup(driver.page_source, "html.parser")

    profile = {}
    info = source.find('div', class_='mt2 relative')
    name = info.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words').get_text().strip()
    title = info.find('div', class_='text-body-medium break-words').get_text().lstrip().strip()
    location = info.find('span', class_='text-body-small inline t-black--light break-words').get_text().lstrip().strip()

    about_section = source.find('div', class_='display-flex ph5 pv3')
    about = about_section.find('div',
                               class_='pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center').get_text().lstrip().strip()
    profile['Name'] = name
    profile['Title'] = title
    profile['Location'] = location
    profile['About'] = about
    sleep(1)
    #get experiences
    url_ex = driver.current_url + '/details/experience/'
    driver.get(url_ex)
    sleep(12)
    source = BeautifulSoup(driver.page_source, "html.parser")
    sleep(11)
    exp = source.find_all('li')
    allExperiences = ''
    for e in exp[14:-23]:
        row = e.getText().lstrip().strip()
        allExperiences += row
    print(allExperiences)
    profile['Experiences'] = allExperiences

    #get educations
    url_ex = user_url
    driver.get(url_ex)
    sleep(12)
    source = BeautifulSoup(driver.page_source, "html.parser")
    sleep(11)
    edu = source.find_all('div', class_="display-flex flex-column full-width align-self-center")
    # get educations
    allEducations = ''
    for e in edu[:]:
        row = e.getText().lstrip().strip()
        if ("Bachelor's" in row) or ("Doctor" in row and 'School' in row) or ("Doctor" in row and 'University' in row) or ("Doctor's" in row) or ("BA" in row) or ("Bachelor" in row) or ("BS" in row) or ("PHD" in row) or ("MD" in row) or ("Doctor of" in row):
            allEducations += row
    print(('Educations', allEducations))
    profile['Educations'] = allEducations
    # get recommendations
    allRecommendations = ''
    for e in edu[:]:
        row = e.getText().lstrip().strip()
        if "I" in row:
            allRecommendations += row
    print(allRecommendations)
    profile['Recommendations'] = allRecommendations
    return profile


# if __name__ == "__main__":
#     profile = returnProfileInfo(user_url)
#     print(profile)
#     with open('profile.csv', mode='w') as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             ['Full Name', 'Title', 'Location', 'About', 'Experiences', 'Education', 'Recommendations'])
#         writer.writerow(profile)
#     print(f'- Profile has been saved to profile.csv')
#     driver.quit()

# if __name__ == "__main__":
    # profile = returnProfileInfo(user_url)
    # print(json.dumps(profile, indent=4))

    # with open('profile.json', 'w') as f:
    #     f.write(json.dumps(profile, indent=4))
    # print(f'- Profile has been saved to profile.json')
    # driver.quit()
