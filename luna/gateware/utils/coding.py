from amaranth import Elaboratable, Signal, Module


__all__ = [
    "Encoder"
]


class Encoder(Elaboratable):
    """Encode one-hot to binary.

    If one bit in ``i`` is asserted, ``n`` is low and ``o`` indicates the asserted bit.
    Otherwise, ``n`` is high and ``o`` is ``0``.

    Parameters
    ----------
    width : int
        Bit width of the input

    Attributes
    ----------
    i : Signal(width), in
        One-hot input.
    o : Signal(range(width)), out
        Encoded natural binary.
    n : Signal, out
        Invalid: either none or multiple input bits are asserted.
    """
    def __init__(self, width):
        self.width = width

        self.i = Signal(width)
        self.o = Signal(range(width))
        self.n = Signal()

    def elaborate(self, platform):
        m = Module()
        with m.Switch(self.i):
            for j in range(self.width):
                with m.Case(1 << j):
                    m.d.comb += self.o.eq(j)
            with m.Default():
                m.d.comb += self.n.eq(1)
        return m

