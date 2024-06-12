from marker import find_differences
from transcriber import recognize_from_microphone
import jinja2
import pdfkit
import os
from datetime import datetime

def DEM_test():

    patient_name = input("Patient Name (Firstname Lastname): ")
    date_of_birth = input("Date of Birth (mm/dd/yyyy): ")
    age = input("Age: ")

    continue_to_1 = input("Continue to Test 1? (y/n): ")
    if continue_to_1 == "n":
        return

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

    continue_to_2 = input("Continue to Test 2? (y/n): ")
    if continue_to_2 == "n":
        return



    #start of Test 2
    #testing purposes:
    # raw_string_2 = "673923991271454675623523577448643asdfas57251978"
    # patient_numbers_2 = to_clean_string(raw_string_2)
    # duration_2 = 45

    transcriber_result_2 = recognize_from_microphone()
    raw_string_2 = transcriber_result_2["text"]
    print(f"raw string: {raw_string_2}")
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

    continue_to_3 = input("Continue to Test 3? (y/n): ")
    if continue_to_3 == "n":
        return

    
    #start of Test 3
    #testing purposes:
    # raw_string_3 = "25943452783578795737145614629372672462632917465253748452177931192147632574637598"
    # patient_numbers_3 = to_clean_string(raw_string_3)
    # duration_3 = 100

    transcriber_result_3 = recognize_from_microphone()
    raw_string_3 = transcriber_result_3["text"]
    print(f"raw string: {raw_string_3}")
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

    make_pdf = input("Make PDF? (y/n): ")
    if make_pdf == "n":
        return
    
    print("Creating PDF...")

    context = {
        "patient_name": patient_name,
        "date_of_birth": date_of_birth,
        "age": age,

        "answer_key_1": answer_key_1,
        "marker_results_1": marker_results_1['marked_numbers'],
        "rounded_duration_1": rounded_duration_1,

        "answer_key_2": answer_key_2,
        "marker_results_2": marker_results_2['marked_numbers'],
        "rounded_duration_2": rounded_duration_2,

        "answer_key_3": answer_key_3,
        "marker_results_3": marker_results_3['marked_numbers'],
        "rounded_duration_3": rounded_duration_3,

        "sub_and_trans_err": total_errors["sub_and_trans_err"],
        "omi_err": total_errors["omi_err"],
        "add_err": total_errors["add_err"],

        "total_vertical_time": total_vertical_time,
        "total_horizontal_time": total_horizontal_time,
        "adjusted_horizontal_time": adjusted_horizontal_time,
        "total_errors_num": total_errors_num,

        "DEM_ratio": DEM_ratio
    }

    #html to pdf set-up
    template_loader = jinja2.FileSystemLoader("./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("pdf.html")
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")

    #custom filenames and directory path
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{patient_name}_{current_date}.pdf"
    output_directory = f"patient_pdf"

    output_path = os.path.join(output_directory, output_filename)

    #making pdf and storing it in the output path
    pdfkit.from_string(output_text, output_path, configuration=config)

    print("Finished!")

DEM_test()






