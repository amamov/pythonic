# pip install beautifulsoup4 requests
from bs4 import BeautifulSoup

# html = requests.get('...').text
html = """
<html>
    <head>
        <title>amamov developer</title>
    </head>
    <body>
        <h1>This is h1 area</h1>
        <h2>This is h2 area</h2>
        <p class="title"><b>Yoon - sang seok</b></p>
        <p class="intro">
            <span>Hello. My name is sang seok Yoon</span>
            <a href="http://yoon-sang-seok" class="sister" id="home">Home</a>
            <a href="https://amamov.tistroy.com" class="sister" id="blog">Blog</a>
            <a data-io="link3" href="https://amamov.tistroy.com" class="bro" id="link3">Title</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

print("soup :", type(soup))
print("prettify :", soup.prettify())

# p 태그중 가장 상위 태그를 가져온다.
p1 = soup.html.body.p
print("p1 :", p1)

# 태그 안의 string을 가져온다.
print("p1 >>", p1.string)

# next_sibling : 다음 <>로 이동한다.
p2 = p1.next_sibling.next_sibling
print("p2 :", p2)

# p2 안의 모든 text를 가져온다. string은 에러난다.
print(p2.text)
