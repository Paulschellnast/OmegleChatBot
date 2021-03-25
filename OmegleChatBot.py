from pyomegle import OmegleClient
from pyomegle import OmegleHandler
import time

h = OmegleHandler(loop=True)
c = OmegleClient(h, wpm=47, lang="de", topics=[("TOPICS YOUR INTERESTED IN")])


c.start()

input_str = "YOUR TEXT"
input_str2 = "YOUR TEXT"

while 1:
    time.sleep(5)
    c.send(input_str)
    time.sleep(1)
    c.send(input_str2)
    time.sleep(7)
    c.next()