This application suite provides means to browse and manage a Karaoke
listing.

Installation
============
* Install Tcl, for Windows, use Active Tcl
* Install **Python**, for Windows, use Active Python
* Install **pip**: 
    easy_install pip
* Install **virtualenv** and **virtualenvwrapper**
* Create a new virtual environment called *karaoke*
* Activate the new virtual environment:
    workon karaoke
* Install the required libraries:
    pip install mako cherrypy
* Edit app.config and make sure the paths are correct


Running the Character-Based Application
=======================================

Running the character-based (text-mode) application is simple, just issue the following command:

    $ tclsh tkara.tcl
    
Below is a list of commands the text-mode application provides.

    t toi dua em sang song    # Search for song title "Toi Dua Em Sang Song"
    s nguyen hung             # Search for singer "Nguyen Hung"
    f                         # List all favorites
    f hai                     # List Hai's favorites
    f hai 1485                # Add song number 1485 to Hai's favorite
    u                         # List all users
    u Jimmy                   # Add Jimmy to the list of users
    q                         # Quit the application
    
Running the Web Application
===========================

From the command line start the web application:

    $ python pykara.py        # Web application
    $ tclsh tkara.tcl         # Text application, more advanced

Point your browser to the server. For example, if your browser is *haimacbookair.local*, browse to:

    http://haimacbookair.local:1111

Files
=====

* README.md            - This file, the project's README
* app.config           - Configuration file for the web app
* css                  - Directory contains stylesheets
* css/style.css        - The primary stylesheet for all platforms
* karaoke.db           - The database containing songs information
* pykara.py            - The main web application
* tkara.tcl            - The main character-base application
* requirements.txt     - List of Python libraries used in the web application
* static               - Contains static files used by the web application
* static/favicon.ico   - The web application's icon
* templates            - Directory contains all the .HTML templates
* templates/index.html - The primary template used by the web application


