

from twisted.internet.defer import inlineCallbacks
from ebs.linuxnode.core.shell import BaseShellMixin

from .base import SysInfoBase

from .host import HostInfo
from .network import NetworkInfo


class SysinfoContainer(SysInfoBase):
    def install_module(self, name, module):
        m = module(self)
        m.install()
        self._items[name] = m

    def install(self):
        self.install_module('network', NetworkInfo)
        self.install_module('host', HostInfo)


class SysinfoMixin(BaseShellMixin):
    def __init__(self, *args, **kwargs):
        super(SysinfoMixin, self).__init__(*args, **kwargs)
        self._sysinfo = SysinfoContainer(self)

    @property
    def sysinfo(self):
        return self._sysinfo

    def install(self):
        super(SysinfoMixin, self).install()
        self.sysinfo.install()

    @property
    @inlineCallbacks
    def network_info(self):
        # Legacy support
        info = yield self.sysinfo.network.info
        if 'ssid' in info.keys():
            return info['ssid']
        else:
            return info['ipaddress']
