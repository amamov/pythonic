# [select, select_one --> css 선택자로 접근할때 사용한다.]
from bs4 import BeautifulSoup

# html = requests.get('...').text
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
            <a data-io="link4" href="https://amamov.tistroy.com" class="bro" id="link4">link4</a>
            <a data-io="link5" href="https://amamov.tistroy.com" class="bro" id="link5">link5</a>
        </p>
        <p class="anoter">
            <a href="http://yoon-sang-seok" class="sister" id="AnoterHome">AnoterHome</a>
        </p>
    </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

#### [select_one]

# p태그의 class가 title인 것의 자식인 b태그를 가져온다.
selected_link1 = soup.select_one("p.title > b")

selected_link2 = soup.select_one("a#link3")

selected_link3 = soup.select_one('a[data-io="link3"]')


### [select]

selected_links1 = soup.select("p > a")

selected_links2 = soup.select("p.intro > a:nth-of-type(2)")

selected_links3 = soup.select("p.intro > a:nth-of-type(2n)")

selected_links = soup.select("a")
