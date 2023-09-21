from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/"
                        "https://www.empireonline.com/movies/features/best-movies-2/")

response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

names_list = soup.find_all(name="h3", class_="title")

regular_list = []

for n in names_list:
    name = n.get_text()
    regular_list.append(name)

final_list = regular_list[::-1]
print(len(final_list))

for item in final_list:
    with open("movies.txt", "a+", encoding="utf8") as file:
        file.write(item+"\n")


