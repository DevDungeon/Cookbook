# https://www.rubydoc.info/gems/win32-api/1.4.8
# # gem install win32-api
#
require 'win32/api'
include Win32

# Typical example - Get user name
buf = 0.chr * 260
len = [buf.length].pack('L')

GetUserName = API.new('GetUserName', 'PP', 'I', 'advapi32')
GetUserName.call(buf, len)

puts buf.strip

# Callback example - Enumerate windows
EnumWindows     = API.new('EnumWindows', 'KP', 'L', 'user32')
GetWindowText   = API.new('GetWindowText', 'LPI', 'I', 'user32')
EnumWindowsProc = API::Callback.new('LP', 'I'){ |handle, param|
    buf = "\0" * 200
    GetWindowText.call(handle, buf, 200);
    puts buf.strip unless buf.strip.empty?
    buf.index(param).nil? ? true : false
}

EnumWindows.call(EnumWindowsProc, 'UEDIT32')

# Raw function pointer example - System beep
LoadLibrary    = API.new('LoadLibrary', 'P', 'L')
GetProcAddress = API.new('GetProcAddress', 'LP', 'L')

hlib = LoadLibrary.call('user32')
addr = GetProcAddress.call(hlib, 'MessageBeep')
func = Win32::API::Function.new(addr, 'L', 'L')
func.call(0)