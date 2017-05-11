
def recursive_reverse(x):
    for a in x:
        if isinstance(a, list):
            recursive_reverse(a)
    x.reverse()
    return x

print(recursive_reverse([1, [12, 3, [4, [5, 16]]]]))
