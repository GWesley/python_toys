# coding: utf-8
import atx
from threading import Timer
import time
import pytesseract
from PIL import Image
import re
from threading import Thread

d = atx.connect('8ee8d717') # 如果多个手机连接电脑，则需要填入对应的设备号
# d.disable_popups()
arena_round = 0

def clear_moods(inc):
    time.sleep(1)
    d.click_exists("imgs2/moods/1@auto.png")
    time.sleep(1)
    d.click_exists("imgs2/moods/2@auto.png")
    time.sleep(1)
    d.click_exists("imgs2/moods/3@auto.png")
    time.sleep(1)
    d.click_exists("imgs2/moods/4@auto.png")
    time.sleep(1)
    d.click_exists("imgs2/moods/5@auto.png")
    time.sleep(1)
    d.click_exists("imgs2/moods/6@auto.png")
    time.sleep(1)

    # 弹窗
    d.click_exists("imgs2/update@auto.png")
    if d.click_exists("imgs2/jump/door_home@auto.png") :
        print("back home")
        t2 = Timer(60, auto_door, ())
        t2.start()


    t = Timer(inc, clear_moods, (inc,))
    t.start()
    print("clear_moods")

# def claim_reward(inc):
#     d.click_exists("imgs2/update@auto.png")
#     time.sleep(2)
#     d.wait_gone("imgs2/loading@auto.png")
#
#     if d.exists('imgs2/arena/end@auto.png'):
#         print("结束")
#         d.click_exists('imgs2/arena/end@auto.png')
#         time.sleep(5)
#         auto_arena()
#     elif  d.exists("imgs2/jump/map@auto.png"):
#         auto_arena()
#
#     t = Timer(inc, claim_reward, (inc,))
#     t.start()

def auto_door():
    print("enter map")
    time.sleep(3)
    d.click_exists("imgs2/jump/map@auto.png")
    time.sleep(3)
    if  d.click_exists("imgs2/jump/door@auto.png") :
        time.sleep(3)
        print("enter door")
        # d.swipe(1000, 1000, 1000, 400)
        d.swipe(1000, 1000, 1000, 300)
        time.sleep(5)
        d.click_exists("imgs2/jump/7@auto.png")
        time.sleep(5)
        d.click_exists("imgs2/jump/attack@auto.png")
        time.sleep(5)
        if d.exists("imgs2/jump/warning@auto.png") :
            time.sleep(60)
            d.click_exists("imgs2/jump/yes@auto.png")
    else:
        auto_door()

def wait_click(image_path, timeout=240):
    d.wait(image_path, timeout)
    d.click_exists(image_path)

def auto_arena(food=True):

    food = False
    # traceback.print_exc()

    d.click_exists('imgs2/arena/end@auto.png')
    time.sleep(3)
    d.click_exists("imgs2/jump/map@auto.png")
    time.sleep(3)
    d.click_exists("imgs2/arena/arena@auto.png")
    time.sleep(3)

    if d.exists("imgs2/arena/home@auto.png") :
        print("continue arena")
        find_rival()
        return

    if food :
        print("food arena")
        d.click_exists("imgs2/arena/food1@auto.png")
    else :
        print("tickets arena")
        d.click_exists("imgs2/arena/tickets@auto.png")

    print("== start round == %d" % arena_round)
    
    wait_click("imgs2/arena/start@auto.png")
    wait_click("imgs2/confirm@auto.png")

    #从第一名开始往下找
    find_rival(240)

    # box = atx.Bounds(0, 0, 0, 0)
    # nd = d.region(box)

