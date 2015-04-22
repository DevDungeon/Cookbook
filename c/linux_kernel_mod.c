/* A basic Linux kernel module in C */

#include <linux/module.h>	/* Needed by all modules */
#include <linux/kernel.h>	/* Needed for KERN_INFO */

int init_module(void) {
	printk(KERN_INFO "Sample kernel module loaded!\n");

	/* 0 = success; non-zero = failure to load */
	return 0;
}

void cleanup_module(void) {
	printk(KERN_INFO "Sample kernel module unloaded.\n");
}