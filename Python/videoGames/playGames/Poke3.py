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
# l1l1lll_opy_ l1l111_opy_ l1l11l_opy_ l1l11ll_opy_ 3
# l1ll_opy_ is a l1ll1l_opy_ l1111l1_opy_ l11lll_opy_ l111111_opy_ l111l1l_opy_ move l11l11_opy_
# the l11ll11_opy_, l11lll1_opy_ l1l1l1l_opy_ the l11111l_opy_. l1l111_opy_ user l1lll11_opy_
# to l1llll11_opy_ the l111l1l_opy_ from colliding by l1lll1l1_opy_ and
# l11l1l1_opy_ the mouse l111lll_opy_ to l1l1111_opy_ the l111l1l_opy_ to
# a random location. l1l111_opy_ l1l11l1_opy_ is the number of l11ll1l_opy_
# from the start of the l1111l1_opy_.
from uagame import Window
from random import randint
from pygame import QUIT, Color, MOUSEBUTTONUP
# from pygame.time import Clock, get_ticks
from pygame.time import get_ticks
from time import sleep
from pygame.event import get as l1l1l11_opy_
from pygame.draw import circle as l1llllll_opy_
# l1lll1ll_opy_-l1111l_opy_ l1l111l_opy_
def main():
    window = l1ll1lll_opy_()
    l1111l1_opy_ = l1ll1ll1_opy_(window)
    l1l1l1ll_opy_(l1111l1_opy_)
    window.close()
def l1ll1lll_opy_():
    window = Window(l11l1_opy_ (u"ࠫࡕࡵ࡫ࡦࠢࡷ࡬ࡪࠦࡄࡰࡶࡶࠫࢅ"), 500, 400)
    window.set_font_name(l11l1_opy_ (u"ࠬࡧࡲࡪࡧ࡯ࠫࢆ"))
    window.set_font_size(64)
    window.set_font_color(l11l1_opy_ (u"࠭ࡷࡩ࡫ࡷࡩࠬࢇ"))
    window.set_bg_color(l11l1_opy_ (u"ࠧࡣ࡮ࡤࡧࡰ࠭࢈"))
    return window
def l1ll1ll1_opy_(window):
    l1111l1_opy_ = l1lll1l_opy_()
    l1111l1_opy_.window = window
    l1111l1_opy_.l1l1llll_opy_ = 90
    l1111l1_opy_.l1l1ll11_opy_ = False
#    l1111l1_opy_.clock = Clock()
    l1111l1_opy_.l1ll1l1l_opy_ = l1lll11l_opy_(l11l1_opy_ (u"ࠨࡴࡨࡨࠬࢉ"), [50,75], 30, [1,2], window)
    l1111l1_opy_.l1l1lll1_opy_ = l1lll11l_opy_(l11l1_opy_ (u"ࠩࡥࡰࡺ࡫ࠧࢊ"), [200,100], 40, [2,1], window)
    l11l11l1l_opy_(l1111l1_opy_.l1ll1l1l_opy_)
    l11l11l1l_opy_(l1111l1_opy_.l1l1lll1_opy_)
    l1111l1_opy_.l1l11l1_opy_ = 0
    return l1111l1_opy_
def l1lll11l_opy_(color, center, l1l1ll1_opy_, l1l1ll1l_opy_, window):
    dot = l1l1ll_opy_()
    dot.color = color
    dot.center = center
    dot.l1l1ll1_opy_ = l1l1ll1_opy_
    dot.l1ll1l1_opy_ = l1l1ll1l_opy_
    dot.window = window
    return dot
def l1l1l1ll_opy_(l1111l1_opy_):
    while not l1111l1_opy_.l1l1ll11_opy_:
        l1llll1_opy_(l1111l1_opy_)
        l1ll11ll_opy_(l1111l1_opy_)
        l1ll1l11_opy_(l1111l1_opy_)
def l1llll1_opy_(l1111l1_opy_):
    l111l11_opy_ = l1l1l11_opy_()
    for event in l111l11_opy_:
        #l1lll111_opy_ l1ll111l_opy_ event
        if event.type == QUIT:
            l1111l1_opy_.l1l1ll11_opy_ = True
        elif event.type == MOUSEBUTTONUP:
            l111ll1_opy_(l1111l1_opy_)
def l111ll1_opy_(l1111l1_opy_):
    l11l11l1l_opy_(l1111l1_opy_.l1ll1l1l_opy_)
    l11l11l1l_opy_(l1111l1_opy_.l1l1lll1_opy_)
def l1ll11ll_opy_(l1111l1_opy_):
    l1111l1_opy_.window.clear()
    l1ll1ll_opy_(l1111l1_opy_)
    l1ll11l1_opy_(l1111l1_opy_.l1ll1l1l_opy_)
    l1ll11l1_opy_(l1111l1_opy_.l1l1lll1_opy_)
    l1111l1_opy_.window.update()
def l1ll1ll_opy_(l1111l1_opy_):
    string = l11l1_opy_ (u"ࠪࡗࡨࡵࡲࡦ࠼ࠣࠫࢋ") + str(l1111l1_opy_.l1l11l1_opy_)
    l1111l1_opy_.window.draw_string(string, 0, 0)
def l1ll1l11_opy_(l1111l1_opy_):
    l1ll1111_opy_(l1111l1_opy_.l1ll1l1l_opy_)
    l1ll1111_opy_(l1111l1_opy_.l1l1lll1_opy_)
#    l1111l1_opy_.clock.l1lllll_opy_(l1111l1_opy_.l1l1llll_opy_)
    sleep(0.01)
    l1111l1_opy_.l1l11l1_opy_ = get_ticks() // 1000
def l1ll11l1_opy_(dot):
    surface = dot.window.get_surface()
    color = Color(dot.color)
    l1llllll_opy_(surface, color, dot.center, dot.l1l1ll1_opy_)
def l1ll1111_opy_(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        dot.center[index] = dot.center[index] + dot.l1ll1l1_opy_[index]
        if (dot.center[index] < dot.l1l1ll1_opy_) or (dot.center[index] + dot.l1l1ll1_opy_ > size[index]):
            dot.l1ll1l1_opy_[index] = - dot.l1ll1l1_opy_[index]
def l11l11l1l_opy_(dot):
    size = (dot.window.get_width(), dot.window.get_height())
    for index in range(0, 2):
        dot.center[index] = randint(dot.l1l1ll1_opy_, size[index] - dot.l1l1ll1_opy_)
class l1lll1l_opy_:
    pass
class l1l1ll_opy_:
    pass
main()