def find_rival(timeout=3):
    print("find_rival")
    time.sleep(3)
    d.click_exists('imgs2/arena/win@auto.png')
    time.sleep(3)
    d.click_exists('imgs2/arena/end@auto.png')

    d.wait("imgs2/arena/home@auto.png",timeout=240)

    n = 0

    while n < 15:
        if d.exists("imgs2/arena/find_next@auto.png"):
            print("找下个对手 %s" % n)
            n = n + 1
            wait_click("imgs2/arena/%d@auto.png" % n)
            time.sleep(3)
            
            if d.exists('imgs2/arena/disable@auto.png'):
                wait_click("imgs2/arena/close@auto.png")
                print('can not fight')
                continue

            if not d.exists("imgs2/arena/close@auto.png") :
                print("no close btn")
                continue

            d.screenshot('screen.png')
            if should_win('screen.png'):
                global arena_round
                arena_round += 1
                print("== round: %d" % arena_round)
                wait_click("imgs2/arena/gan@auto.png")
                wait_click("imgs2/arena/x1@auto.png", timeout=20)
                wait_click("imgs2/arena/x2@auto.png", timeout=20)
                did_win()

                return
            else :
                wait_click("imgs2/arena/close@auto.png")
        else:
            print("退出找对手")
            break

    if d.exists("imgs2/arena/find_next@auto.png"):
        print("再次寻找对手")
        find_rival(3)
    elif d.exists("imgs2/arena/wait_others@auto.png"):
        print("等待他人")
        d.wait("imgs2/arena/find_next@auto.png", 120)
        find_rival(3)
    else :
        did_win()


def did_win():
    print('did win?')
    global arena_round

    if d.exists('imgs2/arena/end@auto.png'):
        print("结束")
        d.click_exists('imgs2/arena/end@auto.png')
        time.sleep(5)
        auto_arena()
        return
    else :
        print("== 等待win %d" % arena_round)
        if arena_round >= 5:
            arena_round = 0
            print("== win")
            wait_click('imgs2/arena/win@auto.png', timeout=120)
            print("== 收菜")
            d.wait('imgs2/arena/end@auto.png', timeout=120)
            print("结束")
            d.click_exists('imgs2/arena/end@auto.png')
            time.sleep(5)
            auto_arena()
            return

        wait_click('imgs2/arena/win@auto.png', timeout=120)
        time.sleep(3)
        if d.exists('imgs2/loading@auto.png'):
            d.wait_gone('imgs2/loading@auto.png')


    print("判断是否结束")
    if  arena_round >= 5:
        arena_round = 0
        print("== 收菜")
        d.wait('imgs2/arena/end@auto.png', timeout=60)
        print("结束")
        d.click_exists("imgs2/arena/close@auto.png")
        time.sleep(2)
        d.click_exists('imgs2/arena/end@auto.png')
        time.sleep(5)
        auto_arena()

    else :
        find_rival(3)
    # elif d.exists('imgs2/arena/end@auto.png'):
    #     print("结束")
    #     arena_round = 0
    #     d.click_exists('imgs2/arena/end@auto.png')
    #     time.sleep(5)
    #     auto_arena()

class ThreadWithReturnValue(Thread):  
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):  
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)  
  
        self._return = None  
  
    def run(self):  
        if self._target is not None:  
            self._return = self._target(*self._args, **self._kwargs)  
  
    def join(self):  
        Thread.join(self)  
        return self._return      

def should_win(img_path):
    t1 = ThreadWithReturnValue(target=get_power,args=(img_path, (600, 470, 820, 510),))
    t1.start()
    t2 = ThreadWithReturnValue(target=get_power,args=(img_path, (1055, 470, 1280, 510),))
    t2.start()

    t1.join()
    t2.join()

    p1 = t1._return
    p2 = t2._return
    # p1 = get_power(img_path, (600, 470, 820, 510))
    # p2 = get_power(img_path, (1055, 470, 1280, 510))
    print('战斗力：%d vs %d' % (p1, p2))
    if  p1 == 1000000 or p2 == 1000000:
        find_rival(3)
    p2 += 10000
    return p1 > p2

def get_power(img_path, box):

    with Image.open(img_path) as img:
        crop = img.crop(box)
        gray = crop.convert('L')
        ww = gray.point(lambda x: 255 if x >= 230 else 0, '1')

        text = pytesseract.image_to_string(ww).replace(' ', '')
        text = re.sub('\D', "", text)
        # print("power : " + text)
        try:
            r = int(text)
            if len(text) < 6:
               return r * pow(10,(6-len(text)))
            return r
        except ValueError as e:
            ww.save('imgs2/arena/failed/%s.png' % time.time())
            return 1000000
        except Exception as e:
            print('Error:', e)
            return 1000000
        else :
            print("not catch")
            return 1000000


# clear_moods(10)
def safe():
    try:
        auto_arena()
    except Exception as e:
        print("!!!! %s" % str(e))
        safe()
    # else:
        # safe()


safe()
# auto_door()

