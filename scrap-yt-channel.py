from requests_html import HTMLSession
from sys import argv
import pandas as pd

from get_video_count import *

URL = "https://www.youtube.com"
session = HTMLSession()
channel_id = ""
try:
    channel_id = argv[1]
except IndexError:
    channel_id = input("Enter Channel ID (it looks like @some_id): ")

def make_link(href: str) -> str:
    return f"{URL}/{href}"

VIDEO_COUNT_FACTOR = 0.333
scrolldown = round(get_video_count(channel_id) * VIDEO_COUNT_FACTOR)

site = session.get(f"{URL}/{channel_id}/videos")
site.html.render(sleep=2, keep_page=True, scrolldown=scrolldown)
video_objects = []

videos = site.html.xpath('//*[@id="video-title-link"]')
for video in videos:
    href = video.attrs["href"][1:]
    title = video.find("yt-formatted-string")[0].text 

    video = {
        "title": title,
        "link": make_link(href)
    }

    print(video)
    video_objects.append(video)

videos_df = pd.DataFrame(video_objects)
videos_df.to_csv(f"{channel_id.replace('@', '')}.csv", index=False)