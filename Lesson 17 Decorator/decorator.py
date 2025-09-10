def decor_result(result_func):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Distinction")
        else:
            result_func(marks)
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m>33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")

    
result([78,93,30,86])