"""
In this file, you need to add your FileDecoder class
See a4 PDF for details

WE WILL EVALUATE YOUR CLASS INDIVIDUAL, SO MAKE SURE YOU READ
THE SPECIFICATIONS CAREFULLY.
"""
import re
import string


class Error(Exception):
    pass


class DecryptException(Error):
    pass


def password_validator(password, file):
    a = re.match(r"^.*[0-9]+.*[0-9]+.*$", password)  # check digits
    b = re.match(r"^[^!@#$&*\-_.]*[!@#$&*\-_.][^!@#$&*\-_.]*[!@#$&*\-_.][^!@#$&*\-_.]*$",
                 password)  # check special chars
    c = re.match(r"^[^A-Z]*[A-Z]+[^A-Z]*$", password)  # check Capital letter
    d = re.match(r"^\S{6,8}$", password)  # check length
    if (a and b) and (c and d):
        return True
    else:
        return False


class FileDecoder:
    ListOfRows = []

    def __init__(self, file, key):
        self.file = file
        self.key = key
        if password_validator(key, file):
            FileDecoder.decrypt(self, key, file)
        # print(FileDecoder.ListOfRows)

    def __iter__(self):
        return iter(FileDecoder.ListOfRows)

    def decrypt(self, key, file):
        fo = open(file, "r")
        txt = fo.read()
        fo.close()
        l = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " \n"
        key = [l.index(x) + 1 for x in key]
        n = 0
        decrypted = ""
        for c in txt:
            n += 1
            c_num = l.index(c)
            k = key[n % len(key) - 1] - 1
            if k > c_num:
                decrypted += l[c_num + len(l) - k]
            else:
                decrypted += l[c_num - k]
        #print(decrypted)
        if re.match(r'departure_terminal', decrypted) and re.search(r'scheduled_departure_year', decrypted):
            FileDecoder.ListOfRows = decrypted.split('\n')

            return iter(self)
        else:
            raise DecryptException

    def __len__(self):
        return len(FileDecoder.ListOfRows) - 1

    def __str__(self):
        return "FileDescriptor(key='" + self.key + "', file='" + self.file + ")\n"
