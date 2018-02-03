from __future__ import division
import tornado.ioloop
import pyrestful.rest
import random
import os

from pyrestful import mediatypes
from pyrestful.rest import get

class RandomNumber(object):
  quote_date_time = float
  price = float

class RandomResource(pyrestful.rest.RestHandler):
  @get(_path="/random", _produces=mediatypes.APPLICATION_JSON)
  def getQuoteJson(self):
    price = random.randint(145000,146000)
    quote = RandomNumber()
    quote.price = price/100000
    return quote

if __name__ == "__main__":
  try:
    print("Start the service")
    app = pyrestful.rest.RestService([RandomResource])
    app.listen(int(os.environ.get("PORT", 5000)))
    tornado.ioloop.IOLoop.instance().start()
  except KeyboardInterrupt:
    print("\nStop the service")



