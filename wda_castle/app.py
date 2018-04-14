import wda
import time

# Enable debug will see http Request and Response
# wda.DEBUG = True
c = wda.Client('http://localhost:8100')

s = c.session('com.my.hc.rpg.kingdom.simulator')

print(s.window_size())

# e = s(text='街舞').tap()

time.sleep(10)

c.screenshot('screen.png')