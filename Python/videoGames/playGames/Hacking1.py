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
# l1l1l1l_opy_ l11l1ll_opy_ 1
# l11l_opy_ is a text-l1ll1lll_opy_ l11l1l_opy_ l1ll111_opy_ l11l11_opy_ that l1ll1l1_opy_ a
# list of l111l1_opy_ l1lllll_opy_ l111ll_opy_. l11llll_opy_ l1l1l11_opy_ is l11lll_opy_
# 1 l11111_opy_ to l1111l_opy_ the l11l1l_opy_. l11llll_opy_ l11l11_opy_ l1l111l_opy_ that the
# l1l1l11_opy_ l11ll11_opy_ to l1111l_opy_ the l11l1l_opy_ l11ll1_opy_.
# l1l_opy_ l1l1ll1_opy_
print(l1ll1l_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠠࡎࡑࡇࡉࠬࡑ"))
print(l1ll1l_opy_ (u"ࠩ࠴ࠤࡆ࡚ࡔࡆࡏࡓࡘ࡙࠭ࠩࠡࡎࡈࡊ࡙࠭ࡒ"))
print(l1ll1l_opy_ (u"ࠪࠫࡓ"))
# l1l_opy_ l11l1l_opy_ list
print(l1ll1l_opy_ (u"ࠫࡕࡘࡏࡗࡋࡇࡉࠬࡔ"))
print(l1ll1l_opy_ (u"࡙ࠬࡅࡕࡖࡌࡒࡌ࠭ࡕ"))
print(l1ll1l_opy_ (u"࠭ࡃࡂࡐࡗࡍࡓࡇࠧࡖ"))
print(l1ll1l_opy_ (u"ࠧࡄࡗࡗࡘࡎࡔࡇࠨࡗ"))
print(l1ll1l_opy_ (u"ࠨࡊࡘࡒ࡙ࡋࡒࡔࠩࡘ"))
print(l1ll1l_opy_ (u"ࠩࡖ࡙ࡗ࡜ࡉࡗࡇ࡙ࠪ"))
print(l1ll1l_opy_ (u"ࠪࡌࡊࡇࡒࡊࡐࡊ࡚ࠫ"))
print(l1ll1l_opy_ (u"ࠫࡍ࡛ࡎࡕࡋࡑࡋ࡛ࠬ"))
print(l1ll1l_opy_ (u"ࠬࡘࡅࡂࡎࡌ࡞ࡊ࠭࡜"))
print(l1ll1l_opy_ (u"࠭ࡎࡐࡖࡋࡍࡓࡍࠧ࡝"))
print(l1ll1l_opy_ (u"ࠧࡐࡘࡈࡖࡑࡇࡐࠨ࡞"))
print(l1ll1l_opy_ (u"ࠨࡈࡌࡒࡉࡏࡎࡈࠩ࡟"))
print(l1ll1l_opy_ (u"ࠩࡓ࡙࡙࡚ࡉࡏࡉࠪࡠ"))
print(l1ll1l_opy_ (u"ࠪࠫࡡ"))
# prompt for l1111l_opy_
input(l1ll1l_opy_ (u"ࠫࡊࡴࡴࡦࡴࠣࡴࡦࡹࡳࡸࡱࡵࡨࠥࡄࠧࡢ"))
# end l11l11_opy_
#   l1l_opy_ l1ll11l_opy_ l1l1lll_opy_
print(l1ll1l_opy_ (u"ࠬࡒࡏࡈࡋࡑࠤࡋࡇࡉࡍࡗࡕࡉࠥ࠳ࠠࡕࡇࡕࡑࡎࡔࡁࡍࠢࡏࡓࡈࡑࡅࡅࠩࡣ"))
print(l1ll1l_opy_ (u"࠭ࠧࡤ"))
print(l1ll1l_opy_ (u"ࠧࡑࡎࡈࡅࡘࡋࠠࡄࡑࡑࡘࡆࡉࡔࠡࡃࡑࠤࡆࡊࡍࡊࡐࡌࡗ࡙ࡘࡁࡕࡑࡕࠫࡥ"))
print(l1ll1l_opy_ (u"ࠨࠩࡦ"))
#   prompt for end
input(l1ll1l_opy_ (u"ࠩࡓࡖࡊ࡙ࡓࠡࡇࡑࡘࡊࡘࠠࡕࡑࠣࡉ࡝ࡏࡔࠨࡧ"))