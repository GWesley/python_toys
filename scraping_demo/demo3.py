import re
from download import  download

def link_crawler(start_url, link_regex):
    """ Crawl from the given start URL following links matched by
       link_regex
           """
    crawl_queue = [start_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        if html is None:
            continue
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""",
                               re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com/places/default', '/(index|view)/')

#http://example.webscraping.com/places/default/index/1
#http://example.webscraping.com/places/default/view/-1