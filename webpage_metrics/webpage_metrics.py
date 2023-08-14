from webpage import URLS, WebPage


if __name__ == '__main__':
    wps = [WebPage(url) for url in URLS]
    WebPage.tabulate_print()
