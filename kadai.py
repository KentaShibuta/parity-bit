print("Input:")
chr = input()
input_val = bin(int(chr, 16))[2:].zfill(8)
#print("Input >>> %s" % input_val)
sev_bit = str(input_val)[1:]
#print("Sev_bit >>> %s" % sev_bit)
top_bit = str(input_val)[0]
#print("Top_bit >>> %s" % top_bit)

popcnt1 = sev_bit.count('1')
#print("Popcnt1 >>> %s" % popcnt1)

#print("odd(0) / even(1) >>> %d" % (popcnt1%2))
print('Output:')
if int(top_bit) == int(popcnt1%2):
    print('ok')
else:
    print('error')