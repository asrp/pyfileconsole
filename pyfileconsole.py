import os
import time
import traceback
in_file = "/tmp/pyconsole-in.txt"
out_file = "/tmp/pyconsole-out.txt"

reset = True
if reset:
    open(in_file, "w").write("")
    open(out_file, "w").write("")

f_in = open(in_file)
f_out = open(out_file, "a")
sep = "\n===Done===\n"

buffer_ = ""
while True:
    line = f_in.readline()
    if not line:
        time.sleep(0.1)
        continue
    elif not line.endswith("\n"):
        buffer_ += line
        continue
    line = buffer_ + line
    buffer_ = ""
    try:
        if line.startswith("eval "):
            out = eval(line[5:])
        elif line.startswith("exec "):
            out = exec(line[5:])
        else:
            print(f"Unknown command. Line: {line}")
            out = "error"
    except Exception as e:
        print(f"Unknown error while evaluating {line}")
        traceback.print_exc()
        out = "error"
    f_out.write(repr(out))
    f_out.write(sep)
    f_out.flush()
