from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    IPictureDisp, Color, OLE_XPOS_CONTAINER, FontEvents,
    OLE_XPOS_HIMETRIC, IFont, VgaColor, dispid, OLE_ENABLEDEFAULTBOOL,
    Default, Library, VARIANT_BOOL, FONTSTRIKETHROUGH, Gray,
    OLE_XSIZE_HIMETRIC, OLE_YSIZE_CONTAINER, DISPPROPERTY, GUID,
    OLE_YSIZE_HIMETRIC, IDispatch, COMMETHOD, _lcid, FONTITALIC,
    IEnumVARIANT, DISPPARAMS, FONTBOLD, StdPicture,
    OLE_XSIZE_CONTAINER, StdFont, OLE_YSIZE_PIXELS, OLE_XSIZE_PIXELS,
    Checked, IUnknown, CoClass, FONTSIZE, OLE_YPOS_PIXELS, Monochrome,
    OLE_YPOS_HIMETRIC, FONTUNDERSCORE, HRESULT, IFontEventsDisp,
    OLE_OPTEXCLUSIVE, Unchecked, _check_version, BSTR, IFontDisp,
    OLE_CANCELBOOL, IPicture, OLE_YPOS_CONTAINER, EXCEPINFO, FONTNAME,
    OLE_XPOS_PIXELS, DISPMETHOD, OLE_COLOR, Picture, OLE_HANDLE,
    typelib_path, Font
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'IPictureDisp', 'StdFont', 'OLE_YSIZE_PIXELS', 'OLE_XSIZE_PIXELS',
    'Color', 'Checked', 'FONTSIZE', 'OLE_YPOS_PIXELS', 'Monochrome',
    'OLE_XPOS_CONTAINER', 'OLE_YPOS_HIMETRIC', 'FontEvents',
    'FONTUNDERSCORE', 'IFontEventsDisp', 'OLE_OPTEXCLUSIVE',
    'Unchecked', 'OLE_XPOS_HIMETRIC', 'IFont', 'VgaColor',
    'IFontDisp', 'OLE_CANCELBOOL', 'IPicture',
    'OLE_ENABLEDEFAULTBOOL', 'OLE_YPOS_CONTAINER', 'FONTNAME',
    'Default', 'OLE_XPOS_PIXELS', 'Library', 'OLE_COLOR',
    'FONTSTRIKETHROUGH', 'Picture', 'OLE_HANDLE', 'typelib_path',
    'Gray', 'OLE_XSIZE_HIMETRIC', 'OLE_YSIZE_CONTAINER', 'FONTITALIC',
    'OLE_YSIZE_HIMETRIC', 'Font', 'LoadPictureConstants', 'FONTBOLD',
    'StdPicture', 'OLE_TRISTATE', 'OLE_XSIZE_CONTAINER'
]

