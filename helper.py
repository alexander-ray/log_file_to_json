class Helper:
    def __check_dict_equality(self, d1, d2, ignore_key):
        ret = {k: v for k,v in d1.items() if k not in ignore_key} == {k: v for k,v in d2.items() if k not in ignore_key}
        return ret

    def remove_concecutive_dups(self, d, ignore_key):
        l = len(d)
        if (l > 1):
            for i in reversed(range(1, l)):
                if self.__check_dict_equality(d[i], d[i - 1], ignore_key):
                    del d[i]
        return d

    def remove_all_dups(self, d, ignore_key):
        seen = []
        ret = []
        for e in d:
            dup = False
            for s in seen:
                if (self.__check_dict_equality(e, s, ignore_key)):
                    dup = True
                    break;
            if (dup):
                continue
            seen.append(e)
            ret.append(e)
        return ret
