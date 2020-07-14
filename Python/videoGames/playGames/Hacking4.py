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
# l1l1l1l_opy_ l11l1ll_opy_ 4
# l11l_opy_ is a l111_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# 1 l11111_opy_ to l1111l_opy_ the l11l1l_opy_. l11llll_opy_ l11l11_opy_ l1l111l_opy_ l1llll11_opy_
# the l1l1l11_opy_ l1lllll1_opy_ l11l11l_opy_ the l11l1l_opy_ or not.
from uagame import Window
from time import sleep
# create window
window = Window(l1ll1l_opy_ (u"ࠫࡍࡧࡣ࡬࡫ࡱ࡫ࠬ࣋"), 600, 500)
window.set_font_name(l1ll1l_opy_ (u"ࠬࡩ࡯ࡶࡴ࡬ࡩࡷࡴࡥࡸࠩ࣌"))
window.set_font_size(18)
window.set_font_color(l1ll1l_opy_ (u"࠭ࡧࡳࡧࡨࡲࠬ࣍"))
window.set_bg_color(l1ll1l_opy_ (u"ࠧࡣ࡮ࡤࡧࡰ࠭࣎"))
# l1l_opy_ l1l1ll1_opy_
l1lll11l_opy_ = 0.3
l1lll1l_opy_ = 0
l1l1111_opy_ = 0
l1llll1_opy_ = window.get_font_height()
l1l1ll1_opy_ = [l1ll1l_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠠࡎࡑࡇࡉ࣏ࠬ"), l1ll1l_opy_ (u"ࠩ࠴ࠤࡆ࡚ࡔࡆࡏࡓࡘ࡙࠭ࠩࠡࡎࡈࡊ࡙࣐࠭"), l1ll1l_opy_ (u"࣑ࠪࠫ")]
for l1111ll_opy_ in l1l1ll1_opy_:
    window.draw_string(l1111ll_opy_, l1lll1l_opy_, l1l1111_opy_)
    window.update()
    sleep(l1lll11l_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# l1l_opy_ l11l1l_opy_ list
#   create l11l1l_opy_ list
l11111l_opy_ = [l1ll1l_opy_ (u"ࠫࡕࡘࡏࡗࡋࡇࡉ࣒ࠬ"), l1ll1l_opy_ (u"࡙ࠬࡅࡕࡖࡌࡒࡌ࣓࠭"), l1ll1l_opy_ (u"࠭ࡃࡂࡐࡗࡍࡓࡇࠧࣔ"), l1ll1l_opy_ (u"ࠧࡄࡗࡗࡘࡎࡔࡇࠨࣕ"), l1ll1l_opy_ (u"ࠨࡊࡘࡒ࡙ࡋࡒࡔࠩࣖ"), l1ll1l_opy_ (u"ࠩࡖ࡙ࡗ࡜ࡉࡗࡇࠪࣗ"),  l1ll1l_opy_ (u"ࠪࡌࡊࡇࡒࡊࡐࡊࠫࣘ"), l1ll1l_opy_ (u"ࠫࡍ࡛ࡎࡕࡋࡑࡋࠬࣙ"), l1ll1l_opy_ (u"ࠬࡘࡅࡂࡎࡌ࡞ࡊ࠭ࣚ"), l1ll1l_opy_ (u"࠭ࡎࡐࡖࡋࡍࡓࡍࠧࣛ"), l1ll1l_opy_ (u"ࠧࡐࡘࡈࡖࡑࡇࡐࠨࣜ"), l1ll1l_opy_ (u"ࠨࡈࡌࡒࡉࡏࡎࡈࠩࣝ"), l1ll1l_opy_ (u"ࠩࡓ࡙࡙࡚ࡉࡏࡉࠪࣞ"), l1ll1l_opy_ (u"ࠪࠫࣟ")]
for l11l1l_opy_ in l11111l_opy_:
    window.draw_string(l11l1l_opy_, l1lll1l_opy_, l1l1111_opy_)
    window.update()
    sleep(l1lll11l_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l111l1l_opy_ l11l1l_opy_
l11l1l_opy_ = l11111l_opy_[7]
# prompt for l1111l_opy_
prompt = l1ll1l_opy_ (u"ࠫࡊࡔࡔࡆࡔࠣࡔࡆ࡙ࡓࡘࡑࡕࡈࠥࡄࠧ࣠")
l1111l_opy_ = window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# end l11l11_opy_
#   clear window
window.clear()
#   create l1l1lll_opy_
if l1111l_opy_ == l11l1l_opy_:
    l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"ࠬ࠭࣡"), l1ll1l_opy_ (u"࠭ࡅ࡙ࡋࡗࡍࡓࡍࠠࡅࡇࡅ࡙ࡌࠦࡍࡐࡆࡈࠫ࣢"), l1ll1l_opy_ (u"ࠧࠨࣣ"), l1ll1l_opy_ (u"ࠨࡎࡒࡋࡎࡔࠠࡔࡗࡆࡇࡊ࡙ࡓࡇࡗࡏࠤ࠲ࠦࡗࡆࡎࡆࡓࡒࡋࠠࡃࡃࡆࡏࠬࣤ"), l1ll1l_opy_ (u"ࠩࠪࣥ")]
    prompt = l1ll1l_opy_ (u"ࠪࡔࡗࡋࡓࡔࠢࡈࡒ࡙ࡋࡒࠡࡖࡒࠤࡈࡕࡎࡕࡋࡑ࡙ࡊࣦ࠭")
else:
    l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"ࠫࠬࣧ"), l1ll1l_opy_ (u"ࠬࡒࡏࡈࡋࡑࠤࡋࡇࡉࡍࡗࡕࡉࠥ࠳ࠠࡕࡇࡕࡑࡎࡔࡁࡍࠢࡏࡓࡈࡑࡅࡅࠩࣨ"), l1ll1l_opy_ (u"ࣩ࠭ࠧ"),l1ll1l_opy_ (u"ࠧࡑࡎࡈࡅࡘࡋࠠࡄࡑࡑࡘࡆࡉࡔࠡࡃࡑࠤࡆࡊࡍࡊࡐࡌࡗ࡙ࡘࡁࡕࡑࡕࠫ࣪"), l1ll1l_opy_ (u"ࠨࠩ࣫")]
    prompt = l1ll1l_opy_ (u"ࠩࡓࡖࡊ࡙ࡓࠡࡇࡑࡘࡊࡘࠠࡕࡑࠣࡉ࡝ࡏࡔࠨ࣬")
#   l1l_opy_ l1l1lll_opy_
#      l11ll1l_opy_ y l1l11l1_opy_
l1lll11_opy_ = (len(l1l1lll_opy_) + 1)*l1llll1_opy_
l1l11ll_opy_ = window.get_height() - l1lll11_opy_
l1l1111_opy_ = l1l11ll_opy_ // 2
for l1lll111_opy_ in l1l1lll_opy_:
    l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1lll111_opy_)
    l1lll1l_opy_ = l1ll1ll_opy_ // 2
    window.draw_string(l1lll111_opy_, l1lll1l_opy_, l1l1111_opy_)
    window.update()
    sleep(l1lll11l_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   prompt for end
l1ll1ll_opy_ = window.get_width() - window.get_string_width(prompt)
l1lll1l_opy_ = l1ll1ll_opy_ // 2
window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
#   close window
window.close()