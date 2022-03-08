# Bootable binary that does nothing

.code16
.global _start

_start:
	jmp	_start

.org 510
.byte 0x55
.byte 0xAA
