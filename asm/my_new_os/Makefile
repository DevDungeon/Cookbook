all: my_os.asm
	mkdir build/
	# Compile
	nasm -f bin -o build/my_os_binary.bin my_os.asm
	# Create a floppy image
	dd status=noxfer conv=notrunc if=build/my_os_binary.bin of=build/my_os_floppy.flp
	mkdir iso/
	mv build/my_os_floppy.flp ./iso/
	mkisofs -no-emul-boot -input-charset iso8859-1 -o build/my_os.iso -b my_os_floppy.flp iso/
clean:
	rm -rf ./build/
	rm -rf ./iso/

run_floppy:
	# Run in qemu from floppy image
	qemu-system-i386 -fda build/my_os_floppy.flp
	# To run floppy from VirtualBox, add floppy disk drive
run_iso:
	qemu-system-i386 -cdrom build/my_os.iso
