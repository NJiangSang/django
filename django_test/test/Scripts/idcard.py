'''

进行身份证信息的校验
输入前17位数，自动计算第18位数
'''



def jiao(self):
    """

    Args:
        self:

    Returns:

    """

    def haoma_validate(self):
        if type(self) in [str, list, tuple]:
            if len(self) == 17:
                return True
        raise Exception('Wrong argument')

    if haoma_validate(self):
        if type(self) == str:
            seq = map(int, self)
        elif type(self) in [list, tuple]:
            seq = self

        t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        s = sum(map(lambda x: x[0] * x[1], zip(t, map(int, seq))))
        b = s % 11
        bd = {
            0: '1',
            1: '0',
            2: 'X',
            3: '9',
            4: '8',
            5: '7',
            6: '6',
            7: '5',
            8: '4',
            9: '3',
            10: '2'
        }

        # return bd[b]
        print(self+bd[b])
if __name__ == '__main__':
    jiao('22020020030222202')