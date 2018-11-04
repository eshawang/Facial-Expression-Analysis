import csv
from face import Face

data = csv.DictReader(open("fer2013/fer2013.csv"))
faces_train = []
faces_val = []
faces_test = []

for row in data:
    if row.get("Usage") == "Training":
        faces_train += [Face(row)]
    elif row.get("Usage") == "PublicTest":
        faces_val += [Face(row)]
    elif row.get("Usage") == "PrivateTest":
        faces_test += [Face(row)]

print((len(faces_train), len(faces_val), len(faces_test)))
