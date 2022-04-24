

import psutil
from functools import partial
from .base import SysInfoBase


class TemperatureInfo(SysInfoBase):
    def __init__(self, *args):
        super(TemperatureInfo, self).__init__(*args)

    def install(self):
        super(TemperatureInfo, self).install()
        result = psutil.sensors_temperatures()
        for device in result.keys():
            zones = result[device]
            if len(zones) == 1:
                self._items[device] = partial(self._read_temp, device, 0)
            else:
                self._items[device] = SysInfoBase(self.actual)
                for idx, zone in enumerate(zones):
                    self._items[device].items[zone.label] = partial(self._read_temp, device, idx)

    def _read_temp(self, device, zone):
        return psutil.sensors_temperatures()[device][zone].current

