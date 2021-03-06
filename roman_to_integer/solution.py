class Solution:
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    group_one = ['I', 'X', 'C', 'M']
    group_five = ['V', 'L', 'D']

    def romanToInt(self, s: str) -> int:
        size = len(s)

        if size == 1:
            return self.data[s]

        if size == 2:
            n0 = self.data[s[0]]
            n1 = self.data[s[1]]
            return n1 - n0 if n1 > n0 else n1 + n0

        result = 0

        p = len(s) - 1

        while p > 0:
            c = s[p]

            if c in self.group_one:
                n = s[p - 1]
                cv = self.data[c]
                nv = self.data[n]
                if cv > nv:
                    result = result + self.romanToInt(s[p - 1:p + 1])
                    p = p - 2
                else:
                    count = 0
                    while p > 0 and s[p] == c:
                        count = count + 1
                        p = p - 1

                    result = result + (self.data[c] * count)

            elif c in self.group_five:
                n = s[p - 1]
                cv = self.data[c]
                nv = self.data[n]
                if cv > nv:
                    result = result + (cv - nv)
                    p = p - 2
                else:
                    result = result + cv
                    p = p - 1

            if p < 0:
                break

            if p == 0:
                result = result + self.romanToInt(s[0])
                break

            if p == 1:
                result = result + self.romanToInt(s[0:2])
                break

        return result
