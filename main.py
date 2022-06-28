from selenium.webdriver import Firefox
import json
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def read_credentials(file_path):
    return json.load(open(file_path))

def main():
    #Setup Firefox Headless Browser
    options = Options()
    options.headless = True
    browser = Firefox(options=options)

    #Get the NoIp Login Page
    browser.get('https://www.noip.com/login')
    if "Sign In" not in browser.title:
        print("Browser can't find Login Page")
        return

    #Read credentials file
    credentials = read_credentials("credentials.json")

    #Login To No-IP
    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")
    username.send_keys(credentials['username'])
    password.send_keys(credentials['password'])
    browser.find_element(By.ID, "clogs-captcha-button").click()

    if "My No-IP" not in browser.title:
        print("Login Failed")
        return
    else:
        print("Login Succ")

    #Move To Hostname Page
    browser.get('https://my.noip.com/dynamic-dns')

    #Find Buttons 
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-labeled.btn-success")

    #If Button Contains "Confirm" Then click
    for button in buttons:
        inner_html = button.get_property("textContent")
        if "Confirm" in inner_html:
            print("Domain needs confirming")
            button.click()

    #Quits Browser
    browser.quit()

if __name__ == "__main__":
    main()
