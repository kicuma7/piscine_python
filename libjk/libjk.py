def jk_len(obj):
    i = int(0)
    while obj[i:i + 1]:
        i += 1
    return (i)

class jk_str(str):
    def jk_upper(self):
        i = int(0)
        while (self[i: i + 1]):
            if (ord(self[i]) >= 97 and ord(self[i]) <= 122):
                temp = self[:i] + chr(ord(self[i]) - 32) + self[i + 1:]
                self = temp
            i += 1
        return (self)

    def jk_lower(self):
        i = int(0)
        while (self[i:i + 1]):
            if (ord(self[i]) >= 65 and ord(self[i]) <= 90):
                temp = self[:i] + chr(ord(self[i]) + 32) + self[i + 1:]
                self = temp
            i += 1
        return (self)

    def jk_find(self, *args):
        begin = 0
        end = jk_len(self)

        if (jk_len(args) > 3 or jk_len(args) < 1):
            raise ValueError('Quantidades de argumentos invalida!')
        to_find = str(args[0])
        if (jk_len(to_find) > jk_len(self)):
            return (-1)
        elif (jk_len(to_find) == 0):
            return (0)

        if (jk_len(args) >= 2 and jk_len(args) <= 3):
            begin = int(args[1])
            if (jk_len(args) == 3):
                end = int(args[2])
                if (end > jk_len(self)):
                    end = int(jk_len(str(args[0])))
        while (begin < end and self[begin:]):
            j = 0
            if (self[begin] == to_find[j]):

            begin += 1





    def jk_split(self, *args):
        char = ' '
        qtd_splits = int(0)
        if (jk_len(args) > 2 or jk_len(args) < 1):
            raise ValueError('A funcao tem mais de 2 parametros')
        elif (jk_len(args) == 1):
            char = args[0]
        else:
            char = args[0]
            qtd_splits = int(args[1])


j = jk_str('JOSEPH')
print(j.jk_find('', 0, 100))
print(j.find('', 0, 100))
