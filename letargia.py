import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    '''This function initialize the webdriver'''
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, airport, date):
    '''This function search for flights and call info_extractor(driver) to get info.
    Parameters: airpot (string, example: "PMI"), date (string, example "29 de Marzo").
    It returns the flighList (multi-dimensional vector).'''
    url = "https://www.google.es/flights/#search;f="+airport+";tt=o;mp=50;mc=m"
    driver.get(url)
    try:
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,".EESPNGB-J-e")))
        box = driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.EESPNGB-G-l:nth-child(1)")))
        box.click()
        box.send_keys(date)
        flightList = []
        i=0
        while i < 15:
            button.click()
            time.sleep(3)
            i+=1
            result = info_extractor(driver)
            flightList.append(result)
        return flightList
    except TimeoutException:
        print("Button not found.")



def info_extractor(driver):
    '''This function get flights from the website. Returns The result (3 dimensional string vector).'''
    countryName = driver.find_elements_by_css_selector(".EESPNGB-K-P > a:nth-child(1)")[0].text
    flightInfo = driver.find_elements_by_css_selector("div.EESPNGB-K-q:nth-child(1) > div:nth-child(1) > div:nth-child(2)")[0].text
    price = driver.find_elements_by_css_selector("div.EESPNGB-K-q:nth-child(1) > div:nth-child(1) > div:nth-child(3)")[0].text
    result = [countryName,flightInfo,price]
    return result


def list_corrector(flightList):
    '''This function transform the flight list in a new list which only has unique values'''
    newFlightList = []
    for flight in flightList:
        if flight not in newFlightList:
            newFlightList.append(flight)
    return newFlightList



def priceListGenerator(newFlightList):
    '''This function get best prices and return the flightlist in order from the chepeast.'''
    priceList = []
    for flight in newFlightList:
        if flight[2] != "":
            price = flight[2]
            priceList.append(int(price[:-2]))
        else:
            pass
    bestPriceList = [x for (y,x) in sorted(zip(priceList,newFlightList))]
    return bestPriceList




if __name__ == "__main__":
    airport = input("Introduce el aeropuerto de salida: ")
    date = input("Introduce la fecha de salida (formato '29 de Marzo'): ")
    driver = init_driver()
    flightList = lookup(driver, airport, date)
    correctList = list_corrector(flightList)
    bestPriceList = priceListGenerator(correctList)
    print("\nEstos son los vuelos más baratos desde tu aeropuerto de salida: ")
    for flight in bestPriceList: 
        print(flight)
    driver.quit()
