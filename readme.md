# Project Description
As I tend sometimes to visit some job search websites like Indeed, Stack Over Flow and others, I've come up with an idea of automating the process of getting updates of new vacancies from these websites.
The frontend part is very simple. There is a start page where you're suggested to input a position and a location, then select the website which will be used as a source of vacancy updates. Press the button 'apply' and you'll see an html formatted table with company name, job title, url, location, summary, post date and a salary.

## Installation
```bash
git clone https://github.com/Iaroslavv/JobScraper.git
pip install -r requirements.txt
```

## What I've learned
- The basics of [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Tablib](https://tablib.readthedocs.io/en/stable/) to convert csv table to html one
