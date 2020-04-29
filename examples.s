#by hydrodog, MIT License does not apply
#ARMv6 ASSEMBLY
#random load/and/shift problem
	.global $fn
$fn:
	ldr	r0, =0x$hw
	mov	r1, #0x$hb
	lsl	r1, #$sh
	add	r1, r0
	lsr	r1, #$sh
	ldr	r2, =0x$hw
	and	r2, r1
	bx	lr
@END
#random AND/SHIFT/OR problem
	.global $fn
$fn:
	ldr	r0, =0x$hw
	ldr	r1, =0x$hw
	$arith	r1, r0
	and	r2, r1
	lsl	r2, #$sh
	or	r2, #0x$hb
	bx	lr
@END
#random AND/XOR problem
	.global $fn
$fn:
	ldr	r0, =0x$hw
	ldr	r1, =0x$hw
	$arith	r1, r0
	and	r2, r1
	lsl	r2, #5
	eor	r2, #0x$hb
	bx	lr
@END
# random loop problem	
	.global $fn
$fn:
	mov	r1, #$u8
$lab:
	$ish	r1, #$sh
	subs	r0, #$countDown
	bne	$lab
@END
