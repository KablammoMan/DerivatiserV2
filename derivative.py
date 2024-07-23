class Term:
    """
    A mathematical term.\n
    `type` (int) - special types of functions, e.g. trig, inverse trig\n
    `base` (term) - base of term\n
    `coef` (term) - coeficient of term\n
    `expo` (term) - exponent of term\n
    `x` (bool) - is this 'x'
    """
    def __init__(self, type, base, coef, expo, x: bool):
        self._type = type
        self._coef = coef
        self._base = base
        self._expo = expo
        self._x = x

    def get_data(self):
        data = {}
        data.type = self._type2name(self._type)
        data.coef = self._coef
        data.base = self._base
        data.expo = self._expo

        return data

    def _type2name(self, type):
        subs = {
            0: "reg",
            1: "cos",
            2: "sin",
            3: "tan",
            4: "acos",
            5: "asin",
            6: "atan"
        }
        return subs[type]

x = Term(0, )
