import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://subhendudash02.github.io'
    ]

    def parse(self, response):
        for post in response.css(".About"):
            yield {
                "title": post.css("h1::text")[0].get(),
                "desc1": post.css(".desc p::text")[0].get(),
                "desc2": post.css(".desc p::text")[1].get()
            }