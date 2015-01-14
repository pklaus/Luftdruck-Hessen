
Luftdruck Hessen
================

This tool scrapes the web page of the *Hessian Agency for the Environment and Geology*
offering the air pressure in different cities in Hessen as HTML table.

The Python toolscrapes the site, extracts the values for a given city and prints the output
in JSON, CSV, or Python dictionary format.


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


Author
------

Philipp Klaus <philipp.l.klaus → at → web.de>


