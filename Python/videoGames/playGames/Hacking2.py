# coding: UTF-8
import sys
l1l11l_opy_ = sys.version_info [0] == 2
l1ll1_opy_ = 2048
l11l1_opy_ = 7
def l1ll1l_opy_ (l11ll_opy_):
    global l111l_opy_
    l1lll1_opy_ = ord (l11ll_opy_ [-1])
    l1llll_opy_ = l11ll_opy_ [:-1]
    l1_opy_ = l1lll1_opy_ % len (l1llll_opy_)
    l1lll_opy_ = l1llll_opy_ [:l1_opy_] + l1llll_opy_ [l1_opy_:]
    if l1l11l_opy_:
        l1ll_opy_ = l1111_opy_ () .join ([l1l1ll_opy_ (ord (char) - l1ll1_opy_ - (l1l1_opy_ + l1lll1_opy_) % l11l1_opy_) for l1l1_opy_, char in enumerate (l1lll_opy_)])
    else:
        l1ll_opy_ = str () .join ([chr (ord (char) - l1ll1_opy_ - (l1l1_opy_ + l1lll1_opy_) % l11l1_opy_) for l1l1_opy_, char in enumerate (l1lll_opy_)])
    return eval (l1ll_opy_)
# l1l1l1l_opy_ l11l1ll_opy_ 2
# l11l_opy_ is a l111_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# 1 l11111_opy_ to l1111l_opy_ the l11l1l_opy_. l11llll_opy_ l11l11_opy_ l1l111l_opy_ that the
# l1l1l11_opy_ l11ll11_opy_ to l1111l_opy_ the l11l1l_opy_ l11ll1_opy_.
from uagame import Window
from time import sleep
# create window
window = Window(l1ll1l_opy_ (u"ࠬࡎࡡࡤ࡭࡬ࡲ࡬࠭ࠏ"), 600, 500)
window.set_font_name(l1ll1l_opy_ (u"࠭ࡣࡰࡷࡵ࡭ࡪࡸ࡮ࡦࡹࠪࠐ"))
window.set_font_size(18)
window.set_font_color(l1ll1l_opy_ (u"ࠧࡨࡴࡨࡩࡳ࠭ࠑ"))
window.set_bg_color(l1ll1l_opy_ (u"ࠨࡤ࡯ࡥࡨࡱࠧࠒ"))
# l1l_opy_ l1l1ll1_opy_
l1l1111_opy_ = 0
l1llll1_opy_ = window.get_font_height()
window.draw_string(l1ll1l_opy_ (u"ࠩࡇࡉࡇ࡛ࡇࠡࡏࡒࡈࡊ࠭ࠓ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠪ࠵ࠥࡇࡔࡕࡇࡐࡔ࡙࠮ࡓࠪࠢࡏࡉࡋ࡚ࠧࠔ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l11lll1_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠫࠬࠕ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# l1l_opy_ l11l1l_opy_ list
window.draw_string(l1ll1l_opy_ (u"ࠬࡖࡒࡐࡘࡌࡈࡊ࠭ࠖ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"࠭ࡓࡆࡖࡗࡍࡓࡍࠧࠗ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠧࡄࡃࡑࡘࡎࡔࡁࠨ࠘"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠨࡅࡘࡘ࡙ࡏࡎࡈࠩ࠙"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠩࡋ࡙ࡓ࡚ࡅࡓࡕࠪࠚ"), 0, l1l1111_opy_)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.update()
sleep(0.3)
window.draw_string(l1ll1l_opy_ (u"ࠪࡗ࡚ࡘࡖࡊࡘࡈࠫࠛ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠫࡍࡋࡁࡓࡋࡑࡋࠬࠜ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠬࡎࡕࡏࡖࡌࡒࡌ࠭ࠝ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"࠭ࡒࡆࡃࡏࡍ࡟ࡋࠧࠞ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠧࡏࡑࡗࡌࡎࡔࡇࠨࠟ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠨࡑ࡙ࡉࡗࡒࡁࡑࠩࠠ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠩࡉࡍࡓࡊࡉࡏࡉࠪࠡ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠪࡔ࡚࡚ࡔࡊࡐࡊࠫࠢ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠫࠬࠣ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# prompt for l1111l_opy_
l1111l_opy_ = window.input_string(l1ll1l_opy_ (u"ࠬࡋࡎࡕࡇࡕࠤࡕࡇࡓࡔ࡙ࡒࡖࡉࠦ࠾ࠨࠤ"), 0, l1l1111_opy_)
# end l11l11_opy_
#   clear window
window.clear()
#   l1l_opy_ l1ll11l_opy_ l1l1lll_opy_
#      l1l_opy_ l1111l_opy_
#         l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1111l_opy_)
l1lll1l_opy_ = l1ll1ll_opy_ // 2
#         l11ll1l_opy_ y l1l11l1_opy_
l1lll11_opy_ = 7*l1llll1_opy_
l1l11ll_opy_ = window.get_height() - l1lll11_opy_
l1l1111_opy_ = l1l11ll_opy_ // 2
window.draw_string(l1111l_opy_, l1lll1l_opy_, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"࠭ࠧࠥ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1ll11l_opy_ line 2
#         l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1ll1l_opy_ (u"ࠧࡍࡑࡊࡍࡓࠦࡆࡂࡋࡏ࡙ࡗࡋࠠ࠮ࠢࡗࡉࡗࡓࡉࡏࡃࡏࠤࡑࡕࡃࡌࡇࡇࠫࠦ"))
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.draw_string(l1ll1l_opy_ (u"ࠨࡎࡒࡋࡎࡔࠠࡇࡃࡌࡐ࡚ࡘࡅࠡ࠯ࠣࡘࡊࡘࡍࡊࡐࡄࡐࠥࡒࡏࡄࡍࡈࡈࠬࠧ"), l1lll1l_opy_, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠩࠪࠨ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1ll11l_opy_ line 3
#         l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1ll1l_opy_ (u"ࠪࡔࡑࡋࡁࡔࡇࠣࡇࡔࡔࡔࡂࡅࡗࠤࡆࡔࠠࡂࡆࡐࡍࡓࡏࡓࡕࡔࡄࡘࡔࡘࠧࠩ"))
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.draw_string(l1ll1l_opy_ (u"ࠫࡕࡒࡅࡂࡕࡈࠤࡈࡕࡎࡕࡃࡆࡘࠥࡇࡎࠡࡃࡇࡑࡎࡔࡉࡔࡖࡕࡅ࡙ࡕࡒࠨࠪ"), l1lll1l_opy_, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠬ࠭ࠫ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   prompt for end
#      l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1ll1l_opy_ (u"࠭ࡐࡓࡇࡖࡗࠥࡋࡎࡕࡇࡕࠤ࡙ࡕࠠࡆ࡚ࡌࡘࠬࠬ"))
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.input_string(l1ll1l_opy_ (u"ࠧࡑࡔࡈࡗࡘࠦࡅࡏࡖࡈࡖ࡚ࠥࡏࠡࡇ࡛ࡍ࡙࠭࠭"), l1lll1l_opy_, l1l1111_opy_)
#   close window
window.close()