output = []
add = 0
container = []
string = ""

with open('input', "r") as f:
    file = f.readlines()

for i in file:
    s = ''.join(i).replace("\n", "").split()
    for n in s:
        n = n.strip()
        output.append(n)

while len(output) > 0:
    for i in str(output[:1]):
        for j in i:
            if j.isdigit():
                string += j
    x = list(string)
    container.append(x)
    output.pop(0)
    string = ""

for k in container:
    first_index = k[0]
    last_index = k[-1]
    index = first_index + last_index

    output.append(index)

for a in output:
    add += int(a)
print(add)