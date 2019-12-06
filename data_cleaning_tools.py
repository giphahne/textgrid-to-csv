import csv
import io

import textgrid


def row_to_tuple(row):
    return (min(i.minTime
                for i in row), max(i.maxTime
                                   for i in row)) + tuple(i.mark for i in row)


def filter_func(itr):
    return filter(lambda x: x.mark != "", itr)


def clean_data(data):

    tg = textgrid.TextGrid()
    #tg.read(f=input_file)

    print("reading data into 'tempfile'...")
    with open("tempfile", "wb") as f:
        f.write(io.BytesIO(data).read())
        f.seek(0, 2)
        size = f.tell()
        print("done recording, now to tg...(read {} bytes)".format(size))
        f.seek(0, 0)
    tg.read(f="tempfile")

    print("tiers in textgrid: {}".format(tg.getNames()))
    output = io.StringIO()
    writer = csv.writer(output)

    # names = tuple(
    #     filter(lambda x: x not in ["Orthographic", "Interviewer"],
    #            tg.getNames()))

    names = tg.getNames()

    row_iters = list(map(filter_func, (tg.getFirst(n) for n in names)))
    rows = zip(*row_iters)

    names = ["minTime", "maxTime"] + names

    writer.writerow(names)

    #for r in filter(lambda x: not all(not i for i in x[2:]),
    for r in map(row_to_tuple, rows):
        writer.writerow(r)

    return output.getvalue().encode()
