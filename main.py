#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser

parser = ArgumentParser(description = "This program converts youtube video links to dideo.ir")
parser.add_argument("url", help = "youtube link")
parser.add_argument("--check", action = "store_true", help = "checking for possible errors")
args = parser.parse_args()

url = args.url

def checkUrl(url):
    try:
        respons = get(url)
        if respons.ok:
            print("No errors")
            return True
        raise Exception("Not ok resopns")
    except:
        print("Link is broken.")
        return False

def getCode(url):
    if "?v=" in url:
        return url.split('?v=')[1]
    return url.split("/")[-1]

video_url = "https://www.dideo.ir/v/yt/{}/".format(getCode(url))
print(video_url)
if args.check:
    print("Checking for possible errors ...")
    checkUrl(video_url)
