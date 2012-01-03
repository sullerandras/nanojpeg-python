import nanojpeg

def main():
    nanojpeg.njInit()
    buf = open('test3.jpg', 'rb').read()
    import array
    buf = array.array('B', buf)

    import cProfile
    cProfile.runctx('nanojpeg.njDecode(buf, len(buf))', globals(), locals(), 'fooprof')
    import pstats
    p = pstats.Stats('fooprof')
    p.strip_dirs().sort_stats('time').print_stats()

    f = open("test3.ppm" if nanojpeg.njIsColor() else "test3.pgm", "wb")
    f.write("P%d\n%d %d\n255\n" % (6 if nanojpeg.njIsColor() else 5, nanojpeg.njGetWidth(), nanojpeg.njGetHeight()))
    f.write(''.join(map(chr, nanojpeg.njGetImage())))
    f.close()
    nanojpeg.njDone()

main()
