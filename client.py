import time
in_file = "/tmp/pyconsole-out.txt"
out_file = "/tmp/pyconsole-in.txt"

f_in = open(in_file)
f_out = open(out_file, "a")
sep = "===Done===\n"

line = True
while line:
    line = f_in.readline()
    print(line, end='')

while True:
    out_line = input()
    f_out.write(f"{out_line}\n" if out_line.startswith("eval") else f"exec {out_line}\n")
    f_out.flush()
    line = None
    while line != sep:
        line = f_in.readline()
        if not line:
            time.sleep(0.1)
        print(line, end='')
