# Letargia
Letargia is a flight search engine (now just a python script!) for adventurous people.

You only has to introduce the departure airport and departure date and Letargia it's going to search for you the most cheap flights to anywhere.



- - - - - 

Letargia es un buscador de vuelos para aventureros.

Solo debes introducir el aeropuerto de salida y la fecha de salida y Letargia te buscará los vuelos mas económicos a cualquier lugar.



##Important notice

This software is in alpha state and it's for educational use only. 

To work, it gets info from Google Flight. Using this software you could violate [Google Flight TOS](https://www.google.com/intl/en/policies/terms/).

Also it's important to note that Google can change Google Flight website structure and in that case this script it's going to fail.


##How it works
Letargia is a simple Python script that uses selenium to execute a web browser and scrap Google Flights web to show best prices from your airport. It was designed to use in Linux/Unix system. Not tested on windows.

_Note: It could fail if your internet connection is really poor._



##Requirements

#####Python 3.5
Obviously you need python to execute the script.

#####Selenium for python:
To get selenium, if you have pip installed, just do:

`pip install selenium`

If you are running it over linux, maybe super user is required.

#####Geckodriver
Download from [here](https://github.com/mozilla/geckodriver/releases) your version and decompress it.

If you are using unix system you have to add the executable to the PATH. The simple way in linux is to move the executable to /usr/bin (super user required). Be sure the executable has executing permission.



##Bugs and next steps
- [NEXT] "Take me home" option. Option to find best options to back home once you have decided where to go.
- [NEXT] Instead of showing result in console, show it in an HTML file.
- [NEXT] Add a budget option. Now it's fixed on 50€.
- [NEXT] Graphical interface to select dates and departure airport.

##Log
- [SOLVED] Date doesn't work properly.
- [DONE] Now it doesn't includes repeated results.
- [DONE] Now prices are shown in order.


##About
Designed and programmed by _Marc Hernández Cabot_.

License: GPL 3


Pull requests are welcome!
