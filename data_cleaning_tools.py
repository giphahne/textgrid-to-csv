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
    print("done recording, now to tg...")
    tg.read("tempfile")

    output = io.StringIO()
    writer = csv.writer(output)

    names = tuple(
        filter(lambda x: x not in ["Orthographic", "Interviewer"],
               tg.getNames()))

    row_iters = list(map(filter_func, (tg.getFirst(n) for n in names)))
    rows = zip(*row_iters)

    names = ("minTime", "maxTime") + names

    writer.writerow(names)

    for r in filter(lambda x: not all(not i for i in x[2:]),
                    map(row_to_tuple, rows)):
        writer.writerow(r)

    return output.getvalue().encode()
