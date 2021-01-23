from cipher import FileDecoder
from cipher import password_validator
import datetime


def __main__():
    decrypted = []
    file_bool = False
    curr = False
    curr2 = False
    key = ''
    file = ''
    while not file_bool:
        if not file_bool:
            file = input("Enter File: ")
            if file == 'q':
                return 0
            try:
                fo = open(file)
                fo.close()
                file_bool = True
            except:
                print("File does not exist")

    while not curr2:
        while not curr:
            key = input("Enter Password: ")
            if key == 'q' or file == 'q':
                return 0
            curr = password_validator(key, file)

        try:
            FileDecoder.decrypt(FileDecoder(key, file), key, file)
            break
        except:
            print("Invalid Password")
            key = input("Enter Password: ")
            if key == 'q':
                return 0

    csvfile = FileDecoder(file, key)

    for x in csvfile:
        decrypted.append(x)
    decrypted.pop(0)
    decrypted.pop()
    jan = []
    feb = []
    march = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    octo = []
    nov = []
    dec = []
    data = [jan, feb, march, apr, may, jun, jul, aug, sep, octo, nov, dec]
    for x in decrypted:
        x = x.split(',')
        (data[int(x[9]) - 1]).append(
            datetime.datetime(int(x[8]), int(x[9]), int(x[10]), int(x[11]), int(x[12])) - datetime.datetime(int(x[3]),
                                                                                                            int(x[4]),
                                                                                                            int(x[5]),
                                                                                                            int(x[6]),
                                                                                                            int(x[7])))

    sum = [datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now(),
           datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now(),
           datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now(),
           datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now(),
           datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now(),
           datetime.datetime.now() - datetime.datetime.now(), datetime.datetime.now() - datetime.datetime.now()]
    ind = 0
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mar', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    print("RESULTS\nFileDecoder: FileDecoder(key='" + key + "', file='" + file + "')")
    print("ENTRIES", len(csvfile))
    for j in data:

        for i in j:
            sum[ind] += i
        if len(data[ind]) != 0:
            print("Average delay for ", months[ind], "{:.2f}".format((sum[ind] / len(data[ind])).total_seconds() / 60))
        ind += 1
    print("END")


if __name__ == "__main__":
    __main__()
