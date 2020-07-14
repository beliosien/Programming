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
# l1l1l1l_opy_ l11l1ll_opy_ 6
# l11l_opy_ is a l111_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# l111lll_opy_ to 4 l11l111_opy_ to l1111l_opy_ the l11l1l_opy_. l1lll1l1_opy_ time the user
# l1llll1l_opy_ l11l1l1_opy_, the user is l1llllll_opy_ to l1111l1_opy_ a new l1111l_opy_.
# l11llll_opy_ l11l11_opy_ l1l111l_opy_ l1llll11_opy_ the l1l1l11_opy_ l1lllll1_opy_ l11l11l_opy_
# the l11l1l_opy_ or not.
from uagame import Window
from time import sleep
def main():
    location = [0,0]
    l11l111_opy_ = 4
    window = l11l11l11_opy_()
    l11ll111l_opy_(window, location, l11l111_opy_)
    l11l1l_opy_ = l11ll1l1l_opy_(window, location)
    l1111l_opy_ = l11l1l111_opy_(window, l11l1l_opy_, location, l11l111_opy_)
    l11ll1111_opy_(window, l1111l_opy_, l11l1l_opy_)
def l11l11l11_opy_():
    window = Window(l1ll1l_opy_ (u"ࠬࡎࡡࡤ࡭࡬ࡲ࡬࠭व"), 600, 500)
    window.set_font_name(l1ll1l_opy_ (u"࠭ࡣࡰࡷࡵ࡭ࡪࡸ࡮ࡦࡹࠪश"))
    window.set_font_size(18)
    window.set_font_color(l1ll1l_opy_ (u"ࠧࡨࡴࡨࡩࡳ࠭ष"))
    window.set_bg_color(l1ll1l_opy_ (u"ࠨࡤ࡯ࡥࡨࡱࠧस"))
    return window
def l11ll111l_opy_(window, location, l11l111_opy_):
    l1l1ll1_opy_ = [l1ll1l_opy_ (u"ࠩࡇࡉࡇ࡛ࡇࠡࡏࡒࡈࡊ࠭ह"), str(l11l111_opy_) + l1ll1l_opy_ (u"ࠪࠤࡆ࡚ࡔࡆࡏࡓࡘ࡙࠭ࠩࠡࡎࡈࡊ࡙࠭ऺ"), l1ll1l_opy_ (u"ࠫࠬऻ")]
    for l1111ll_opy_ in l1l1ll1_opy_:
        l11ll11ll_opy_(window, l1111ll_opy_, location)
def l11ll1l1l_opy_(window, location):
    l11111l_opy_ = [l1ll1l_opy_ (u"ࠬࡖࡒࡐࡘࡌࡈࡊ़࠭"), l1ll1l_opy_ (u"࠭ࡓࡆࡖࡗࡍࡓࡍࠧऽ"), l1ll1l_opy_ (u"ࠧࡄࡃࡑࡘࡎࡔࡁࠨा"), l1ll1l_opy_ (u"ࠨࡅࡘࡘ࡙ࡏࡎࡈࠩि"), l1ll1l_opy_ (u"ࠩࡋ࡙ࡓ࡚ࡅࡓࡕࠪी"), l1ll1l_opy_ (u"ࠪࡗ࡚ࡘࡖࡊࡘࡈࠫु"),  l1ll1l_opy_ (u"ࠫࡍࡋࡁࡓࡋࡑࡋࠬू"), l1ll1l_opy_ (u"ࠬࡎࡕࡏࡖࡌࡒࡌ࠭ृ"), l1ll1l_opy_ (u"࠭ࡒࡆࡃࡏࡍ࡟ࡋࠧॄ"), l1ll1l_opy_ (u"ࠧࡏࡑࡗࡌࡎࡔࡇࠨॅ"), l1ll1l_opy_ (u"ࠨࡑ࡙ࡉࡗࡒࡁࡑࠩॆ"), l1ll1l_opy_ (u"ࠩࡉࡍࡓࡊࡉࡏࡉࠪे"), l1ll1l_opy_ (u"ࠪࡔ࡚࡚ࡔࡊࡐࡊࠫै"), l1ll1l_opy_ (u"ࠫࠬॉ")]
    for l11l1l_opy_ in l11111l_opy_:
        l11ll11ll_opy_(window, l11l1l_opy_, location)
    return l11111l_opy_[7]
