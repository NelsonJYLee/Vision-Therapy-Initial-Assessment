#compares patient_numbers to answer_key, creates a marked_string to show differences in patient_numbers, counts errors, and details errors.
def find_differences(patient_numbers, answer_key):

    #error tally
    sub_and_trans_err = 0
    omi_err = 0
    add_err = 0

    #2D DP - Levenstein Distance
    m, n = len(patient_numbers), len(answer_key)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    #creates a 2D graph for edit distances
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif patient_numbers[i - 1] == answer_key[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    i, j = m, n

    #intialize array to hold strings for error explanation
    differences = []

    #initialize marked_numbers variable
    marked_numbers = patient_numbers

    #going from bottom-right to top-left of graph to gather error counts, error descriptions, and create marked_numbers
    while i > 0 and j > 0:
        if patient_numbers[i - 1] == answer_key[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                differences.append(f"'{patient_numbers[i - 1]}' was substituted for '{answer_key[j - 1]}' at position {i-1}")
                marked_numbers = marked_numbers[:i-1] + f"({marked_numbers[i-1]})" + marked_numbers[i:]
                sub_and_trans_err += 1
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                differences.append(f"'{patient_numbers[i - 1]}' was added at position {i-1}")
                marked_numbers = marked_numbers[:i-1] + f"[{marked_numbers[i-1]}]"  + marked_numbers[i:]
                add_err += 1
                i -= 1
            elif dp[i][j] == dp[i][j - 1] + 1:
                differences.append(f"'{answer_key[j - 1]}' is missing at position {i}")
                marked_numbers = marked_numbers[:i] + "_" + marked_numbers[i:]
                omi_err += 1
                j -= 1

    #used when j == 0 and i > 0 
    while i > 0:
        differences.append(f"'{patient_numbers[i - 1]}' was added at position{i-1}")
        marked_numbers = marked_numbers[:i-1] + f"[{marked_numbers[i-1]}]"  + marked_numbers[i:]
        add_err += 1
        i -= 1

    #used when i == 0 and j > 0
    while j > 0:
        differences.append(f"'{answer_key[j - 1]}' is missing at position {j-1}")
        marked_numbers = marked_numbers[:j-1] + "_" + marked_numbers[j-1:]
        j -= 1

    return {"marked_numbers": marked_numbers,
            "errors":{
                "add_err": add_err,
                "omi_err": omi_err,
                "sub_and_trans_err": sub_and_trans_err
            },
            "differences": differences[::-1]
            }

    #should return, marked_numbers, errors, differences
