from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests,csv,time
from random import randint


output_file_path = "../data/output.csv"
website = "https://hackr.io/blog/tag/courses"
csv_header = [
    "course_title",
    "course_tag",
    "author",
    "course_date",
    "course_link",
    "article_content_first_4_graph"
]


def write_csv_header(file_path, csv_header):
    with open(file_path,"w",newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(csv_header)

def write_csv_content(file_path, *args):
    with open(file_path,"a",newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(args)

def get_single_course_info(url):
    time.sleep(randint(0,4))

    response = requests.get(url)
    if (response.status_code == 200):
        course_content = BeautifulSoup(response.text,'html.parser')
        #todo: extract course title, author_tag. course_date_tags. find course_date, course_link,article_content_first_4_graph

write_csv_header(output_file_path,csv_header)
response = requests.get(website)
soup_data = BeautifulSoup(response.text,'html.parser')
course_cards = soup_data.find_all("div",{"class":"col-md-4 col-sm-6"})


#process soup_data
for course in course_cards:
    #extract title, tag, link and individual info
    link = course.find("a").attrs.get("href","None")
    title =  course.find("h3",{"class":"card-title"}).get_text()
    tags =  course.find("div",{"class":"tags"}).get_text()

    response = requests.get(link)
    if (response.status_code == 200):
        course_content = BeautifulSoup(response.text,'html.parser')
        author = course_content.find("a",{"class":"align-middle inline-block text-hackr-blue text-p14 font-medium"}).get_text()

        course_dates_tag = course_content.findAll("span",{"class":"align-middle inline-block text-hackr-black text-p14 font-medium"})
        course_date = ""
        for course_date_tag in course_dates_tag:
            course_date = course_date_tag.get_text().strip() if (course_date_tag.get_text().strip()!="|") else ""

        article_content = course_content.find("article",{"class":"article-content"})
        article_paragraph_first_4 = ""
        for article_paragraph_content in article_content.find_all("p")[0:4]:
            if (article_paragraph_first_4!=""):
                article_paragraph_first_4 += ","
            article_paragraph_first_4 += (article_paragraph_content.get_text())
    write_csv_content(output_file_path,title,tags,author,course_date,link,article_paragraph_first_4)