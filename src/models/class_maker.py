
import sys


name = sys.argv[1]
list_of_pram = [sys.argv[i] for i in range(2, len(sys.argv))]
params = "self, "
this = ""

f = open(f"{sys.argv[1]}.py", 'a')
for itm in list_of_pram:
    this += f'self._{itm} = {itm}\n\t\t'
    params += f'{itm}, '
init_def = f"class {name}:\n\tdef __init__({params}):\n\t\t{this}"
f.write(init_def)

for item in list_of_pram:
    g = f"\n\tdef get_{item}(self):\n\t\treturn self._{item}\n"
    s = f"\n\tdef set_{item}(self, new_{item}):\n\t\tself._{item} = new_{item}\n"
    f.write(g)
    f.write(s)



f.close()