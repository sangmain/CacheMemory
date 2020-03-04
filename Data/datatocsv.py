import pandas as pd
import numpy as np

txt = pd.read_csv("./Data/cc1.txt")

address = []
spec2006 = []
print(txt.shape)
for line in txt.values:
    address.append((line[0].split(" ")[1]))
print(address)
data =pd.DataFrame({"address": address})
data.to_csv("./Data/cc1.csv", index=False)


# address_idx = {}
# for i, item in enumerate(address):
#     address_idx[item] = address_idx.get(item, i)

# print(len(address_idx))
# addr_int = []
# data = []
# front = []
# for line in txt.values:
#     front.append(line[0].split(" ")[0])
#     addr_int.append(address_idx[line[0].split(" ")[1]])
#     data.append(line[0].split(" ")[2])
#     # for address, index in address_idx.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
#     #     if address == line[0].split(" ")[1]:
#     #         addr_int.append(index)

# print(max(address_idx))

# data =pd.DataFrame({"load/store": front, "address": addr_int, "data": data})
# data.to_csv("./Data/spec2006.csv", index=False)






# import pandas as pd
# import numpy as np

# txt = pd.read_csv("./Data/spec2006.txt")

# address = []
# spec2006 = []
# print(txt.shape)
# for line in txt.values:
#     address.append((line[0].split(" ")[1]))

# address_idx = {}
# for i, item in enumerate(address):
#     address_idx[item] = address_idx.get(item, i)

# print(len(address_idx))
# addr_int = []
# data = []
# front = []
# for line in txt.values:
#     front.append(line[0].split(" ")[0])
#     addr_int.append(address_idx[line[0].split(" ")[1]])
#     data.append(line[0].split(" ")[2])
#     # for address, index in address_idx.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
#     #     if address == line[0].split(" ")[1]:
#     #         addr_int.append(index)

# print(max(address_idx))

# data =pd.DataFrame({"load/store": front, "address": addr_int, "data": data})
# data.to_csv("./Data/spec2006.csv", index=False)

            

