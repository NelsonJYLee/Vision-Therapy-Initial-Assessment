from marker import find_differences
#from transcriber import recognize_from_microphone

def DEM_test():   
    
    
    #transcriber_result = recognize_from_microphone() #{"text":recognized_text, "duration": duration}

    #unprocessed string, may contain words or punctuation
    #raw_string = transcriber_result["text"]
    raw_string_1 = "3475529187255111377446817447665327992339624"

    #duration with many decimal points
    #duration = transcriber_result["duration"]
    duration_1 = 36

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
    raw_string_2 = "673923991271454675623523577448643asdfas57251978"
    patient_numbers_2 = to_clean_string(raw_string_2)
    duration_2 = 45
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
    for diff in marker_results_2["differences"]:
        print(diff)

DEM_test()






