import requests

session = requests.Session()

response_get = session.get("https://api.github.com/events")

response_post = session.post(
    "https://httpbin.org/post",
    data={"id": "testid", "pw": "1205"},
    cookies={"id": "testid"},
)
# print(response_post.text)

response_put = session.put(
    "https://httpbin.org/put",
    data={"id": "testid", "pw": "1205"},
)

response_delete = session.delete("https://httpbin.org/delete")
