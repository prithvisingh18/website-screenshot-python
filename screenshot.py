from selenium import webdriver
from PIL import Image

driver_ = './chromedriver'
driver = webdriver.Chrome(driver_)

path = ''
path = input()
check = path.split('www')
print(check[0])
if(str(check[0]) != 'https://'):
    path = 'https://' + path 
driver.get(path)
screenshot = driver.save_screenshot('screenshot.png')
img = Image.open('screenshot.png')
img = img.resize((1024,768))
img.save("resized_screenshot.png")



