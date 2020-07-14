# coding: UTF-8
import sys
ll_opy_ = sys.version_info [0] == 2
l11l_opy_ = 2048
l1_opy_ = 7
def l11l1_opy_ (l1ll1_opy_):
    global l1l11_opy_
    l1lll1_opy_ = ord (l1ll1_opy_ [-1])
    l11ll_opy_ = l1ll1_opy_ [:-1]
    l11_opy_ = l1lll1_opy_ % len (l11ll_opy_)
    l1lll_opy_ = l11ll_opy_ [:l11_opy_] + l11ll_opy_ [l11_opy_:]
    if ll_opy_:
        l1l1_opy_ = l1l1l_opy_ () .join ([l111_opy_ (ord (char) - l11l_opy_ - (l111l_opy_ + l1lll1_opy_) % l1_opy_) for l111l_opy_, char in enumerate (l1lll_opy_)])
    else:
        l1l1_opy_ = str () .join ([chr (ord (char) - l11l_opy_ - (l111l_opy_ + l1lll1_opy_) % l1_opy_) for l111l_opy_, char in enumerate (l1lll_opy_)])
    return eval (l1l1_opy_)
# l1l1lll_opy_ l1l111_opy_ l1l11l_opy_ l1l11ll_opy_ 1
# l1ll_opy_ is a l1ll1l_opy_ l1111l1_opy_ l11lll_opy_ l111111_opy_ l111l1l_opy_ move l11l11_opy_
# the l11ll11_opy_, l11lll1_opy_ l1l1l1l_opy_ the l11111l_opy_.
from uagame import Window
from pygame import QUIT, Color
# from pygame.time import Clock
from time import sleep
from pygame.event import get as l1l1l11_opy_
from pygame.draw import circle as l1llllll_opy_
# l1lll1ll_opy_-l1111l_opy_ l1l111l_opy_
def main():
    window = l1ll1lll_opy_()
#    clock = Clock()
    l111llll1_opy_ = l11l1_opy_ (u"ࠫࡷ࡫ࡤࠨࢌ")
    l11l11l11_opy_ = 30
    l11l111l1_opy_ = [50,75]
    l11l111ll_opy_ = [1,2]
    l11l1111l_opy_ = l11l1_opy_ (u"ࠬࡨ࡬ࡶࡧࠪࢍ")
    l111lll1l_opy_ = 40
    l111lllll_opy_ = [200,100]
    l11l11111_opy_ = [2,1]
    l1l1l1ll_opy_(window, l111llll1_opy_, l11l111l1_opy_, l11l11l11_opy_, l11l111ll_opy_, l11l1111l_opy_, l111lllll_opy_, l111lll1l_opy_, l11l11111_opy_) #, clock)
    window.close()
def l1ll1lll_opy_():
    window = Window(l11l1_opy_ (u"࠭ࡐࡰ࡭ࡨࠤࡹ࡮ࡥࠡࡆࡲࡸࡸ࠭ࢎ"), 500, 400)
    window.set_bg_color(l11l1_opy_ (u"ࠧࡣ࡮ࡤࡧࡰ࠭࢏"))
    return window
def l1l1l1ll_opy_(window, l111llll1_opy_, l11l111l1_opy_, l11l11l11_opy_, l11l111ll_opy_, l11l1111l_opy_, l111lllll_opy_, l111lll1l_opy_, l11l11111_opy_): #, clock):
    l1l1ll11_opy_ = False
    while not l1l1ll11_opy_:
        l1l1ll11_opy_ = l1llll1_opy_()
        l1ll11ll_opy_(window, l111llll1_opy_, l11l111l1_opy_, l11l11l11_opy_, l11l1111l_opy_, l111lllll_opy_, l111lll1l_opy_)
        l1ll1l11_opy_(window, l11l111l1_opy_, l11l11l11_opy_, l11l111ll_opy_, l111lllll_opy_, l111lll1l_opy_, l11l11111_opy_) #, clock)
def l1llll1_opy_():
    closed = False
    l111l11_opy_ = l1l1l11_opy_()
    for event in l111l11_opy_:
        if event.type == QUIT:
            closed = True
    return closed
def l1ll11ll_opy_(window, l111llll1_opy_, l11l111l1_opy_, l11l11l11_opy_, l11l1111l_opy_, l111lllll_opy_, l111lll1l_opy_):
    window.clear()
    l1ll11l1_opy_(window, l111llll1_opy_, l11l111l1_opy_, l11l11l11_opy_)
    l1ll11l1_opy_(window, l11l1111l_opy_, l111lllll_opy_, l111lll1l_opy_)
    window.update()
def l1ll1l11_opy_(window, l11l111l1_opy_, l11l11l11_opy_, l11l111ll_opy_, l111lllll_opy_, l111lll1l_opy_, l11l11111_opy_): #, clock):
    l1l1llll_opy_ = 90
    l1ll1111_opy_(window, l11l111l1_opy_, l11l11l11_opy_, l11l111ll_opy_)
    l1ll1111_opy_(window, l111lllll_opy_, l111lll1l_opy_, l11l11111_opy_)
    sleep(0.01)
#    clock.l1lllll_opy_(l1l1llll_opy_)
def l1ll11l1_opy_(window, color_string, center, l1l1ll1_opy_):
    surface = window.get_surface()
    color = Color(color_string)
    l1llllll_opy_(surface, color, center, l1l1ll1_opy_)
def l1ll1111_opy_(window, center, l1l1ll1_opy_, l1ll1l1_opy_):
    size = (window.get_width(), window.get_height())
    for index in range(0, 2):
        center[index] = center[index] + l1ll1l1_opy_[index]
        if (center[index] <= l1l1ll1_opy_) or (center[index] + l1l1ll1_opy_ >= size[index]):
            l1ll1l1_opy_[index] = - l1ll1l1_opy_[index]
main()