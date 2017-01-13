
'''
Letargia

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, url):
    driver.get(url)
    try:
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,".EESPNGB-J-e")))
        i=0
        while i < 15:
            button.click()
            time.sleep(1)
            i+=1
            try:
                resultado = info_extractor(driver)
                print(resultado)
            except:
                print("Ya no hay mas vuelos.")
                break
    except TimeoutException:
        print("Button not found.")



def info_extractor(driver):
    countryName = driver.find_elements_by_css_selector(".EESPNGB-K-P > a:nth-child(1)")[0].text
    flightInfo = driver.find_elements_by_css_selector("div.EESPNGB-K-q:nth-child(1) > div:nth-child(1) > div:nth-child(2)")[0].text
    price = driver.find_elements_by_css_selector("div.EESPNGB-K-q:nth-child(1) > div:nth-child(1) > div:nth-child(3)")[0].text
    resultado = [countryName,flightInfo,price]
    return resultado



if __name__ == "__main__":
    aeropuerto = input("Introduce el aeropuerto de salida: ")
    fecha = input("Introduce la fecha de salida (formato AAAA/MM/DD): ")
    urlDef = "https://www.google.es/flights/#search;f="+aeropuerto+";d="+fecha+";tt=o;mp=50;mc=m"
    driver = init_driver()
    lookup(driver, urlDef)
    time.sleep(1)
    driver.quit()