valid_encodings = []

# 遍历所有可能的组合（A=1, J=0 固定，枚举 B, C, D, E, F, G, H, I）
for b in [0, 1]:
    for c in [0, 1]:
        for d in [0, 1]:
            for e in [0, 1]:
                for f in [0, 1]:
                    for g in [0, 1]:
                        for h in [0, 1]:
                            for i in [0, 1]:
                                # 固定 A 和 J 的值
                                a, j = 1, 0

                                # 排除条件
                                cond1 = (d == 0 and g == 1)  # 不能 D=0 且 G=1
                                cond2 = (d == 1 and g == 0)  # 不能 D=1 且 G=0
                                cond3 = (b == 1 and c == 0 and e == 0)  # 不能 B=1, C=0, E=0
                                cond4 = (f == 1 and h == 1 and i == 0)  # 不能 F=1, H=1, I=0

                                # 如果不满足任何排除条件，则记录编码
                                if not (cond1 or cond2 or cond3 or cond4):
                                    # 计算编码值 N
                                    n = (a * 2**0 + b * 2**1 + c * 2**2 + d * 2**3 +
                                         e * 2**4 + f * 2**5 + g * 2**6 + h * 2**7 +
                                         i * 2**8 + j * 2**9)
                                    valid_encodings.append(n)
                                    
# 排序编码
valid_encodings.sort()

# 输出总人数和部分编码
print("符合条件的编码总人数:", len(valid_encodings))
print("符合条件的编码:", valid_encodings[:98])
