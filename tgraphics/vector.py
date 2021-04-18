from .chars import Chars
import math


def frange(start, end, step):
    counter = start
    while counter < end:
        yield counter
        counter += step


class Vector:
    def __init__(self, bw_vals, smooth_stretch: bool = True):
        self.vals = bw_vals
        self.distortion: float = 1
        self.smooth_stretch = smooth_stretch

    def __str__(self):
        result = ""
        for interval in frange(0, len(self.vals)-1, self.distortion):
            if self.smooth_stretch:
                fi = interval - math.floor(interval)
                ic = math.ceil(interval) - interval

                icv = self.vals[math.floor(interval)] * ic
                fiv = self.vals[min(math.ceil(interval), len(self.vals)-1)] * fi

                adj_val = (
                    icv if ic else self.vals[math.floor(interval)]
                ) + (
                    fiv if fi else 0
                )
            else:
                adj_val = self.vals[min(round(interval), len(self.vals))]

            result += Chars.BW[int(adj_val * (len(Chars.BW) - 1))]
        result += Chars.BW[int(self.vals[-1] * (len(Chars.BW) - 1))]
        return result

    def distort(self, distortion):
        self.distortion = distortion
        return self
