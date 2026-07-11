

def print_string_reversed (string):
    if len(string) == 0:
        print ("Wrong string")
    else:
        reversed_string = string[::-1]
        print(reversed_string)
my_string = "Hello friends"
print_string_reversed(my_string)


def is_isr_phone_number(phone):
    if '""' in  phone :
        return None

    if phone.isdigit() and phone[0]=="0" and len (phone) ==10:
        return "True"
    else:
        return "False"
mis = "0555333440"
result = is_isr_phone_number(mis)
print(result)


def print_substring_reverse(st, start, end):
    if not st.isalpha() or start <0 or end > len(st) or start >=end:
        return "Wrong args"
    part1 = st[:start]
    part2 = st[end:start-1:-1]
    part3 = st[end+1:]
    return  part1+part2+part3
text = "Sanktpeterburg"
result = print_substring_reverse(text, 5 ,9)
print(result)

def get_words_reverse (text):
    words = text.split()
    words.reverse()
    result = " ".join(words)
    return result
t = "i live in Israel"
result = get_words_reverse(t)




def print_string_reversed (string):
    if len(string) == 0:
        print ("Wrong string")
    else:
        reversed_string = string[::-1]
        print(reversed_string)
my_string = "Hello friends"
print_string_reversed(my_string)


def is_isr_phone_number(phone):
    if '""' in  phone :
        return None

    if phone.isdigit() and phone[0]=="0" and len (phone) ==10:
        return "True"
    else:
        return "False"
mis = "0555333440"
result = is_isr_phone_number(mis)
print(result)


def print_substring_reverse(st, start, end):
    if not st.isalpha() or start <0 or end > len(st) or start >=end:
        return "Wrong args"
    part1 = st[:start]
    part2 = st[end:start-1:-1]
    part3 = st[end+1:]
    return  part1+part2+part3
text = "Sanktpeterburg"
result = print_substring_reverse(text, 5 ,9)
print(result)









