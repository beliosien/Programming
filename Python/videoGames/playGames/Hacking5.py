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
# l1l1l1l_opy_ l11l1ll_opy_ 5
# l11l_opy_ is a l111_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# l111lll_opy_ to 4 l11l111_opy_ to l1111l_opy_ the l11l1l_opy_. l1lll1l1_opy_ time the user
# l1llll1l_opy_ l11l1l1_opy_, the user is l1llllll_opy_ to l1111l1_opy_ a new l1111l_opy_.
# l11llll_opy_ l11l11_opy_ l1l111l_opy_ l1llll11_opy_ the l1l1l11_opy_ l1lllll1_opy_ l11l11l_opy_
# the l11l1l_opy_ or not.
from uagame import Window
from time import sleep
# create window
window = Window(l1ll1l_opy_ (u"ࠨࡊࡤࡧࡰ࡯࡮ࡨࠩ࠮"), 600, 500)
window.set_font_name(l1ll1l_opy_ (u"ࠩࡦࡳࡺࡸࡩࡦࡴࡱࡩࡼ࠭࠯"))
window.set_font_size(18)
window.set_font_color(l1ll1l_opy_ (u"ࠪ࡫ࡷ࡫ࡥ࡯ࠩ࠰"))
window.set_bg_color(l1ll1l_opy_ (u"ࠫࡧࡲࡡࡤ࡭ࠪ࠱"))
# l1l_opy_ l1l1ll1_opy_
l1lll11l_opy_ = 0.3
l1lll1l_opy_ = 0
l1l1111_opy_ = 0
l1llll1_opy_ = window.get_font_height()
l111111_opy_ = 4
l1l1ll1_opy_ = [l1ll1l_opy_ (u"ࠬࡊࡅࡃࡗࡊࠤࡒࡕࡄࡆࠩ࠲"), str(l111111_opy_) + l1ll1l_opy_ (u"࠭ࠠࡂࡖࡗࡉࡒࡖࡔࠩࡕࠬࠤࡑࡋࡆࡕࠩ࠳"), l1ll1l_opy_ (u"ࠧࠨ࠴")]
for l1111ll_opy_ in l1l1ll1_opy_:
    window.draw_string(l1111ll_opy_, l1lll1l_opy_, l1l1111_opy_)
    window.update()
    sleep(l1lll11l_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
# l1l_opy_ l11l1l_opy_ list
#   create l11l1l_opy_ list
l11111l_opy_ = [l1ll1l_opy_ (u"ࠨࡒࡕࡓ࡛ࡏࡄࡆࠩ࠵"), l1ll1l_opy_ (u"ࠩࡖࡉ࡙࡚ࡉࡏࡉࠪ࠶"), l1ll1l_opy_ (u"ࠪࡇࡆࡔࡔࡊࡐࡄࠫ࠷"), l1ll1l_opy_ (u"ࠫࡈ࡛ࡔࡕࡋࡑࡋࠬ࠸"), l1ll1l_opy_ (u"ࠬࡎࡕࡏࡖࡈࡖࡘ࠭࠹"), l1ll1l_opy_ (u"࠭ࡓࡖࡔ࡙ࡍ࡛ࡋࠧ࠺"),  l1ll1l_opy_ (u"ࠧࡉࡇࡄࡖࡎࡔࡇࠨ࠻"), l1ll1l_opy_ (u"ࠨࡊࡘࡒ࡙ࡏࡎࡈࠩ࠼"), l1ll1l_opy_ (u"ࠩࡕࡉࡆࡒࡉ࡛ࡇࠪ࠽"), l1ll1l_opy_ (u"ࠪࡒࡔ࡚ࡈࡊࡐࡊࠫ࠾"), l1ll1l_opy_ (u"ࠫࡔ࡜ࡅࡓࡎࡄࡔࠬ࠿"), l1ll1l_opy_ (u"ࠬࡌࡉࡏࡆࡌࡒࡌ࠭ࡀ"), l1ll1l_opy_ (u"࠭ࡐࡖࡖࡗࡍࡓࡍࠧࡁ"), l1ll1l_opy_ (u"ࠧࠨࡂ")]
for l11l1l_opy_ in l11111l_opy_:
    window.draw_string(l11l1l_opy_, l1lll1l_opy_, l1l1111_opy_)
    window.update()
    sleep(l1lll11l_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
#   l111l1l_opy_ l11l1l_opy_
l11l1l_opy_ = l11111l_opy_[7]
# get l1llll1l_opy_
prompt = l1ll1l_opy_ (u"ࠨࡇࡑࡘࡊࡘࠠࡑࡃࡖࡗ࡜ࡕࡒࡅࠢࡁࠫࡃ")
#   prompt for l1111l_opy_
l1111l_opy_ = window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
l111111_opy_ = l111111_opy_ - 1
while l1111l_opy_ != l11l1l_opy_ and l111111_opy_ > 0:
    window.draw_string(str(l111111_opy_), l1lll1l_opy_, l1llll1_opy_)
    if l111111_opy_ == 1:
        l111l11_opy_ = l1ll1l_opy_ (u"ࠩ࠭࠮࠯ࠦࡌࡐࡅࡎࡓ࡚࡚ࠠࡘࡃࡕࡒࡎࡔࡇࠡࠬ࠭࠮ࠬࡄ")
        l111ll1_opy_ = window.get_width() - window.get_string_width(l111l11_opy_)
        l1lll1ll_opy_ = window.get_height() - l1llll1_opy_
        window.draw_string(l111l11_opy_, l111ll1_opy_, l1lll1ll_opy_)
    l1111l_opy_ = window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
    l1l1111_opy_ = l1l1111_opy_ + l1llll1_opy_
    l111111_opy_ = l111111_opy_ - 1
# end l11l11_opy_
#   clear window
window.clear()
#   create l1l1lll_opy_
if l1111l_opy_ == l11l1l_opy_:
    l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"ࠪࠫࡅ"), l1ll1l_opy_ (u"ࠫࡊ࡞ࡉࡕࡋࡑࡋࠥࡊࡅࡃࡗࡊࠤࡒࡕࡄࡆࠩࡆ"), l1ll1l_opy_ (u"ࠬ࠭ࡇ"), l1ll1l_opy_ (u"࠭ࡌࡐࡉࡌࡒ࡙ࠥࡕࡄࡅࡈࡗࡘࡌࡕࡍࠢ࠰ࠤ࡜ࡋࡌࡄࡑࡐࡉࠥࡈࡁࡄࡍࠪࡈ"), l1ll1l_opy_ (u"ࠧࠨࡉ")]
    prompt = l1ll1l_opy_ (u"ࠨࡒࡕࡉࡘ࡙ࠠࡆࡐࡗࡉࡗࠦࡔࡐࠢࡆࡓࡓ࡚ࡉࡏࡗࡈࠫࡊ")
else:
    l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"ࠩࠪࡋ"), l1ll1l_opy_ (u"ࠪࡐࡔࡍࡉࡏࠢࡉࡅࡎࡒࡕࡓࡇࠣ࠱࡚ࠥࡅࡓࡏࡌࡒࡆࡒࠠࡍࡑࡆࡏࡊࡊࠧࡌ"), l1ll1l_opy_ (u"ࠫࠬࡍ"),l1ll1l_opy_ (u"ࠬࡖࡌࡆࡃࡖࡉࠥࡉࡏࡏࡖࡄࡇ࡙ࠦࡁࡏࠢࡄࡈࡒࡏࡎࡊࡕࡗࡖࡆ࡚ࡏࡓࠩࡎ"), l1ll1l_opy_ (u"࠭ࠧࡏ")]
    prompt = l1ll1l_opy_ (u"ࠧࡑࡔࡈࡗࡘࠦࡅࡏࡖࡈࡖ࡚ࠥࡏࠡࡇ࡛ࡍ࡙࠭ࡐ")
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
l1lll1l_opy_ = (window.get_width() - window.get_string_width(prompt)) // 2
window.input_string(prompt, l1lll1l_opy_, l1l1111_opy_)
#   close window
window.close()