
def get_result(start_number, end_number):
    result = []
    end_number = end_number+1
    for i in range(start_number, end_number):
        if i % 3 == 0 and i % 5 == 0:
            result.append("CracklePop")
        elif i % 5 == 0:
            result.append("Pop")
        elif i % 3 == 0:
            result.append("Crackle")
        else:
            result.append(i)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_result(1, 100))


