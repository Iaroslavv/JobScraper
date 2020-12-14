import requests
from bs4 import BeautifulSoup
from datetime import date
import csv


class Indeed:
    """Extracts job's data from indeed."""

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
            write.writerow(["Job Title", "Url", "Company", "Location",
                            "Summary", "Date post", "Date", "Salary"])
            write.writerows(records)
        return records


class StackOver:
    """Extracts job's data from stackoverflow."""

    @staticmethod
    def get_record(card):
        atag = card.h2.a
        title = atag.get("title")
        job_url = "https://ru.indeed.com/" + atag.get("href")
        company_name = card.find("span", "").text.strip()
        job_location = card.find("span", "fc-black-500").text.strip()
        tech_info = card.find("div", "ps-relative").text
        date_today = date.today().strftime("%Y-%m-%d")
        date_post = " ".join(card.find("ul", "mt4").text.split()[:2])
        try:
            salary = " ".join(card.find("ul", "mt4").text.split()[5])
        except IndexError:
            salary = ""

        record = (title, job_url, company_name, job_location,
                tech_info, date_post, date_today, salary)

        return record

    @staticmethod
    def get_records(position, location):
        url = f"https://stackoverflow.com/jobs?q={position}&l={location}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", class_="-job")
        records = []
        for card in cards:
            record = StackOver.get_record(card)
            records.append(record)
        with open("jobs_stackover.csv", "w", newline="", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerow(["Job title", "Url", "Company", "Location",
                            "Tech Info", "Date post", "Date", "Salary/Kind of work"])
            write.writerows(records)
        return records
