import wda
import time

# Enable debug will see http Request and Response
# wda.DEBUG = True
c = wda.Client('http://localhost:8100')

s = c.session('com.hotrizon.hvideo')
print(s.orientation)

print(s.window_size())

# e = s(text='街舞').tap()

n = 0
while n < 10:
    n = n + 1
    s.swipe_up()
    s.tap(200, 200)
    time.sleep(4)
