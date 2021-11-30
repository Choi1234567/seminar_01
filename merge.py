def merge(a, b):
    if isinstance(a, tuple):
        ans = list(a[:])
    else:
        ans = a.copy()
    index_a = 0
    for index_b in range(0, len(b)):
        while index_a < len(a):
            if b[index_b] <= a[index_a]:
                ans.insert(index_a + index_b, b[index_b])
                break
            else:
                index_a += 1
        else:
            ans = ans + b[index_b:]
            break
    if isinstance(a, tuple):
        return tuple(ans)
    else:
        return ans


if __name__ == '__main__':
    assert merge([1, 2, 7], [3]) == [1, 2, 3, 7]
    assert merge((3, 15), (7, 8)) == (3, 7, 8, 15)
