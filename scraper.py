#!/usr/bin/env python

"""
Scrapes the air pressure in Hesse from the site
http://www.hlug.de/no_cache/messwerte/luft/meteorologie/luftdruck.html
"""

try:
    from bs4 import BeautifulSoup
    import requests
    ext_deps = True
except ImportError:
    ext_deps = False
import sys

def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('station', help='Station to scrape the air pressure for.')
    parser.add_argument('--format', default='dict', choices=['dict', 'json', 'csv'], help='Output format')
    parser.add_argument('-ua', metavar='USER_AGENT', default='Air pressure scraper', help='User agent you want scraper to use.')

    if not ext_deps: parser.error("Missing at least one of the python modules 'requests' or 'beautifulsoup4'.")

    args = parser.parse_args()

    browser = requests.Session()
    browser.headers.update({'User-Agent': args.ua})

    times = []
    values = []

    site = browser.get('http://www.hlug.de/no_cache/messwerte/luft/meteorologie/luftdruck.html')
    site_structure = BeautifulSoup(site.text)

    for table_header_cell in site_structure.find_all('th'):
        thct = table_header_cell.text
        if len(thct) == 5 and thct[2] == ':':
            times.append(thct)

    for table_row in site_structure.find_all('tr'):
        cells = table_row.find_all('td')
        if len(cells) < 2: continue
        if not cells[0].text == args.station:
            continue
        for cell in cells[1:]:
            value = float('nan') if cell.text in ['\xa0', '#']  else float(cell.text)
            values.append(value)

    if len(times) != len(values) or len(times) != 48:
        sys.stderr.write("The scraped times and/or values don't fit:\n")
        sys.stderr.write("times: {}\n".format(times))
        sys.stderr.write("values: {}\n".format(values))
        sys.exit(1)

    val_dict = dict(zip(times, values))

    if args.format == 'dict':
        from pprint import pprint
        pprint(val_dict)
    if args.format == 'json':
        import json
        print(json.dumps(val_dict))
    if args.format == 'csv':
        print("# Time, Air Pressure")
        for time in sorted(times):
            print("{}, {}".format(time, val_dict[time]))

if __name__ == "__main__":
    main()

