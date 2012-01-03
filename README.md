NanoJPEG -- KeyJ's Tiny Baseline JPEG Decoder -- ported to Python
=================================================================

version 1.1 (2010-03-05)

by Martin J. Fiedler <martin.fiedler@gmx.net>

[http://keyj.emphy.de/nanojpeg/](http://keyj.emphy.de/nanojpeg/)

This software is published under the terms of KeyJ's Research License,
version 0.2. Usage of this software is subject to the following conditions:

0.  There's no warranty whatsoever. The author(s) of this software can not
    be held liable for any damages that occur when using this software.

1.  This software may be used freely for both non-commercial and commercial
    purposes.

2.  This software may be redistributed freely as long as no fees are charged
    for the distribution and this license information is included.

3.  This software may be modified freely except for this license information,
    which must not be changed in any way.

4.  If anything other than configuration, indentation or comments have been
    altered in the code, the original author(s) must receive a copy of the
    modified code.

Ported to python by Andras Suller <suller.andras@gmail.com>, 2012 January 03
[https://github.com/sullerandras/nanojpeg-python](https://github.com/sullerandras/nanojpeg-python)

VERSION HISTORY
---------------

2012 January 03 -- first working release


WHY?
----

I couldn't find a pure Python JPEG decompressor which has a good quality.
PIL is not available in Goolge App Engine, and I will use this library there.


REMARKS
-------

There may be bugs in the porting, but it is good enough for me.

Some parts are not converted. For example, it doesn't support
grayscale JPEGs and always use chroma upscaling.

Performance is awful, it needs 12 seconds to decompress a 400x400 pixel image
on my core2duo machine, compared to the original C code's 0.2 seconds.

No test suite, since I have no idea how the JPEG decompression is working.
I only translated it to Python.

