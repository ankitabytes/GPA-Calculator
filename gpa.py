import math

def calculate_gpa(num_courses, mark_mode):
    # Just calculating overall GPA based on how many courses there are
    total_pts = 0
    total_cr = 0

    for i in range(num_courses):
        cname = input("Course name: ")
        cr = int(input(f"Credits for {cname}: "))

        # the user can either enter full marks or break them down
        if mark_mode == 0:
            got = int(input(f"Total marks you got in {cname}: "))
        else:
            mid = int(input(f"{cname} Mid Sem marks: "))
            internal = int(input(f"{cname} Internal marks: "))
            end = int(input(f"{cname} End Sem marks: "))
            got = mid + internal + end

        print()

        # sanity check
        if got > 100:
            print("Marks can't exceed 100.")
            total_pts = 0
            total_cr = 1
            break
        elif got < 100:
            # a small increment to avoid zero issues (as in your original logic)
            got += 1

        # convert marks to grade-points (roughly)
        p = math.ceil(got / 10)

        total_pts += p * cr
        total_cr += cr

    return total_pts / total_cr


if __name__ == "__main__":
    print("\n---------------------------")
    print("     GPA CALCULATOR")
    print("---------------------------\n")

    try:
        n = int(input("How many courses do you have? "))
        mode = int(input("Enter 1 for Mid+Internal+End, or 0 for Total Marks: "))

        result = calculate_gpa(n, mode)
        print("\nYour GPA for this semester:", result)

    except ValueError:
        print("\nPlease enter valid numeric inputs.")
