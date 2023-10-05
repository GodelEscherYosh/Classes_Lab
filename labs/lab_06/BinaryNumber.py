import math


class BinaryNumber():
    def __init__(self, bits: list[int]):
        self.bits = bits

    def __str__(self):
        return f"{self.bits}"
    

    def __or__(self, other: "BinaryNumber") -> list[int]:
        bit = []
        for i in range(len(other.bits)):
            if self.bits[i] == 1 or other.bits[i] == 1:
                bit.append(1)
            else:
                bit.append(0)

        return bit

    def __and__(self, other: "BinaryNumber") -> list[int]:
        bit = []
        for i in range(len(self.bits)):
            if self.bits[i] == 1 and other.bits[i] == 1:
                bit.append(1)
            else:
                bit.append(0)

        return bit


    def left_shift(self):
        """0010 << 1  →  0100"""
        self.bits = self.bits[1:]
        self.bits.append(0)


    def right_shift(self):
        """0010 >> 1  →  0001"""
        self.bits = self.bits[: -1]
        self.bits.insert(0)
bit = [0,0,1,0]
print(bit[: -1])
print(bit[1:])



bit[: -1] = bit[1:]



print(bit)


# bn = BinaryNumber([1,0,1,0,1])
# bn2 = BinaryNumber([1,1,1,0,0])
# print("1st binary number =",bn)
# 1st binary number = [1, 0, 1, 0, 1]

# print("2nd binary number =", bn2)
# 2nd binary number = [1, 1, 1, 0, 0]

# print("AND",bn & bn2)
# AND [1, 0, 1, 0, 0]

# print("OR", bn | bn2)
# OR [1, 1, 1, 0, 1]

# bn.right_shift()
# print("1st number right-shifted =", bn)
# 1st number right-shifted = [0, 1, 0, 1, 0]

# bn.left_shift()
# print("1st number left-shifted =", bn)
# 1st number left-shifted = [1, 0, 1, 0, 0]


bn = BinaryNumber([1,0,1,0,1])
