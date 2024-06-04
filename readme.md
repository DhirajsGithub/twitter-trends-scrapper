# Twitter Trends Scraper

This application scrapes trending topics from Twitter using Selenium and displays them on a web page. It uses Django for the web framework and Selenium for web scraping.

## Features

- Scrape the top 5 trending topics from Twitter.
- Display the trends along with the date and the IP address used for scraping.
- Use proxies to avoid being blocked by Twitter.
- Display a loading indicator while scraping is in progress.
- Stores the scraped trends in a database for future reference.

## Setup

### Prerequisites

- Python 3.7+
- Django 3.2+
- Selenium 4.0+
- Geckodriver
- Firefox browser

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/DhirajsGithub/twitter-trends-scrapper.git
    cd twitter-trends-scraper
    ```

2. **Create and activate a virtual environment**

    ```bash
    # mac/linux
    python3 -m venv venv
    source venv/bin/activate  

    # On Windows, use 
    `venv\Scripts\activate`
    ```

3. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download and setup Geckodriver**

    - Download Firefox from the [official site](https://www.mozilla.org/en-US/firefox/new/).
    - Download Geckodriver from the [official site](https://github.com/mozilla/geckodriver/releases).
    - Extract the downloaded file and move it to a directory included in your system's PATH, or specify the path in your Selenium code.
    - for mac : 
    - move the geckodriver to /usr/local/bin use
    - ```sudo mv geckodriver_path /usr/local/bin```
    - for windows :
    - move the geckodriver to C:\Windows\System32
    - as ```move geckodriver_path C:\Windows\System32```


### Running the Application

1. **Start the Django development server**

    ```bash
    cd twitter-trends-scraper
    cd scrapping
    python manage.py runserver
    ```

2. **Access the application**

    Open your web browser and go to `http://127.0.0.1:8000/` to view the scraping interface.

### Usage

- Click the "Run Scrape Script" button to start scraping Twitter trends.
- A loading indicator will appear while the scraping is in progress.
- The top 5 trending topics will be displayed along with the date and the IP address used for scraping.

### Project Structure

- `scraper/`: Contains the Django app for scraping and displaying trends.
  - `views.py`: Contains the logic for scraping Twitter trends using Selenium.
  - `urls.py`: Defines the URL routes for the scraping and listing views.
  - `models.py`: Defines the `TrendingTopic` model for storing scraped trends.
  - `templates/scraper/scraper_trends.html`: The HTML template for the scraping interface.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: Lists the dependencies required for the project.

