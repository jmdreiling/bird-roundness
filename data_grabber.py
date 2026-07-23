import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

## Cobbled together little image scraper that grabs Hugh's bird images
## Initially tried to use the Cloudflare API but found that I need some level of authentication.
## Or at least I think so? ¯\_(ツ)_/¯ 

## This is the old bits I was using to try and access it using the cloudflare method.
## Keeping around in case it ends up useful
# ACCOUNT_HASH= "VHUFY-rex3e4Q_VyKYqYcw"
# IMAGE_ID = "148d027f-2201-4199-3791-83dd0b07fc00"
# VARIANT_NAME = "public"


link = "https://bird-upload-api.hugh-evans-dev.workers.dev/gallery"


## Starts with code from https://brightdata.com/blog/how-tos/scrape-images-from-websites

# to run Chrome in headless mode
options = Options()
options.add_argument("--headless")

# initialize a Chrome WerbDriver instance
# with the specified options
driver = webdriver.Chrome(
    service=ChromeService(),
    options=options
)

# to avoid issues with responsive content
driver.maximize_window()

# the URL of the target page
# visit the target page in the controlled browser
driver.get(link)

## Grab what images you can
image_html_nodes = driver.find_elements(By.TAG_NAME, value ="img")

SCROLL_PAUSE_TIME = 2 #How long to wait between scrolls

## Scroll until you reach the total number of images, I know this is 3038
## Could generate the 3038 dynamically but I'm fine with jankiness for now.
## Scroll code yoinked from: https://stackoverflow.com/questions/77790368/scraping-lazy-loading-images-with-selenium
## Specifically the answer by Clg9100
while len(image_html_nodes) < 3038: ## stop when you hit the number of total images
    driver.execute_script('window.scrollBy( 0, 4000 )' ) #Alternative scroll, a bit slower but reliable - increased from 400 to 4000 for more scrollll
    sleep(SCROLL_PAUSE_TIME) #Give images a bit of time to load by waiting
    image_html_nodes = driver.find_elements(By.TAG_NAME, value ="img") ## Grab the images that you see
    print(len(image_html_nodes)) ## print how many images you've gotten

## We return here to the bright data code.
image_urls =[]
for image_html_node in image_html_nodes:
  try:
    # use the URL in the "src" as the default behavior
    image_url = image_html_node.get_attribute("src")
    image_urls.append(image_url)
  except StaleElementReferenceException as e:
    continue
## Print your total number of URLS (this should be 3038)
print(len(image_urls))

image_name_counter = 1

# # download each image and add it
# # to the "/images" local folder
for image_url in image_urls:
    img_data = requests.get(image_url).content
    with open(f'./images/{image_url.split('/')[4]}.jpg', 'wb') as handler:
        handler.write(img_data)
    image_name_counter += 1
    ## kinda of useless but I don't feel like adding a loading bar so I'm going to just 
    ## blast my terminal with output text.
    print(f"saved {image_name_counter}th image")

## kill the selenium driver
driver.quit()