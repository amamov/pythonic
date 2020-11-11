from scraper import PhotoScraper

if __name__ == "__main__":
    keyword = input("이미지 검색 >> ").strip()
    photo_scraper = PhotoScraper(keyword)
    photo_scraper.scrape()
