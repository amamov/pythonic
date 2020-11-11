# [find, find_all --> 태그로 접근할때 사용한다.]
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>amamov developer</title>
    </head>
    <body>
        <p class="intro">
            <span>Hello. My name is sang seok Yoon</span>
            <a href="http://yoon-sang-seok" class="sister" id="home">Home</a>
            <a href="https://amamov.tistroy.com" class="sister" id="blog">Blog</a>
            <a data-io="link3" href="https://amamov.tistroy.com" class="bro" id="link3">Title</a>
        </p>
    </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

#### [find]

# a 태그중 가장 위에 있는 것을 가져온다.
first_link = soup.find("a")

# class가 bro이고 data-io가 link3인 a의 href 속성 값을 가져온다.
found_link = soup.find("a", {"class": "bro", "data-io": "link3"})["href"]


#### [find_all]

# 모든 a 태그를 가져와서 리스트로 만든다.
link = soup.find_all("a")

# a 태그중 2개만 가져온다.
link2 = soup.find_all("a", limit=2)

# a 태그중에서 class가 sister인 것을 가져온다.
link3 = soup.find_all("a", class_="sister")

# a 태그중에서 class가 sister인 것을 가져온다.
link3 = soup.find_all("a", id="home")

# a 태그중에서 string이 Blog, Title인 것을 가져온다.
link4 = soup.find_all("a", string=["Blog", "Title"])
