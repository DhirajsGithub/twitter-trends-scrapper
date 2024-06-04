from django.urls import path
from .views import run_selenium_script, list_trending_topics, scrape_trends_page

urlpatterns = [
    path('run-script/', run_selenium_script, name='run_selenium_script'),
    path('list-topics/', list_trending_topics, name='list_trending_topics'),
    path('', scrape_trends_page, name='scrape_trends_page'),
]