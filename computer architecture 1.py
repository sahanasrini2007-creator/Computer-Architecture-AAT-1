
# LRU (Least Recently Used) Cache Replacement Algorithm

cache_size = 3
cache = []  # Least recently used block is at the beginning

access_sequence = [4, 2, 1, 4, 3, 2, 5, 4]

hits = 0
misses = 0

print("LRU Cache Replacement Algorithm")
print("-" * 65)
print(f"{'Block':<10}{'Status':<12}{'Cache Contents':<25}{'Removed'}")
print("-" * 65)

for block in access_sequence:

    removed = "-"

    if block in cache:
        # Block is already present: HIT
        hits += 1
        cache.remove(block)
        cache.append(block)
        status = "HIT"

    else:
        # Block is absent: MISS
        misses += 1
        status = "MISS"

        if len(cache) == cache_size:
            # Remove the least recently used block
            removed = cache.pop(0)

        cache.append(block)

    print(f"{block:<10}{status:<12}{str(cache):<25}{removed}")

print("-" * 65)

total_accesses = len(access_sequence)
hit_ratio = hits / total_accesses

print("Total Hits   :", hits)
print("Total Misses :", misses)
print("Hit Ratio    :", f"{hit_ratio:.3f}")
print("Hit Ratio (%) :", f"{hit_ratio * 100:.2f}%")
