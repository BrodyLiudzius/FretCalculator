import sys, math

argc:int = len(sys.argv)

length:float
n:float = 22

if argc > 1:
    length = float(sys.argv[1])
else:
    print("Please provide a scale length.")
    quit()

if argc > 2:
    n = int(sys.argv[2])

print("\nfret, distance\n==============")
[print((str(i) + ":").ljust(4) + "{:9.3f}".format(length - (length/(math.pow(2, i/12))))) for i in range(n)]