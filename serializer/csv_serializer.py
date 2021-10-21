import csv


def load():
    with open('db.csv', 'rt') as f:
        raise ValueError('not implemented yet for new data type')
        # reader = csv.reader(f)
        # return {name: phone for name,phone in reader}


def save(db):
    raise ValueError('not implemented yet for new data type')
    # with open('db.csv', 'wt') as f:
    #     writer = csv.writer(f)
    #     for key in db.items():
    #         print('saving',key,db[key])
    #         writer.writerow([key,db[key]])
