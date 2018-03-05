import csv
import io


def yield_increasing_datapoints(data):
    rows = csv.reader(data, delimiter='\t')

    current_value = 0.0

    for row in rows:
        if float(row[1]) >= current_value:
            current_value = float(row[1])
            yield row + [
                True,
            ]
        else:
            yield row + [
                False,
            ]


def clean_data(data):
    output = io.StringIO()
    writer = csv.writer(output)

    for row in yield_increasing_datapoints(
            io.StringIO(data.decode()).readlines()):
        writer.writerow(row)

    return output.getvalue().encode()
