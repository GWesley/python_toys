# coding: utf-8
import atx, wda
import time

d = atx.connect('http://localhost:8100')

print(d.status)
d.session.orientation = wda.LANDSCAPE


def start_kingdom(d):
    d.start_app('com.my.hc.rpg.kingdom.simulator')
    # d.wait("imgs/pages/home.png", timeout=20, safe=False)
    time.sleep(15)
    print("启动成功")

def clear_moods(d):
    while (d.exists("imgs/moods/1.png") is not None):
        d.click_image("imgs/moods/1.png", timeout=2)
    # while (d.exists("imgs/moods/2.png") is not None):
    #     d.click_image("imgs/moods/2.png", timeout=2)

def go_map(d):
    # d.click_image('imgs/map.1242x2208.png', timeout=5)
    d.click(20,1000)

def go_home(d):
    # d.click_image('imgs/home.1242x2208.png', timeout=5)
    d.click(20, 1000)

def go_market(d):
    d.click(2100, 1000)

# start_kingdom(d)
# go_map(d)
# go_home(d)
# clear_moods(d)

go_market(d)