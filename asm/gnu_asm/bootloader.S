# Reference: https://gist.github.com/rain-1/52a0be541364d0212a8b526396503c7a
# Reference: https://50linesofco.de/post/2018-02-28-writing-an-x86-hello-world-bootloader-with-assembly
.code16

.global _start

_start:
	cli
	xor	%ax, %ax
	mov	%ax, %ds
	mov	$msg, %si
	cld

print_string:
  # Loop, printing one character at a time until null delimiter is reached
	lodsb
	or	%al, %al  # AL contains character to print. Is it null?
	jz	hang      # We're done when the next char up is null
	mov	$0x0E, %ah  # Print character
	mov	$0x00, %bh
	int	$0x10  # Trigger BIOS interrupt https://en.wikipedia.org/wiki/INT_10H
	jmp	print_string

hang:
	jmp	hang

msg:
	.string "Hello, world!"
    .byte 0x0D,0x0A
    .string "Hello on another line!"
	.byte 0x0D, 0x0A, 0x00  # /r, /n, null

# OR:
# msg: .asciz "Hello world!"



.org 510  # Jump to offset 510, filling with 0 in between
# OR: .fill 510-(.-_start), 1, 0

.byte 0x55, 0xAA  # Designate as bootable
# OR: .word 0xaa55
