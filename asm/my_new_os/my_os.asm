; Reference: http://mikeos.sourceforge.net/write-your-own-os.html

	BITS 16 ; In boot mode, you're in real mode, 16 bits

start:

	mov ax, 07C0h	; Set up 4K stack space after this bootloader
	add ax, 288		; (4096 + 512) / 16 bytes per paragraph
	mov ss, ax
	mov sp, 4096

	mov ax, 07C0h	; Set data segment to where we're loaded
	mov ds, ax

	mov si, text_string	; Put string position into source index
	call print_string	; Call the function

	jmp $			; Jump here - infinite loop!

		; 0xa for newline (move down) and 0xd for carriage return (go left)
	text_string db 'MikeOS tutorial works!', 0xa, 0xd, 'Yay!!', 0



print_string:		; Print string in SI to screen
	mov ah, 0Eh		; int 10h 'print char' function

.repeat:
	lodsb			; Get character from string
	cmp al, 0
	je .done		; If char is zero, end of string
	int 10h			; Otherwise, print it
	jmp .repeat

.done:
	ret


	times 510-($-$$) db 0	; Pad remainder of boot sector with 0s
	dw 0xAA55		; The standard PC boot signature
