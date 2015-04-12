
Luftdruck Hessen
================

This tool scrapes the web page of the *Hessian Agency for the Environment and Geology*
offering the air pressure in different cities in an HTML table:
["Aktuelle Luftdruck-Messwerte"][luftdruck].

The Python tool scrapes the site, extracts the values for a given city
and prints the output in JSON, CSV, or Python dictionary format.


Example Usage
-------------

To get the values for "Fürth/Odenwald", run the script like this

    python scraper.py --format csv "Fürth/Odenwald"

an you will get this:

    # Time, Air Pressure
    00:00, 1009.0
    00:30, 1009.0
    [...]
    09:00, 1012.0
    09:30, 1011.0
    10:00, nan
    10:30, 1012.0
    11:00, 1012.0
    11:30, 1012.0
    [...]
    22:00, 1016.0
    22:30, 1016.0
    23:00, 1016.0
    23:30, 1016.0

Check [the web page][luftdruck] for other possible city names.

Requirements
------------

To run this script, you need Python (tested with Python 3) and the modules
requests and beautifulsoup4, both of which you can install with `pip`.

Remarks
-------

If the HTML code of the site was better organized, you could parse it with Pandas in Python like this:

    import pandas as pd
    pressure_url = 'http://www.hlug.de/no_cache/messwerte/luft/meteorologie/luftdruck.html'
    dfs = pd.read_html(pressure_url)

Author
------

Philipp Klaus <philipp.l.klaus → at → web.de>

[luftdruck]: http://www.hlug.de/no_cache/messwerte/luft/meteorologie/luftdruck.html
