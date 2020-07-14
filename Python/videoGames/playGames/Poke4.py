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
# l1l1lll_opy_ l1l111_opy_ l1l11l_opy_ l1l11ll_opy_ 4
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
    l1111l1_opy_ = l1lll1l_opy_()
    l1111l1_opy_.play()
# l1lll1ll_opy_-l1111l_opy_ l11ll1_opy_
class l1lll1l_opy_:
    def __init__(self):
        self._11l111_opy_ = Window(l11l1_opy_ (u"ࠬࡖ࡯࡬ࡧࠣࡸ࡭࡫ࠠࡅࡱࡷࡷࠬࠏ"), 500, 400)
        self._11llll_opy_()
        self._111ll_opy_ = 90
        self._111l1_opy_ = False
#        self._11l11l_opy_ = Clock()
        self._11l1ll_opy_ = l1l1ll_opy_(l11l1_opy_ (u"࠭ࡲࡦࡦࠪࠐ"), [50,75], 30, [1,2], self._11l111_opy_)
        self._1ll111_opy_ = l1l1ll_opy_(l11l1_opy_ (u"ࠧࡣ࡮ࡸࡩࠬࠑ"), [200,100], 40, [2,1], self._11l111_opy_)
        self._11l1ll_opy_.l1lllll1_opy_()
        self._1ll111_opy_.l1lllll1_opy_()
        self._11l1l_opy_ = 0
    def _11llll_opy_(self):
        self._11l111_opy_.set_font_name(l11l1_opy_ (u"ࠨࡣࡵ࡭ࡪࡲࠧࠒ"))
        self._11l111_opy_.set_font_size(64)
        self._11l111_opy_.set_font_color(l11l1_opy_ (u"ࠩࡺ࡬࡮ࡺࡥࠨࠓ"))
        self._11l111_opy_.set_bg_color(l11l1_opy_ (u"ࠪࡦࡱࡧࡣ࡬ࠩࠔ"))
    def play(self):
        while not self._111l1_opy_:
            self.l1llll1_opy_()
            self.draw()
            self.update()
        self._11l111_opy_.close()
    def l1llll1_opy_(self):
        l111l11_opy_ = l1l1l11_opy_()
        for event in l111l11_opy_:
            self.l1ll11l_opy_(event)
    def l1ll11l_opy_(self, event):
        if event.type == QUIT:
            self._111l1_opy_ = True
        elif event.type == MOUSEBUTTONUP:
            self.l111ll1_opy_(event)
    def l111ll1_opy_(self, event):
        self._11l1ll_opy_.l1lllll1_opy_()
        self._1ll111_opy_.l1lllll1_opy_()
    def draw(self):
        self._11l111_opy_.clear()
        self.l1ll1ll_opy_()
        self._11l1ll_opy_.draw()
        self._1ll111_opy_.draw()
        self._11l111_opy_.update()
    def update(self):
        self._11l1ll_opy_.move()
        self._1ll111_opy_.move()
        sleep(0.01)
#        self._11l11l_opy_.l1lllll_opy_(self._111ll_opy_)
        self._11l1l_opy_ = get_ticks() // 1000
    def l1ll1ll_opy_(self):
        string = l11l1_opy_ (u"ࠫࡘࡩ࡯ࡳࡧ࠽ࠤࠬࠕ") + str(self._11l1l_opy_)
        self._11l111_opy_.draw_string(string, 0, 0)
class l1l1ll_opy_:
    def __init__(self, color, center, l1l1ll1_opy_, l1ll1l1_opy_, window):
        self._1111ll_opy_ = color
        self._1l1l1_opy_ = center
        self._1llll1l_opy_ = l1l1ll1_opy_
        self._11111_opy_ = l1ll1l1_opy_
        self._11l111_opy_ = window
    def move(self):
        size = (self._11l111_opy_.get_width(), self._11l111_opy_.get_height())
        for index in range(0, 2):
            self._1l1l1_opy_[index] = self._1l1l1_opy_[index] + self._11111_opy_[index]
            if (self._1l1l1_opy_[index] < self._1llll1l_opy_) or (self._1l1l1_opy_[index] + self._1llll1l_opy_ > size[index]):
                self._11111_opy_[index] = - self._11111_opy_[index]
    def draw(self):
        surface = self._11l111_opy_.get_surface()
        color = Color(self._1111ll_opy_)
        l1llllll_opy_(surface, color, self._1l1l1_opy_, self._1llll1l_opy_)
    def l1lllll1_opy_(self):
        size = (self._11l111_opy_.get_width(), self._11l111_opy_.get_height())
        for index in range(0, 2):
            self._1l1l1_opy_[index] = randint(self._1llll1l_opy_, size[index] - self._1llll1l_opy_)
main()