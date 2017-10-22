class Helper:
    # Compare dicts not including "timestamp" key
    def __check_dict_equality(self, d1, d2, ignore_key):
        ret = {k: v for k,v in d1.items() if k not in ignore_key} == {k: v for k,v in d2.items() if k not in ignore_key}
        return ret

    # Remove consecutive duplicate log entries
    def remove_concecutive_dups(self, d, ignore_key):
        l = len(d)
        if (l > 1):
            # Iterate backwards, removing elements as necessary
            for i in reversed(range(1, l)):
                # If equal, delete ith element
                if self.__check_dict_equality(d[i], d[i - 1], ignore_key):
                    del d[i]
        return d

    # Remove all duplicate log entries
    # The first logs in the file are the ones that will remain
    def remove_all_dups(self, d, ignore_key):
        seen = []
        ret = []
        for e in d:
            dup = False
            # Compare e to all "seen" elements
            for s in seen:
                if (self.__check_dict_equality(e, s, ignore_key)):
                    dup = True
                    break;
            if (dup):
                continue
            # Add element to seen and return lists
            seen.append(e)
            ret.append(e)
        return ret
