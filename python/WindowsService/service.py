# python -m pip install pywin32
# Example: https://github.com/mhammond/pywin32/blob/master/win32/Demos/service/serviceEvents.py
import socket

from servicemanager import LogMsg, EVENTLOG_INFORMATION_TYPE, PYS_SERVICE_STARTED, PYS_SERVICE_STOPPED
from win32serviceutil import ServiceFramework, HandleCommandLine
from win32event import CreateEvent, SetEvent, WaitForSingleObject, INFINITE
from win32service import SERVICE_STOP_PENDING, SERVICE_RUNNING

class MyService(ServiceFramework):

    _svc_name_ = 'myService'
    _svc_display_name_ = '1My Cool Service'
    _svc_description_ = 'Custom service written in Python with pywin32'

    def __init__(self, args):
        ServiceFramework.__init__(self, args)
        self.hWaitStop = CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(SERVICE_STOP_PENDING)
        SetEvent(self.hWaitStop)


    def SvcDoRun(self):
        LogMsg(EVENTLOG_INFORMATION_TYPE,
               PYS_SERVICE_STARTED,
               (self._svc_name_, ''))

        self.ReportServiceStatus(SERVICE_RUNNING)

        self.main_loop()

        WaitForSingleObject(self.hWaitStop, INFINITE)

        LogMsg(EVENTLOG_INFORMATION_TYPE,
               PYS_SERVICE_STOPPED,
               (self._svc_name_, ''))

    def main_loop(self):
        while True:
            pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        import servicemanager
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        HandleCommandLine(MyService)

