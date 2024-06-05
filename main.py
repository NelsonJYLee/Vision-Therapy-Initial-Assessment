#from transcriber import recognize_from_microphone

#transcriber_result = recognize_from_microphone() #{"text":recognized_text, "duration": duration}

#unprocessed string, may contain words or punctuation
#raw_string = transcriber_result["text"]
raw_string = "3475529187255377446817447665327992339624"

#duration with many decimal points
#duration = transcriber_result["duration"]
duration = 36

#duration rounded to the nearest whole number
rounded_duration = round(duration)

#processed string, numbers only:
patient_numbers = []

#answer key to compare patient_numbers with
answer_key = ['3', '4', '7', '5', '5', '2', '9', '1', '8', '7', '2', '5', '5', '3', '7', '7', '4', '4', '6', '8', '1', '7', '4', '4', '7', '6', '6', '5', '3', '2', '7', '9', '9', '2', '3', '3', '9', '6', '2', '4']
print(f"Duration: {rounded_duration}s")

#producing patient numbers to only have the numbers from raw_string
for char in raw_string:
    if char.isdigit():
        patient_numbers.append(char) 
print(patient_numbers)

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
    marked_numbers = answer_key.copy()

    #going from bottom-right to top-left of graph to gather error counts, error descriptions, and create marked_numbers
    while i > 0 and j > 0:
        if patient_numbers[i - 1] == answer_key[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                differences.append(f"'{patient_numbers[i - 1]}' was substituted for '{answer_key[j - 1]}' at position {i-1}")
                marked_numbers[i-1] += "s"
                sub_and_trans_err += 1
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                differences.append(f"'{patient_numbers[i - 1]}' was added at position {i-1}")
                marked_numbers[i-1] += "a"
                add_err += 1
                i -= 1
            elif dp[i][j] == dp[i][j - 1] + 1:
                differences.append(f"'{answer_key[j - 1]}' is missing at position {i}")
                marked_numbers[i] += "o"
                omi_err += 1
                j -= 1

    #used when j == 0 and i > 0 
    while i > 0:
        differences.append(f"'{patient_numbers[i - 1]}' was added at position{i-1}")
        marked_numbers[i-2] += "a"
        add_err += 1
        i -= 1

    #used when i == 0 and j > 0
    while j > 0:
        differences.append(f"'{answer_key[j - 1]}' is missing at position {j-1}")
        marked_numbers[i] += "o"
        j -= 1
    print(marked_numbers)
    print(answer_key)

    #error counts
    print(f"Addition Errors: {add_err}\n"
      f"Omission Errors: {omi_err}\n"
      f"Transposition and Substitution Errors: {sub_and_trans_err}")
    
    #error descriptions
    return differences[::-1]


differences = find_differences(patient_numbers, answer_key)

#printing all error descriptions
for diff in differences:
    print(diff)



