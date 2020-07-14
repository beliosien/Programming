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
# l1l1l1l_opy_ l11l1ll_opy_ 3
# l11l_opy_ is a l111_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# 1 l11111_opy_ to l1111l_opy_ the l11l1l_opy_. l11llll_opy_ l11l11_opy_ l1l111l_opy_ l1llll11_opy_
# the l1l1l11_opy_ l1lllll1_opy_ l11l11l_opy_ the l11l1l_opy_ or not.
from uagame import Window
from time import sleep
# create window
window = Window(l1ll1l_opy_ (u"ࠪࡌࡦࡩ࡫ࡪࡰࡪ࣭ࠫ"), 600, 500)
window.set_font_name(l1ll1l_opy_ (u"ࠫࡨࡵࡵࡳ࡫ࡨࡶࡳ࡫ࡷࠨ࣮"))
window.set_font_size(18)
window.set_font_color(l1ll1l_opy_ (u"ࠬ࡭ࡲࡦࡧࡱ࣯ࠫ"))
window.set_bg_color(l1ll1l_opy_ (u"࠭ࡢ࡭ࡣࡦ࡯ࣰࠬ"))
# l1l_opy_ l1l1ll1_opy_
l1l1111_opy_ = 0
l1llll1_opy_ = window.get_font_height()
window.draw_string(l1ll1l_opy_ (u"ࠧࡅࡇࡅ࡙ࡌࠦࡍࡐࡆࡈࣱࠫ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠨ࠳ࠣࡅ࡙࡚ࡅࡎࡒࡗࠬࡘ࠯ࠠࡍࡇࡉࡘࣲࠬ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠩࠪࣳ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# l1l_opy_ l11l1l_opy_ list
window.draw_string(l1ll1l_opy_ (u"ࠪࡔࡗࡕࡖࡊࡆࡈࠫࣴ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠫࡘࡋࡔࡕࡋࡑࡋࠬࣵ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠬࡉࡁࡏࡖࡌࡒࡆࣶ࠭"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"࠭ࡃࡖࡖࡗࡍࡓࡍࠧࣷ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠧࡉࡗࡑࡘࡊࡘࡓࠨࣸ"), 0, l1l1111_opy_)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.update()
sleep(0.3)
window.draw_string(l1ll1l_opy_ (u"ࠨࡕࡘࡖ࡛ࡏࡖࡆࣹࠩ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠩࡋࡉࡆࡘࡉࡏࡉࣺࠪ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠪࡌ࡚ࡔࡔࡊࡐࡊࠫࣻ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠫࡗࡋࡁࡍࡋ࡝ࡉࠬࣼ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠬࡔࡏࡕࡊࡌࡒࡌ࠭ࣽ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"࠭ࡏࡗࡇࡕࡐࡆࡖࠧࣾ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠧࡇࡋࡑࡈࡎࡔࡇࠨࣿ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
window.draw_string(l1ll1l_opy_ (u"ࠨࡒࡘࡘ࡙ࡏࡎࡈࠩऀ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠩࠪँ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# prompt for l1111l_opy_
l1111l_opy_ = window.input_string(l1ll1l_opy_ (u"ࠪࡉࡓ࡚ࡅࡓࠢࡓࡅࡘ࡙ࡗࡐࡔࡇࠤࡃ࠭ं"), 0, l1l1111_opy_)
# end l11l11_opy_
#   clear window
window.clear()
#   create l1l1lll_opy_
if l1111l_opy_ == l1ll1l_opy_ (u"ࠫࡍ࡛ࡎࡕࡋࡑࡋࠬः"):
    l11ll1lll_opy_ = l1ll1l_opy_ (u"ࠬࡋࡘࡊࡖࡌࡒࡌࠦࡄࡆࡄࡘࡋࠥࡓࡏࡅࡇࠪऄ")
    l11lll111_opy_ = l1ll1l_opy_ (u"࠭ࡌࡐࡉࡌࡒ࡙ࠥࡕࡄࡅࡈࡗࡘࡌࡕࡍࠢ࠰ࠤ࡜ࡋࡌࡄࡑࡐࡉࠥࡈࡁࡄࡍࠪअ")
    prompt = l1ll1l_opy_ (u"ࠧࡑࡔࡈࡗࡘࠦࡅࡏࡖࡈࡖ࡚ࠥࡏࠡࡅࡒࡒ࡙ࡏࡎࡖࡇࠪआ")
else:
    l11ll1lll_opy_ = l1ll1l_opy_ (u"ࠨࡎࡒࡋࡎࡔࠠࡇࡃࡌࡐ࡚ࡘࡅࠡ࠯ࠣࡘࡊࡘࡍࡊࡐࡄࡐࠥࡒࡏࡄࡍࡈࡈࠬइ")
    l11lll111_opy_ = l1ll1l_opy_ (u"ࠩࡓࡐࡊࡇࡓࡆࠢࡆࡓࡓ࡚ࡁࡄࡖࠣࡅࡓࠦࡁࡅࡏࡌࡒࡎ࡙ࡔࡓࡃࡗࡓࡗ࠭ई")
    prompt = l1ll1l_opy_ (u"ࠪࡔࡗࡋࡓࡔࠢࡈࡒ࡙ࡋࡒࠡࡖࡒࠤࡊ࡞ࡉࡕࠩउ")
#   l1l_opy_ l1l1lll_opy_
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
window.draw_string(l1ll1l_opy_ (u"ࠫࠬऊ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l1lll_opy_ line 2
#         l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l11ll1lll_opy_)
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.draw_string(l11ll1lll_opy_, l1lll1l_opy_, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"ࠬ࠭ऋ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l1lll_opy_ line 3
#         l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(l11lll111_opy_)
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.draw_string(l11lll111_opy_, l1lll1l_opy_, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#      l1l_opy_ l1l111_opy_ line
window.draw_string(l1ll1l_opy_ (u"࠭ࠧऌ"), 0, l1l1111_opy_)
window.update()
sleep(0.3)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   prompt for end
#      l11ll1l_opy_ x l1l11l1_opy_
l1ll1ll_opy_ = window.get_width() - window.get_string_width(prompt)
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
#   close window
window.close()