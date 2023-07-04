from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        capital = dic.get('capital')
        country = dic.get('country')

        if country:
            url = 'https://restcountries.com/v3.1/name'
            message = ''
            response = requests.get(url + country)
            data = response.json()
            country_message = data[0]['capital'][0]
            message = f"The capital of {country} is {country_message}"
            self.wfile.write(message.encode())

            return

        elif capital:
            url = 'https://restcountries.com/v3.1/name'
            message = ''
            response = requests.get(url + capital)
            data = response.json()
            country_message = data[0]['name']['common']
            message = f"The capital of {capital} is {country_message}"
            self.wfile.write(message.encode())

            return

        # respond with the formatted current time?
        message = "Invalid request"
        self.wfile.write(message.encode())

        return