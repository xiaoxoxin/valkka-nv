# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_valkka_nv')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_valkka_nv')
    _valkka_nv = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_valkka_nv', [dirname(__file__)])
        except ImportError:
            import _valkka_nv
            return _valkka_nv
        try:
            _mod = imp.load_module('_valkka_nv', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _valkka_nv = swig_import_helper()
    del swig_import_helper
else:
    import _valkka_nv
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

from valkka import core 
class FrameFilter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FrameFilter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FrameFilter, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _valkka_nv.delete_FrameFilter
    __del__ = lambda self: None
FrameFilter_swigregister = _valkka_nv.FrameFilter_swigregister
FrameFilter_swigregister(FrameFilter)

class DummyFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DummyFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DummyFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, verbose=True, next=None):
        this = _valkka_nv.new_DummyFrameFilter(name, verbose, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_DummyFrameFilter
    __del__ = lambda self: None
DummyFrameFilter_swigregister = _valkka_nv.DummyFrameFilter_swigregister
DummyFrameFilter_swigregister(DummyFrameFilter)

class InfoFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InfoFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InfoFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_InfoFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_InfoFrameFilter
    __del__ = lambda self: None
InfoFrameFilter_swigregister = _valkka_nv.InfoFrameFilter_swigregister
InfoFrameFilter_swigregister(InfoFrameFilter)

class BriefInfoFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BriefInfoFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BriefInfoFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_BriefInfoFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_BriefInfoFrameFilter
    __del__ = lambda self: None
BriefInfoFrameFilter_swigregister = _valkka_nv.BriefInfoFrameFilter_swigregister
BriefInfoFrameFilter_swigregister(BriefInfoFrameFilter)

class ThreadSafeFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThreadSafeFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ThreadSafeFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_ThreadSafeFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_ThreadSafeFrameFilter
    __del__ = lambda self: None
ThreadSafeFrameFilter_swigregister = _valkka_nv.ThreadSafeFrameFilter_swigregister
ThreadSafeFrameFilter_swigregister(ThreadSafeFrameFilter)

class ForkFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ForkFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ForkFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None, next2=None):
        this = _valkka_nv.new_ForkFrameFilter(name, next, next2)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_ForkFrameFilter
    __del__ = lambda self: None
ForkFrameFilter_swigregister = _valkka_nv.ForkFrameFilter_swigregister
ForkFrameFilter_swigregister(ForkFrameFilter)

class ForkFrameFilter3(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ForkFrameFilter3, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ForkFrameFilter3, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None, next2=None, next3=None):
        this = _valkka_nv.new_ForkFrameFilter3(name, next, next2, next3)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_ForkFrameFilter3
    __del__ = lambda self: None
ForkFrameFilter3_swigregister = _valkka_nv.ForkFrameFilter3_swigregister
ForkFrameFilter3_swigregister(ForkFrameFilter3)

class ForkFrameFilterN(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ForkFrameFilterN, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ForkFrameFilterN, name)
    __repr__ = _swig_repr

    def __init__(self, name):
        this = _valkka_nv.new_ForkFrameFilterN(name)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_ForkFrameFilterN
    __del__ = lambda self: None

    def connect(self, tag, filter):
        return _valkka_nv.ForkFrameFilterN_connect(self, tag, filter)

    def disconnect(self, tag):
        return _valkka_nv.ForkFrameFilterN_disconnect(self, tag)
ForkFrameFilterN_swigregister = _valkka_nv.ForkFrameFilterN_swigregister
ForkFrameFilterN_swigregister(ForkFrameFilterN)

class SlotFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SlotFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SlotFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, n_slot, next=None):
        this = _valkka_nv.new_SlotFrameFilter(name, n_slot, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_SlotFrameFilter
    __del__ = lambda self: None
SlotFrameFilter_swigregister = _valkka_nv.SlotFrameFilter_swigregister
SlotFrameFilter_swigregister(SlotFrameFilter)

class PassSlotFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PassSlotFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PassSlotFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, n_slot, next=None):
        this = _valkka_nv.new_PassSlotFrameFilter(name, n_slot, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_PassSlotFrameFilter
    __del__ = lambda self: None
PassSlotFrameFilter_swigregister = _valkka_nv.PassSlotFrameFilter_swigregister
PassSlotFrameFilter_swigregister(PassSlotFrameFilter)

class DumpFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DumpFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DumpFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_DumpFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_DumpFrameFilter
    __del__ = lambda self: None
DumpFrameFilter_swigregister = _valkka_nv.DumpFrameFilter_swigregister
DumpFrameFilter_swigregister(DumpFrameFilter)

class CountFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CountFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CountFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_CountFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_CountFrameFilter
    __del__ = lambda self: None
CountFrameFilter_swigregister = _valkka_nv.CountFrameFilter_swigregister
CountFrameFilter_swigregister(CountFrameFilter)

class TimestampFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimestampFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimestampFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _valkka_nv.new_TimestampFrameFilter(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_TimestampFrameFilter
    __del__ = lambda self: None
TimestampFrameFilter_swigregister = _valkka_nv.TimestampFrameFilter_swigregister
TimestampFrameFilter_swigregister(TimestampFrameFilter)

class TimestampFrameFilter2(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimestampFrameFilter2, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimestampFrameFilter2, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _valkka_nv.new_TimestampFrameFilter2(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_TimestampFrameFilter2
    __del__ = lambda self: None
TimestampFrameFilter2_swigregister = _valkka_nv.TimestampFrameFilter2_swigregister
TimestampFrameFilter2_swigregister(TimestampFrameFilter2)

class DummyTimestampFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DummyTimestampFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DummyTimestampFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_DummyTimestampFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_DummyTimestampFrameFilter
    __del__ = lambda self: None
DummyTimestampFrameFilter_swigregister = _valkka_nv.DummyTimestampFrameFilter_swigregister
DummyTimestampFrameFilter_swigregister(DummyTimestampFrameFilter)

class RepeatH264ParsFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RepeatH264ParsFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RepeatH264ParsFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_RepeatH264ParsFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_RepeatH264ParsFrameFilter
    __del__ = lambda self: None
RepeatH264ParsFrameFilter_swigregister = _valkka_nv.RepeatH264ParsFrameFilter_swigregister
RepeatH264ParsFrameFilter_swigregister(RepeatH264ParsFrameFilter)

class GateFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GateFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GateFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_GateFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set(self):
        return _valkka_nv.GateFrameFilter_set(self)

    def unSet(self):
        return _valkka_nv.GateFrameFilter_unSet(self)

    def passConfigFrames(self):
        return _valkka_nv.GateFrameFilter_passConfigFrames(self)

    def noConfigFrames(self):
        return _valkka_nv.GateFrameFilter_noConfigFrames(self)
    __swig_destroy__ = _valkka_nv.delete_GateFrameFilter
    __del__ = lambda self: None
GateFrameFilter_swigregister = _valkka_nv.GateFrameFilter_swigregister
GateFrameFilter_swigregister(GateFrameFilter)

class SwitchFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwitchFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SwitchFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next1=None, next2=None):
        this = _valkka_nv.new_SwitchFrameFilter(name, next1, next2)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set1(self):
        return _valkka_nv.SwitchFrameFilter_set1(self)

    def set2(self):
        return _valkka_nv.SwitchFrameFilter_set2(self)
    __swig_destroy__ = _valkka_nv.delete_SwitchFrameFilter
    __del__ = lambda self: None
SwitchFrameFilter_swigregister = _valkka_nv.SwitchFrameFilter_swigregister
SwitchFrameFilter_swigregister(SwitchFrameFilter)

class CachingGateFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CachingGateFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CachingGateFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_CachingGateFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def set(self):
        return _valkka_nv.CachingGateFrameFilter_set(self)

    def unSet(self):
        return _valkka_nv.CachingGateFrameFilter_unSet(self)
    __swig_destroy__ = _valkka_nv.delete_CachingGateFrameFilter
    __del__ = lambda self: None
CachingGateFrameFilter_swigregister = _valkka_nv.CachingGateFrameFilter_swigregister
CachingGateFrameFilter_swigregister(CachingGateFrameFilter)

class SetSlotFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SetSlotFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SetSlotFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, next=None):
        this = _valkka_nv.new_SetSlotFrameFilter(name, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def setSlot(self, n=0):
        return _valkka_nv.SetSlotFrameFilter_setSlot(self, n)
    __swig_destroy__ = _valkka_nv.delete_SetSlotFrameFilter
    __del__ = lambda self: None
SetSlotFrameFilter_swigregister = _valkka_nv.SetSlotFrameFilter_swigregister
SetSlotFrameFilter_swigregister(SetSlotFrameFilter)

class TimeIntervalFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimeIntervalFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimeIntervalFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, mstimedelta, next=None):
        this = _valkka_nv.new_TimeIntervalFrameFilter(name, mstimedelta, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_TimeIntervalFrameFilter
    __del__ = lambda self: None
TimeIntervalFrameFilter_swigregister = _valkka_nv.TimeIntervalFrameFilter_swigregister
TimeIntervalFrameFilter_swigregister(TimeIntervalFrameFilter)

class FifoFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FifoFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FifoFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, framefifo):
        this = _valkka_nv.new_FifoFrameFilter(name, framefifo)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_FifoFrameFilter
    __del__ = lambda self: None
FifoFrameFilter_swigregister = _valkka_nv.FifoFrameFilter_swigregister
FifoFrameFilter_swigregister(FifoFrameFilter)

class BlockingFifoFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockingFifoFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BlockingFifoFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, framefifo):
        this = _valkka_nv.new_BlockingFifoFrameFilter(name, framefifo)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_BlockingFifoFrameFilter
    __del__ = lambda self: None
BlockingFifoFrameFilter_swigregister = _valkka_nv.BlockingFifoFrameFilter_swigregister
BlockingFifoFrameFilter_swigregister(BlockingFifoFrameFilter)

class SwScaleFrameFilter(FrameFilter):
    __swig_setmethods__ = {}
    for _s in [FrameFilter]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwScaleFrameFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [FrameFilter]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SwScaleFrameFilter, name)
    __repr__ = _swig_repr

    def __init__(self, name, target_width, target_height, next=None):
        this = _valkka_nv.new_SwScaleFrameFilter(name, target_width, target_height, next)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_SwScaleFrameFilter
    __del__ = lambda self: None
