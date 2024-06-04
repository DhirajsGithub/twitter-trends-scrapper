from django.shortcuts import render
from django.http import JsonResponse
from .models import TrendingTopic
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import random
from selenium.webdriver.firefox.options import Options

proxies = [
    "45.32.86.6:31280",
    "45.32.231.36:31280",
    "199.247.13.177:31280",
    "198.13.59.209:31280",
    "207.148.86.251:31280",
    "138.68.111.53:31280",
    "128.199.116.150:31280",
    "45.63.75.212:31280",
    "216.173.113.135:31280",
    "191.96.166.60:31280",
    "192.154.248.231:31280",
    "46.101.40.23:31280",
    "31.171.246.26:31280",
]

def get_random_proxy():
    return random.choice(proxies)

def run_selenium_script(request):
    unique_id = str(uuid.uuid4())
    proxy_address = get_random_proxy()
    options = Options()
    options.headless = False
    options.add_argument('--proxy-server=%s' % proxy_address)
    driver = webdriver.Firefox(options=options)

	
    driver.implicitly_wait(10)

    try:
        url = "https://x.com/explore/tabs/for-you"
        driver.get(url)
        
        login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a")
        login_btn.click()

        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys("DhirajBorse13")
        username_input.send_keys(Keys.ENTER)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("twitter.in")
        password_input.send_keys(Keys.ENTER)

        trend1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[4]/div/div/div/div/div[2]")
        trend2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[5]/div/div/div/div/div[2]")
        trend3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[6]/div/div/div/div/div[2]")
        trend4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[7]/div/div/div/div/div[2]")
        trend5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[8]/div/div/div/div/div[2]")

        TrendingTopic.objects.create(
            unique_id=unique_id,
            trend1=trend1.text,
            trend2=trend2.text,
            trend3=trend3.text,
            trend4=trend4.text,
            trend5=trend5.text,
            date_time=datetime.now(),
            ip_address=proxy_address
        )

        result = {
            'unique_id': unique_id,
            'trends': {
                'trend1': trend1.text,
                'trend2': trend2.text,
                'trend3': trend3.text,
                'trend4': trend4.text,
                'trend5': trend5.text
            },
            'date_time': datetime.now(),
            'ip_address': proxy_address
        }

    except (TimeoutException, NoSuchElementException, WebDriverException) as e:
        result = {
            'error': str(e),
            'unique_id': unique_id,
            'date_time': datetime.now(),
            'ip_address': proxy_address
        }

    finally:
        driver.quit()

    return JsonResponse(result)

def list_trending_topics(request):
    trending_topics = list(TrendingTopic.objects.all().values())
    return JsonResponse(trending_topics, safe=False)

def scrape_trends_page(request):
    return render(request, 'scraper/scraper_trends.html')