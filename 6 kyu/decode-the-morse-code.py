from preloaded import MORSE_CODE

def decode_morse(morse_code):
    list1 = morse_code.strip().split("   ")
    list2=[]
    final = []
    for x in list1:
        list2.append(x.split(" "))
    for x in list2:
        x = "".join([MORSE_CODE[i] for i in x])
        final.append(x)
    return " ".join(final)