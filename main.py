#patient sequence:
str1 = "12309182"

#displayed sequence
str2 = "123456789"



def find_differences(str1, str2):
    sub_and_trans_err = 0
    omi_err = 0
    add_err = 0

    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    i, j = m, n
    differences = []

    edited = str1
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                differences.append(f"'{str1[i - 1]}' was substituted for '{str2[j - 1]}' at position {i-1}")
                edited = edited[:i-1] + f"({edited[i-1]})" + edited[i:]
                sub_and_trans_err += 1
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                differences.append(f"'{str1[i - 1]}' was added at position {i-1}")
                edited = edited[:i-1] + f"[{edited[i-1]}]"  + edited[i:]
                add_err += 1
                i -= 1
            elif dp[i][j] == dp[i][j - 1] + 1:
                differences.append(f"'{str2[j - 1]}' is missing at position {i}")
                edited = edited[:i] + "_" + edited[i:]
                omi_err += 1
                j -= 1

    while i > 0:
        differences.append(f"'{str1[i - 1]}' was added at position{i-1}")
        edited = edited[:i-1] + f"[{edited[i-1]}]"  + edited[i:]
        add_err += 1
        i -= 1

    while j > 0:
        differences.append(f"'{str2[j - 1]}' is missing at position {j-1}")
        edited = edited[:j-1] + "_" + edited[j-1:]
        j -= 1
    print(edited, str2)

    print(f"Addition Errors: {add_err}\n"
      f"Omission Errors: {omi_err}\n"
      f"Transposition and Substitution Errors: {sub_and_trans_err}")
    
    return differences[::-1]


differences = find_differences(str1, str2)
for diff in differences:
    print(diff)

