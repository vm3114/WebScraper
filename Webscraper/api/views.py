from rest_framework.response import Response
from rest_framework.decorators import api_view
from selenium import webdriver
from selenium.webdriver.common.by import By


@api_view(['GET'])
def getData(request):

    driver = webdriver.Chrome()
    url = 'https://www.nvidia.com/en-in/geforce/buy/'
    driver.get(url)
    empty_indexes = [2, 3, 4]

    gpu_list = []
    price_list = []

    gpus = driver.find_elements(By.CSS_SELECTOR, 'h3.title')
    prices = driver.find_elements(By.CLASS_NAME, 'startingprice')

    for gpu in gpus:
        gpu_name = gpu.text.strip()
        if gpu_name.startswith('Starting at'):
            pass
        else:
            gpu_list.append(gpu_name)

    for index, element in enumerate(prices):
        text = element.text.strip()
        if index in empty_indexes:
            price_list.append("N/A")
            
        starting_price = text.strip().replace('Starting at Rs. ', '').replace(',', '')
        price_list.append(int(starting_price))

    driver.quit()

    output = {}
    for i in range(len(gpu_list)):
        output[gpu_list[i]] = price_list[i]

    return Response(output)
