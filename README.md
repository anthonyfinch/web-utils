Utils
=====

To be added to: various scripts I find useful when developing for the web.

echo.py
-------

Simple server that echos back the path requested, the headers of the request and any data send along with the request. Useful for debugging api calls where the issue is with the client making the call.

Runs by default on port 8080, this can be overriden by supplying a port number as an argument.

		./echo.py
		Listening on localhost:8080

		./echo.py 8050
		Listening on localhost:8050