def l11l1l111_opy_(window, l11l1l_opy_, location, l111111_opy_):
    prompt = l1ll1l_opy_ (u"ࠬࡋࡎࡕࡇࡕࠤࡕࡇࡓࡔ࡙ࡒࡖࡉࠦ࠾ࠨॊ")
    l1lll1l_opy_ = 0
    l1111l_opy_ = l11ll11l1_opy_(window, prompt, location)
    l111111_opy_ = l111111_opy_ - 1
    while l1111l_opy_ != l11l1l_opy_ and l111111_opy_ > 0:
        window.draw_string(str(l111111_opy_), l1lll1l_opy_, window.get_font_height())
        l11l11lll_opy_(window, l111111_opy_)
        l1111l_opy_ = l11ll11l1_opy_(window, prompt, location)
        l111111_opy_ = l111111_opy_ - 1
    return l1111l_opy_
def l11l11lll_opy_(window, l111111_opy_):
    l111l11_opy_ = l1ll1l_opy_ (u"࠭ࠪࠫࠬࠣࡐࡔࡉࡋࡐࡗࡗࠤ࡜ࡇࡒࡏࡋࡑࡋࠥ࠰ࠪࠫࠩो")
    if l111111_opy_ == 1:
        l111ll1_opy_ = window.get_width() - window.get_string_width(l111l11_opy_)
        l1lll1ll_opy_ = window.get_height() - window.get_font_height()
        window.draw_string(l111l11_opy_, l111ll1_opy_, l1lll1ll_opy_)
def l11ll1111_opy_(window, l1111l_opy_, l11l1l_opy_):
    window.clear()
    if l1111l_opy_ == l11l1l_opy_:
        l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"ࠧࠨौ"), l1ll1l_opy_ (u"ࠨࡇ࡛ࡍ࡙ࡏࡎࡈࠢࡇࡉࡇ࡛ࡇࠡࡏࡒࡈࡊ्࠭"), l1ll1l_opy_ (u"ࠩࠪॎ"), l1ll1l_opy_ (u"ࠪࡐࡔࡍࡉࡏࠢࡖ࡙ࡈࡉࡅࡔࡕࡉ࡙ࡑ࡙ࠦ࠭ࠡࡈࡐࡈࡕࡍࡆࠢࡅࡅࡈࡑࠧॏ"), l1ll1l_opy_ (u"ࠫࠬॐ")]
        prompt = l1ll1l_opy_ (u"ࠬࡖࡒࡆࡕࡖࠤࡊࡔࡔࡆࡔࠣࡘࡔࠦࡃࡐࡐࡗࡍࡓ࡛ࡅࠨ॑")
    else:
        l1l1lll_opy_ = [l1111l_opy_, l1ll1l_opy_ (u"॒࠭ࠧ"), l1ll1l_opy_ (u"ࠧࡍࡑࡊࡍࡓࠦࡆࡂࡋࡏ࡙ࡗࡋࠠ࠮ࠢࡗࡉࡗࡓࡉࡏࡃࡏࠤࡑࡕࡃࡌࡇࡇࠫ॓"), l1ll1l_opy_ (u"ࠨࠩ॔"),l1ll1l_opy_ (u"ࠩࡓࡐࡊࡇࡓࡆࠢࡆࡓࡓ࡚ࡁࡄࡖࠣࡅࡓࠦࡁࡅࡏࡌࡒࡎ࡙ࡔࡓࡃࡗࡓࡗ࠭ॕ"), l1ll1l_opy_ (u"ࠪࠫॖ")]
        prompt = l1ll1l_opy_ (u"ࠫࡕࡘࡅࡔࡕࠣࡉࡓ࡚ࡅࡓࠢࡗࡓࠥࡋࡘࡊࡖࠪॗ")
    location = l11l1l1l1_opy_(window, l1l1lll_opy_)
    location[0] = (window.get_width() - window.get_string_width(prompt)) // 2
    l11ll11l1_opy_(window, prompt, location)
    window.close()
def l11l1l1l1_opy_(window, l1l1lll_opy_):
    l1llll1_opy_ = window.get_font_height()
    l1lll11_opy_ = (len(l1l1lll_opy_) + 1)*l1llll1_opy_
    l1l11ll_opy_ = window.get_height() - l1lll11_opy_
    l1l1111_opy_ = l1l11ll_opy_ // 2
    location = [0, l1l1111_opy_]
    for l1lll111_opy_ in l1l1lll_opy_:
        l1ll1ll_opy_ = window.get_width() - window.get_string_width(l1lll111_opy_)
        location[0] = l1ll1ll_opy_ // 2
        l11ll11ll_opy_(window, l1lll111_opy_, location)
    return location
def l11ll11ll_opy_(window, string, location):
    l1lll11l_opy_ = 0.3
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(l1lll11l_opy_)
    location[1] = location[1] + window.get_font_height()
def l11ll11l1_opy_(window, prompt, location):
    input = window.input_string(prompt, location[0], location[1])
    location[1] = location[1] + window.get_font_height()
    return input
main()