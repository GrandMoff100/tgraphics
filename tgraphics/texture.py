from .vector import Vector
from .chars import Chars


def rev_char(char):
    return (Chars.BW.index(char)+1) / len(Chars.BW)

class Texture:
    def __init__(self, bw_texture, smooth_stretch: bool = True):
        self.tex = bw_texture
        self.smooth_stretch = smooth_stretch

    def __str__(self):
        return "\n".join([str(Vector(line, smooth_stretch=self.smooth_stretch)) for line in self.tex])

    @property
    def vvecs(self):
        return [Vector(v, smooth_stretch=self.smooth_stretch) for v in [[h[c] for h in self.tex] for c in range(len(self.tex[0]))]]

    @property
    def hvecs(self):
        return [Vector(h, smooth_stretch=self.smooth_stretch) for h in self.tex]

    def distort_h(self, factor):
        vecs = []
        for vector in self.hvecs:
            vecs.append([rev_char(x) for x in str(vector.distort(factor))])
        return Texture(vecs)

    def distort_v(self, factor):
        vecs = []
        for vector in self.vvecs:
            vecs.append([rev_char(x) for x in str(vector.distort(factor))])
        return Texture(zip(*vecs))
