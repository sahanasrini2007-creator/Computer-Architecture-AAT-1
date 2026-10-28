
tlb_time = 10
memory_time = 80

# First TLB hit ratio
h1 = 0.90

eat1 = h1 * (tlb_time + memory_time) + (1 - h1) * (tlb_time + 2 * memory_time)

print("TLB Hit Ratio:", h1)
print("TLB Lookup Time:", tlb_time, "ns")
print("Memory Access Time:", memory_time, "ns")
print("Effective Access Time:", eat1, "ns")

print()

# Second TLB hit ratio
h2 = 0.75

eat2 = h2 * (tlb_time + memory_time) + (1 - h2) * (tlb_time + 2 * memory_time)

print("TLB Hit Ratio:", h2)
print("Effective Access Time:", eat2, "ns")

print()

# Compare both results
if eat1 < eat2:
    print("TLB hit ratio 0.90 gives better performance.")
elif eat2 < eat1:
    print("TLB hit ratio 0.75 gives better performance.")
else:
    print("Both give the same performance.")
