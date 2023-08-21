import requests as rq
from requests_html import HTMLSession

def get_video_count(channel: str) -> int:
    session = HTMLSession()
    site = session.get(f"https://www.youtube.com/{channel}")
    site.html.render(sleep=1, keep_page=True, scrolldown=1)
    video_count = site.html.xpath('//*[@id="videos-count"]/span[1]')[0]
    return int(video_count.text)
