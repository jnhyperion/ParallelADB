import os
from ._exceptions import OfflineDevicesError


class _DevicesMgr:

    def __init__(self):
        self._serials = list()

    def get_serials(self):
        if not self._serials:
            self.get_serials_instantly()
        return self._serials

    def get_serials_instantly(self):
        result = os.popen('adb devices').read()
        for r in result.split('\n'):
            r = r.strip()
            if r.endswith('\tdevice'):
                device = r.split('\t')[0]
                self._serials.append(device)
        if not self._serials:
            raise OfflineDevicesError('No devices!!!')
        return self._serials


DevicesMgr = _DevicesMgr()
