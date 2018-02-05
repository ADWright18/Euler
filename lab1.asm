#	Comments.  Anything after # is comments.
#	MIPS Example

	.data				#data segment
newline:	.asciiz "\n"			#ASCII for a new line. asciiz with z means 0 (not character '0') is placed after the last character.
	.align 2			# The next variable (symbol) should starts at an address that is a multiple of 4.
name:	.asciiz "CSE3666: Lab 0: Rania Chowdhury \n\n\n"
	.align 2
msg1:	.asciiz "\nThe integer you just typed is\n"
	.align 2
buf:	.space 128			# Reserve space for a variable (array). Not initialized.

	.align 2
reserved:	.space 20

	.text				# Code segment
	.globl	main			# declare main to be global

main:
	# load an address, which is a 32-bit value.
	# Could be a symbol. See the example below. Still, the value is a 32-bit value.
	# la is a pseudo instruction.It is converted into two instructions.
	#la	$a0, 0xBF63C886

	# Load a large constant with two instructions. Higher 16 bits will be 0 although the MSB of the constant is 1.
	#lui	$a0, 0xBF63
	#ori	$a0, 0xC886

	# example of subtraction
	#sub	$a0, $a0, 1

	# system call no. 8, read a string.
	# The address of the buffer 'buf', which stores the returned string, is specified by $a0.
	# Notice that buf is a label. You can consider it as a 32-bit constant. So you can load it directly into a register.
	# The max length of the buffer is spacified in $a1. Try type a long string and see what happens.

	#la	$a0, buf
	#li	$a1, 10		# load a small constant (signed).
	#li	$v0, 8		# prepare a system call. Type 8.
	#syscall			# read a string

	# system call no. 4, output a string that is ended with a NULL (0) byte.
	# msg1 is a label. Again, you can consider it as a 32-bit constant.
	#la	$a0, msg1
	#li	$v0, 4
	#syscall

	#la	$a0, buf
	#li	$v0, 4		# system call, type 4, print an string, *$a0
	#syscall			# call the "OS"


				#new part**
	li	$v0, 5		#prepare to read integer 1
	syscall			#system call to read integer 1

	add	$s0, $v0, $zero	#set s0 as the v0 (integer 1)
	li	$v0, 5		#prepare to read integer 2
	syscall			#system call to read integer 2

	move	$s2, $v0	#set s2 as the v0 (integer 2)
	la	$t0, buf	#load the starting address of buf (?) into this temporary value, t0
	sll	$s0, $s0, 2	#
	add	$t0, $t0, $s0	#calculate the address of buf[$s0] by adding t0 to s0 and storing it in t0
	sw	$s2, ($t0)	#store the value of $s2 into buf[$s0] **

	la	$a0, msg1	#display the message from line 9
	li	$v0, 4		#outprint the integer
	syscall

	lw $t0, buf
	li $v0, 1
	syscall

	la	$a0, newline	#create a new line
	li	$v0, 4		#outprint the new line
	syscall

	lw	$s2, ($t0)	#load the value of t0 into s2
	li	$v0, 34		#display this value in hexadecimal
	syscall

Exit:	li	$v0, 10		# System call, type 10, standard exit
	syscall
