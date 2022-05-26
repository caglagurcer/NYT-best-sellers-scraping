import scrapy


class BooksSpider(scrapy.Spider):
    book_count = 1
    file = open("books.txt","a")
    name = "books"
    start_urls = ["https://www.nytimes.com/books/best-sellers/"]

    def parse(self,response):
        book_names = response.css("a.css-g5yn3w div.css-1le66x h3.css-i1z3c1::text").getall()
        book_authors = response.css("a.css-g5yn3w div.css-1le66x p.css-1nxjbfc::text").getall()

        i = 0
        while (i < len(book_names)):
            """ yield {
                "name" : book_names[i],                
                "author" : book_authors[i],
            }"""

            self.file.write("-------------------------------------------\n")
            self.file.write(str(self.book_count) + ".\n")
            self.file.write("Book's name : " + book_names[i] + "\n")
            self.file.write("Book's author : " + book_authors[i] + "\n")
            self.file.write("-------------------------------------------\n")
            self.book_count += 1

            i += 1

                

