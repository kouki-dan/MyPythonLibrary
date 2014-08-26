
import re

url_parser = re.compile("^(.+?)://(.+?):?(d+)?(/.*)?$")

def parse_url(url):
  return url_parser.match(url).groups()

def get_domain(url):
  return parse_url(url)[1]



