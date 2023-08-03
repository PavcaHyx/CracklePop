
def get_result(start_number, end_number):
    result = []
    start_number = int(start_number)
    end_number = int(end_number)
    for i in range(start_number, end_number + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("CracklePop")
        elif i % 5 == 0:
            result.append("Pop")
        elif i % 3 == 0:
            result.append("Crackle")
        else:
            result.append(i)
    return result



