from marker import find_differences
from transcriber import recognize_from_microphone

def DEM_test():   

    total_errors = {
        "add_err": 0,
        "omi_err": 0,
        "sub_and_trans_err": 0
    }
    
    #testing purposes
    # #unprocessed string, may contain words or punctuation
    # raw_string_1 = "3475529187255111377446817447665327992339624"

    # #duration with many decimal points
    # duration_1 = 36

    transcriber_result_1 = recognize_from_microphone() #{"text":recognized_text, "duration": duration}

    #unprocessed string, may contain words or punctuation
    raw_string_1 = transcriber_result_1["text"]
    print(f"raw string: {raw_string_1}")
    #duration with many decimal points
    duration_1 = transcriber_result_1["duration"]

    #duration rounded to the nearest whole number
    rounded_duration_1 = round(duration_1)

    #answer key to compare patient_numbers with
    answer_key_1 = "3475529187255377446817447665327992339624"

    #producing patient numbers to only have the numbers from raw_string
    def to_clean_string(raw_string):
        clean_string = ""
        for char in raw_string:
            if char.isdigit():
                clean_string += char
        return clean_string

    #processed string, numbers only:
    patient_numbers_1 = to_clean_string(raw_string_1)

    marker_results_1 = find_differences(patient_numbers_1, answer_key_1)
    # {"marked_numbers": marked_numbers,
    #             "errors":{
    #                 "add_err": add_err,
    #                 "omi_err": omi_err,
    #                 "sub_and_trans_err": sub_and_trans_err
    #             },
    #             "differences": differences[::-1]
    #             }


    for err in marker_results_1["errors"]:
        total_errors[err] += marker_results_1["errors"][err]

    print("Test 1")
    print(f"Duration: {rounded_duration_1}s")
    print(f"Answer Key: {answer_key_1}")
    print(f"Patient Results: {patient_numbers_1}")
    print(f"Marked Results: {marker_results_1['marked_numbers']}\n"
        f"Errors: {marker_results_1['errors']}\n"
        )

    #printing all error descriptions
    for diff in marker_results_1["differences"]:
        print(diff)

    continue_to_2 = input("Continue to Test 2? (y/n)")
    if continue_to_2 == "n":
        return



    #start of Test 2
    #testing purposes:
    # raw_string_2 = "673923991271454675623523577448643asdfas57251978"
    # patient_numbers_2 = to_clean_string(raw_string_2)
    # duration_2 = 45

    transcriber_result_2 = recognize_from_microphone()
    raw_string_2 = transcriber_result_2["text"]
    patient_numbers_2 = to_clean_string(raw_string_2)
    duration_2 = transcriber_result_2["duration"]
    rounded_duration_2 = round(duration_2)
    answer_key_2 = "6739239912714467562352357744864357251978"

    marker_results_2 = find_differences(patient_numbers_2, answer_key_2)

    print("Test 2")
    print(f"Duration: {rounded_duration_2}s")
    print(f"Answer Key: {answer_key_2}")
    print(f"Patient Results: {patient_numbers_2}")
    print(f"Marked Results: {marker_results_2['marked_numbers']}\n"
        f"Errors: {marker_results_2['errors']}\n"
        )
    
    for err in marker_results_2["errors"]:
        total_errors[err] += marker_results_2["errors"][err]

    for diff in marker_results_2["differences"]:
        print(diff)

    continue_to_3 = input("Continue to Test 3? (y/n)")
    if continue_to_3 == "n":
        return

    
    #start of Test 3
    #testing purposes:
    # raw_string_3 = "25943452783578795737145614629372672462632917465253748452177931192147632574637598"
    # patient_numbers_3 = to_clean_string(raw_string_3)
    # duration_3 = 100

    transcriber_result_3 = recognize_from_microphone()
    raw_string_3 = transcriber_result_3["text"]
    patient_numbers_3 = to_clean_string(raw_string_3)
    duration_3 = transcriber_result_3["duration"]
    rounded_duration_3 = round(duration_3)
    answer_key_3 = "25943452783574987957371456146293726724636329174652537484521779392147632574637598"

    marker_results_3 = find_differences(patient_numbers_3, answer_key_3)

    print("Test 3")
    print(f"Duration: {rounded_duration_3}s")
    print(f"Answer Key: {answer_key_3}")
    print(f"Patient Results: {patient_numbers_3}")
    print(f"Marked Results: {marker_results_3['marked_numbers']}\n"
        f"Errors: {marker_results_3['errors']}\n"
        )
    
    for err in marker_results_3["errors"]:
        total_errors[err] += marker_results_3["errors"][err]

    for diff in marker_results_3["differences"]:
        print(diff)

    print(total_errors)
    total_vertical_time = round(duration_1 + duration_2)
    total_horizontal_time = duration_3
    adjusted_horizontal_time = round(total_horizontal_time * (80/(80 - total_errors["omi_err"] + total_errors["add_err"])))
    total_errors_num = sum(total_errors.values())
    DEM_ratio = round(adjusted_horizontal_time/total_vertical_time,2)
    print(f"Total Vertical Time: {total_vertical_time}")
    print(f"Adjusted Horizontal Time: {adjusted_horizontal_time}")
    print(f"Total Errors: {total_errors_num}")
    print(f"DEM Ratio: {DEM_ratio}")

DEM_test()






