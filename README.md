# web-survey-tool

Simple Web survey tool written in Python 2 using TDI for HTML rendering
and matplotlib for evaluation plots.

Homepage: https://github.com/digitalarbeiter/web-survey-tool


## Dependencies

The following standard Python libraries are used:

    sys, os, errno, re, json, time, random, hashlib, socket,
    urlparse, urllib, cgi, BaseHTTPServer

Two more packages are needed that may or may not be available for
your distribution:

### matplotlib

matplotlib is a library for for generating data plots. Install the
Debian package (if applicable):

    $ sudo apt-get install python-matplotlib python-matplotlib-data

or from pip repository:

    $ sudo pip install matplotlib

### tdi

The Template Data Interface (https://pypi.python.org/pypi/tdi) is used
for generating HTML. Install from pip repository:

    $ sudo pip install tdi


## Your Own Survey

Copy one of the example surveys (kiga2015.py) and edit it to your needs.
Then you need to generate, print and distribute the vote codes that
restrict voting to registered voters:

    $ python2 my_survey.py --generate-votecodes 100
    $ python2 my_survey.py --print-votecodes > votecodes.txt

Then print votecodes.txt and distribute vote codes.

Next, to conduct the actual survey, start the built-in SimpleHTTPServer
within the web-survey-tool:

    $ python2 my_survey.py --run

and keep it running for the voting period. The screen(1) utility is
helpful for this, or, even better, the daemontools.

After the voting period is over, stop the server and run the evaluation:

    $ python2 my_survey.py --evaluate /tmp/my_survey_report

Now edit the report in /tmp/my\_survey\_report/report.html to your
needs and preceed from there.

