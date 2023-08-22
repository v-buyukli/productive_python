from tabulate import tabulate

from webpage import WebPage


URLS = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.netflix.com',
    'https://www.jetbrains.com',
    'https://aws.amazon.com',
]


def main():
    wps = {}

    for url in URLS:
        wp = WebPage(url)
        wps[url] = wp.page_size, wp.time_elapsed

    table_data = [(url,) + data for url, data in wps.items()]
    headers = ['url', 'size(bytes)', 'elapsed(s)']
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))


if __name__ == '__main__':
    main()
