H, M = map(int, input().split)


if M > 45:
    M -= 45
else:
    M = M + 60 - 45
    H = H - 1 if H > 0 else 23

print(H, M)