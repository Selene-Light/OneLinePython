print("".join([" ".join(["%d*%d=%d" % (j, i, i*j) for j in range(1, i+1)])+"\n" for i in range(1, 10)]))
