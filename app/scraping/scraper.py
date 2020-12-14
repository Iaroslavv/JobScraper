import requests
from bs4 import BeautifulSoup
from datetime import date
import csv

class Indeed:
    """Extrts job's data from indeed."""

    @staticmethod
    def get_record(card):
        atag = card.h2.a
        job_title = atag.get("title")
        job_url = "https://ru.indeed.com" + atag.get("href")
        company_name = card.find("span", "company").text.strip()
        location = card.find("div", "recJobLoc").get("data-rc-loc")
        summary = card.find("div", "summary").text.strip()
        date_post = card.find("span", "date").text.strip()
        today_date = date.today().strftime("%Y-%m-%d")
        try:
            salary = card.find("span", "salaryText").text.strip()
        except AttributeError:
            salary = ""
        record = (job_title, job_url, company_name, location, summary,
                  date_post, today_date, salary)
        return record

    @staticmethod
    def get_records(position, location):
        url = f"https://ru.indeed.com/jobs?q={position}&l={location}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="jobsearch-SerpJobCard")
        records = []
        for card in cards:
            record = Indeed.get_record(card)
            records.append(record)
        with open("jobs_indeed.csv", "w", newline="", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerow(["Job title", "Url", "Company", "Location",
                            "Summary", "Date post", "Date", "Salary"])
            write.writerows(records)
        return records



def find_url(position, location):
    url = f"https://stackoverflow.com/jobs?q={position}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="-job")
    card = cards[0]
    atag = card.h2.a
    title = atag.get("title")
    job_url = "https://ru.indeed.com/" + atag.get("href")
    company_name = card.find("span", "").text.strip()
    job_location = card.find("span", "fc-black-500").text.strip()
    tech_info = card.find("div", "ps-relative")
    technologies = tech_info.find("a", "post-tag").text
    return technologies
print(find_url("python junior", "europe"))
