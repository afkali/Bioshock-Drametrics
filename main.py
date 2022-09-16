from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

final_data = pd.DataFrame()

page = requests.get("https://game-scripts-wiki.blogspot.com/2022/01/bioshock-full-transcript.html")

soup = BeautifulSoup(page.content, "html.parser")

content = soup.find_all(class_="post-body entry-content float-container")
content = str(content)

re_acts = r'<h2>(.*?)</h2>'
acts_list = re.findall(re_acts, content)

re_speaker = r'<b>(.*?):'
speaker_list = re.findall(re_speaker, content)  # funktioniert,
# nur ein <i> content wird ganz am Anfang auch mitaufgenommen??

re_stageDirections = r'<i>(.*?)</i>'
stageDirections_list = re.findall(re_stageDirections, content)

re_texts = r'</b>(.*?)<br/>'
texts_list = re.findall(re_texts, content)

re_scenes = r'\[(.*?)\]'
scenes_list = re.findall(re_scenes, content)

# bioshockI = pd.DataFrame({
#    "acts": texts_list,
#    "scenes": scenes_list,
#    "speaker": speaker_list,
#    "text": texts_list,
#    "SD": stageDirections_list
#})


