import requests

res = requests.post("http://localhost:5000/api/ytTranscript", json={"url": "https://www.youtube.com/watch?v=mBYu5NoXBcs"})

if res.text == open("test.txt").read():
    print("Content same")