SwScaleFrameFilter_swigregister = _valkka_nv.SwScaleFrameFilter_swigregister
SwScaleFrameFilter_swigregister(SwScaleFrameFilter)

class Thread(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Thread, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Thread, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _valkka_nv.delete_Thread
    __del__ = lambda self: None

    def setAffinity(self, i):
        return _valkka_nv.Thread_setAffinity(self, i)

    def startCall(self):
        return _valkka_nv.Thread_startCall(self)

    def stopCall(self):
        return _valkka_nv.Thread_stopCall(self)

    def requestStopCall(self):
        return _valkka_nv.Thread_requestStopCall(self)

    def waitStopCall(self):
        return _valkka_nv.Thread_waitStopCall(self)

    def waitReady(self):
        return _valkka_nv.Thread_waitReady(self)
Thread_swigregister = _valkka_nv.Thread_swigregister
Thread_swigregister(Thread)

class FrameFifoContext(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FrameFifoContext, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FrameFifoContext, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _valkka_nv.new_FrameFifoContext(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["n_basic"] = _valkka_nv.FrameFifoContext_n_basic_set
    __swig_getmethods__["n_basic"] = _valkka_nv.FrameFifoContext_n_basic_get
    if _newclass:
        n_basic = _swig_property(_valkka_nv.FrameFifoContext_n_basic_get, _valkka_nv.FrameFifoContext_n_basic_set)
    __swig_setmethods__["n_avpkt"] = _valkka_nv.FrameFifoContext_n_avpkt_set
    __swig_getmethods__["n_avpkt"] = _valkka_nv.FrameFifoContext_n_avpkt_get
    if _newclass:
        n_avpkt = _swig_property(_valkka_nv.FrameFifoContext_n_avpkt_get, _valkka_nv.FrameFifoContext_n_avpkt_set)
    __swig_setmethods__["n_avframe"] = _valkka_nv.FrameFifoContext_n_avframe_set
    __swig_getmethods__["n_avframe"] = _valkka_nv.FrameFifoContext_n_avframe_get
    if _newclass:
        n_avframe = _swig_property(_valkka_nv.FrameFifoContext_n_avframe_get, _valkka_nv.FrameFifoContext_n_avframe_set)
    __swig_setmethods__["n_yuvpbo"] = _valkka_nv.FrameFifoContext_n_yuvpbo_set
    __swig_getmethods__["n_yuvpbo"] = _valkka_nv.FrameFifoContext_n_yuvpbo_get
    if _newclass:
        n_yuvpbo = _swig_property(_valkka_nv.FrameFifoContext_n_yuvpbo_get, _valkka_nv.FrameFifoContext_n_yuvpbo_set)
    __swig_setmethods__["n_setup"] = _valkka_nv.FrameFifoContext_n_setup_set
    __swig_getmethods__["n_setup"] = _valkka_nv.FrameFifoContext_n_setup_get
    if _newclass:
        n_setup = _swig_property(_valkka_nv.FrameFifoContext_n_setup_get, _valkka_nv.FrameFifoContext_n_setup_set)
    __swig_setmethods__["n_signal"] = _valkka_nv.FrameFifoContext_n_signal_set
    __swig_getmethods__["n_signal"] = _valkka_nv.FrameFifoContext_n_signal_get
    if _newclass:
        n_signal = _swig_property(_valkka_nv.FrameFifoContext_n_signal_get, _valkka_nv.FrameFifoContext_n_signal_set)
    __swig_setmethods__["n_marker"] = _valkka_nv.FrameFifoContext_n_marker_set
    __swig_getmethods__["n_marker"] = _valkka_nv.FrameFifoContext_n_marker_get
    if _newclass:
        n_marker = _swig_property(_valkka_nv.FrameFifoContext_n_marker_get, _valkka_nv.FrameFifoContext_n_marker_set)
    __swig_setmethods__["flush_when_full"] = _valkka_nv.FrameFifoContext_flush_when_full_set
    __swig_getmethods__["flush_when_full"] = _valkka_nv.FrameFifoContext_flush_when_full_get
    if _newclass:
        flush_when_full = _swig_property(_valkka_nv.FrameFifoContext_flush_when_full_get, _valkka_nv.FrameFifoContext_flush_when_full_set)
    __swig_destroy__ = _valkka_nv.delete_FrameFifoContext
    __del__ = lambda self: None
FrameFifoContext_swigregister = _valkka_nv.FrameFifoContext_swigregister
FrameFifoContext_swigregister(FrameFifoContext)

class DecoderThread(Thread):
    __swig_setmethods__ = {}
    for _s in [Thread]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DecoderThread, name, value)
    __swig_getmethods__ = {}
    for _s in [Thread]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DecoderThread, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _valkka_nv.new_DecoderThread(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_DecoderThread
    __del__ = lambda self: None

    def setTimeCorrection(self, val):
        return _valkka_nv.DecoderThread_setTimeCorrection(self, val)

    def getFrameFilter(self):
        return _valkka_nv.DecoderThread_getFrameFilter(self)

    def getBlockingFrameFilter(self):
        return _valkka_nv.DecoderThread_getBlockingFrameFilter(self)

    def setTimeTolerance(self, mstol):
        return _valkka_nv.DecoderThread_setTimeTolerance(self, mstol)

    def setNumberOfThreads(self, n_threads):
        return _valkka_nv.DecoderThread_setNumberOfThreads(self, n_threads)

    def decodingOnCall(self):
        return _valkka_nv.DecoderThread_decodingOnCall(self)

    def decodingOffCall(self):
        return _valkka_nv.DecoderThread_decodingOffCall(self)

    def requestStopCall(self):
        return _valkka_nv.DecoderThread_requestStopCall(self)
DecoderThread_swigregister = _valkka_nv.DecoderThread_swigregister
DecoderThread_swigregister(DecoderThread)


def NVcuInit():
    return _valkka_nv.NVcuInit()
NVcuInit = _valkka_nv.NVcuInit

def NVgetDevices():
    return _valkka_nv.NVgetDevices()
NVgetDevices = _valkka_nv.NVgetDevices
class NVThread(DecoderThread):
    __swig_setmethods__ = {}
    for _s in [DecoderThread]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NVThread, name, value)
    __swig_getmethods__ = {}
    for _s in [DecoderThread]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NVThread, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _valkka_nv.new_NVThread(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _valkka_nv.delete_NVThread
    __del__ = lambda self: None
NVThread_swigregister = _valkka_nv.NVThread_swigregister
NVThread_swigregister(NVThread)

# This file is compatible with both classic and new-style classes.


