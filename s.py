import sys
try:
    with open(sys.argv[1], "r") as file_in:
        a = file_in.read()
    with open(sys.argv[2], 'a') as file_out:
        file_out.write(a)
    print(a)

except:
    print("An exception occurred")
