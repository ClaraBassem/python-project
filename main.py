#python project
import requests
from bs4 import BeautifulSoup
#step 1 get URL from page which we extract data from it
response= requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue")
wiki_text= response.text

#step 2 to make an object
soup = BeautifulSoup(wiki_text , "html.parser")
required_table = soup.find("table" , {"style" :"text-align:left;"})

#step 3 take headers data
header_tags = required_table.findAll("th" , {"scope" : ""})
headers = []
for i in range(8):
   headers.append(header_tags[i].getText().replace('\n', ''))

#step 4 take body data
rows =[]
body_data = required_table.findAll("tbody")
for row in body_data:
    value = row.findAll("td")
    text_value = [ dp.text.strip() for dp in value]
    rows.append(text_value)

print(headers)
print(rows)
























