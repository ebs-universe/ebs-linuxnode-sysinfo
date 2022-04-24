

from twisted.internet.defer import inlineCallbacks


class SysInfoBase(object):
    def __init__(self, actual):
        self._actual = actual
        self._items = {}

    @property
    def actual(self):
        if hasattr(self._actual, '_actual'):
            return self._actual._actual
        else:
            return self._actual

    def _shell_execute(self, *args, **kwargs):
        self._actual._shell_execute(*args, **kwargs)

    def install(self):
        pass

    @inlineCallbacks
    def render(self):
        rval = {}
        for k, v in self._items.items():
            if hasattr(v, 'render'):
                rval[k] = yield v.render()
            elif hasattr(self, v):
                if callable(getattr(self, v)):
                    rval[k] = yield getattr(self, v)()
                else:
                    rval[k] = yield getattr(self, v)
        return rval

    def __getattr__(self, item):
        if item in self._items.keys():
            v = self._items[item]
            if not isinstance(v, str):
                return v
            if callable(getattr(self, v)):
                rval = getattr(self, v)()
            else:
                rval = getattr(self, v)
            return rval
