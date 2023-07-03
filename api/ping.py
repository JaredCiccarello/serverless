from ast import parse
from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # response code
        self.send_response(200)

        # headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        word = dic["word"]

        # create message
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

        # https://serverless-ooayg6mii-jaredciccarello.vercel.app/api/ping.py?word=Montezuma


        response = requests.get(url + word)
        data = response.json()
        definitions = []
        for word_data in data:
            definition = word_data["meanings"][0]["definitions"][0]["definition"]
            definitions.append(definition)

        message = str(definitions)

        # respond with the formatted current time?
        self.wfile.write(message.encode())

        return