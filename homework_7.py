def is_possible_less_than_300(value):

    if type(value) is  not int :
        return "not integer"
    elif  1 <= value <= 299:
        return True
    else:
        return"out of range"

print(is_possible_less_than_300(300))



def is_number_from_1_to_255(value):

    if not isinstance(value, int):
        return "Value is not integer"
    if value < 1 or value > 255:
        return "Value is out of range"
    return True

print(is_number_from_1_to_255(254))


def is_israel_mobile(phone):
    clean_phone = phone.replace(" ", "").replace("-","")
    if (
        len(clean_phone) == 10 and clean_phone.startswith("05") and clean_phone.isdigit()):

        return True


    if (
       len(clean_phone) == 13 and
           clean_phone.startswith("+9725") and clean_phone[1:].isdigit()
   ):
           return  True
    return False

print(is_israel_mobile("054-123-4567"))
print(is_israel_mobile("54-1234567"))
