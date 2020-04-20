# Unique Homework Generator

<em>By [hydrodog](https://github.com/hydrodog) and [PMARINA](https://github.com/PMARINA) </em>

---

<h2>To Use:</h2>
<ol>
<li>

[Get Python](https://www.python.org/downloads/)

</li>
<li>
Write your template file. Supported functions:
<ul>
<li>

Shift Instructions: `$ish`: `lsl/lsr/rol/ror`

</li>
<li>

Arithmetic & Logical Instructions: `$arith`: `add/sub/and/orr/eor`

</li>
<li>

Unnamed Functions: `$fn` (`n` evaluates to a number, in order of usage)

</li>
<li>

Unsigned 8-bit numbers: `$u8`

</li>
<li>

Main named functions: `$lab`

</li>
<li>
And other custom functions:
<ul>
<li>

`$hb`

</li>
<li>

`$hw`

</li>
<li>

`$sh`

</li>
<li>

`$countDown`

</li>
</ul>
</li>
</ul>
</li>
<li>

Run our generator: `python3 generator.py template_file number_assignments_to_generate`</li>

</ol>

<h2>Future Improvements:</h2>
<ul>
<li>Support for easy creation of custom variables</li>
</ul>
