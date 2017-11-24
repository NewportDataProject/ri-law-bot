import scrapy
from rilaws.items import Section

class LawSpider(scrapy.Spider):
    name = "laws"
    start_urls = [
    "http://webserver.rilin.state.ri.us/Statutes/"
    ]

    def parse(self, response):
        # get links to titles
        titles = response.css('table a.homeLinks::attr(href)').extract()
        # limit breadth for debugging:
        for title in titles[0:2]:
            yield response.follow(title, callback=self.parse_title)

    def parse_title(self, response):
        # in each title, get links to chapters
        chapters = response.css('a::attr(href)').extract()
        for chapter in chapters:
            yield response.follow(chapter, callback=self.parse_chapter)

    def parse_chapter(self, response):
        # in each chapter, get links to sections
        sections = response.css('ul a::attr(href)').extract()
        for section in sections:
            yield response.follow(section, callback=self.parse_section)

    def parse_section(self, response):
        # extract the information from each section
        section_id = response.css('title::text').extract_first()
        section_subject = response.css('body p b::text').extract_first()
        section_text = response.css('body p::text').extract()
        section_history = response.css('body history::text').extract()[1]
        # print(section_id)
        section = Section(id=section_id, subject=section_subject, history=section_history, text=section_text)
        yield section
    #     yield {
    #             'id': section_id,
    #             'subject': section_subject,
    #             'text': section_text,
    #             'history': section_history,
    # }
