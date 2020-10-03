import os

from apiclient.discovery import build


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
DEVELOPER_KEY = os.environ['YOUTUBE_API_ACCESS_KEY']
# 500件までしかAPIで取得できないため、年毎に分けて取得する
PUBLISHED_PARAM = [
    {"publishedAfter": "2020-01-01T00:00:00Z", "publishedBefore": "2021-01-01T00:00:00Z"},
    {"publishedAfter": "2019-01-01T00:00:00Z", "publishedBefore": "2020-01-01T00:00:00Z"},
    {"publishedAfter": "2018-01-01T00:00:00Z", "publishedBefore": "2019-01-01T00:00:00Z"},
    {"publishedAfter": "2017-01-01T00:00:00Z", "publishedBefore": "2018-01-01T00:00:00Z"},
    {"publishedAfter": "2016-01-01T00:00:00Z", "publishedBefore": "2017-01-01T00:00:00Z"},
    {"publishedAfter": "2015-01-01T00:00:00Z", "publishedBefore": "2016-01-01T00:00:00Z"},
    {"publishedAfter": "2014-01-01T00:00:00Z", "publishedBefore": "2015-01-01T00:00:00Z"},
    {"publishedAfter": "2013-01-01T00:00:00Z", "publishedBefore": "2014-01-01T00:00:00Z"},
]


def get_all_videos(channel_id):
    youtube = youtube_build()
    videos = []

    for param in PUBLISHED_PARAM:
        next_page_token = None
        while True:
            response = youtube.search().list(
                channelId=channel_id,
                order="date",
                pageToken=next_page_token,
                part="id",
                publishedAfter=param["publishedAfter"],
                publishedBefore=param["publishedBefore"],
                maxResults=50,
                safeSearch=None,
                type="video"
            ).execute()

            for item in response["items"]:
                if item["id"]["kind"] == "youtube#video":
                    videos.append(f"https://youtube.com/video/{item['id']['videoId']}")

            if "nextPageToken" not in response: break
            else: next_page_token = response["nextPageToken"]

    # 作成日の降順で取得されるため、昇順に並び替える
    videos.reverse()
    write_txt(videos)


def youtube_build():
    return build(
        YOUTUBE_API_SERVICE_NAME, 
        YOUTUBE_API_VERSION, 
        developerKey=DEVELOPER_KEY
    )


def write_txt(data):
    with open('videos.txt','w') as f:
        f.write('\n'.join(data))


if __name__ == '__main__':
    get_all_videos(input())