from bs4 import BeautifulSoup
import requests
import json
import csv


def write_to_csv(job_list):
    try:
        with open("job_lists.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            header = [
                "company",
                "job",
                "required_experience",
                "location",
                "key_skills",
                "description",
            ]
            writer.writerow(header)
            for i in range(1, (len(job_lists) + 1)):
                new_row = []
                new_row.append(job_lists[i]["company"])
                new_row.append(job_lists[i]["job"])
                new_row.append(job_lists[i]["required_experience"])
                new_row.append(job_lists[i]["location"])
                new_row.append(job_lists[i]["key_skills"])
                new_row.append(job_lists[i]["description"])
                writer.writerow(new_row)
    except Exception as e:
        print(f"Error :{e}")


job_lists = {}


def get_desc(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    desc = soup.find("div", class_="jd-sec")

    desc_divs = desc.find_all(
        "div", class_=["jd-desc", "job-description-main", "job-basic-info"]
    )
    desc_text = ""
    string = desc_divs[0].get_text(separator="\n", strip=True)
    desc_text += string + "\n"
    for div in desc_divs:
        for li_tags in div.select("div.job-basic-info li.clearfix"):
            desc_text += li_tags.get_text(separator=" ", strip=True) + "\n"

    return desc_text


html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
).text

soup = BeautifulSoup(html_text, "lxml")

ul = soup.find("ul", class_="new-joblist")

jobs = ul.find_all("li", class_="clearfix job-bx wht-shd-bx")

i = 1

for job in jobs:
    job_dict = {}
    job_dict["company"] = job.find("h3", class_="joblist-comp-name").text.strip()
    print(job_dict["company"])
    job_dict["job"] = job.find("h2").a.text.strip()
    job_dict["url"] = job.a["href"]
    job_dict["description"] = get_desc(job_dict["url"])
    job_dict["required_experience"] = job.select("ul.top-jd-dtl li")[0].find(
        string=True, recursive=False
    )
    job_dict["location"] = job.select("ul.top-jd-dtl li span")[0].find(
        string=True, recursive=False
    )
    skill = (
        job.select("ul.list-job-dtl li span.srp-skills")[0]
        .get_text(separator=" ", strip=True)
        .split(" , ")
    )
    key_skill = ", ".join(skill)
    job_dict["key_skills"] = key_skill
    job_lists[i] = job_dict
    i += 1

json_obj = json.dumps(job_lists, indent=4)

with open("temp.json", "w") as j:
    j.write(json_obj)
    j.close()

write_to_csv(job_lists)