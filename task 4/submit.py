def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return signature[:2]
    else:
        seq = signature[:]
        for _ in range(2, n):
            seq.append(sum(seq[-3:]))
        return seq[:n]