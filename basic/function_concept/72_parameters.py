def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10)) # Returns -5
print(minimum(1, 5, 2, -5, 10, clip=0)) # Returns 0