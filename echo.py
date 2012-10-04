#!/usr/bin/env python
# Simple echo server for debugging http requests.
# Author: Anthony Finch

import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

	def _print_request(self):
		print "Request path:", self.path
		print "\nHeaders:\n", self.headers

		data_length = self.headers.getheaders('content-length')
		if data_length:
			print self.rfile.read(int(data_length[0]))

	def _return_success(self):
		self.send_response(200)

	def do_GET(self):
		print "\nRECEIEVED 'GET' REQUEST:"
		self._print_request()
		self._return_success()

	def do_POST(self):
		print "\nRECEIEVED 'POST' REQUEST:"
		self._print_request()
		self._return_success()

	def do_PUT(self):
		print "\nRECEIEVED 'PUT' REQUEST:"
		self._print_request()
		self._return_success()

	def do_DELETE(self):
		print "\nRECEIEVED 'DELETE' REQUEST:"
		self._print_request()
		self._return_success()

def main(port):
	print('Listening on localhost:%s' % port)
	server = HTTPServer(('', port), RequestHandler)
	server.serve_forever()


if __name__ == "__main__":
	if len(sys.argv) >= 2: 
		port = int(sys.argv[1])
	else:
		port = 8080
	
	main(port)
