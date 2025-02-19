def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    num_words=get_num_words(text)
    #print(f"{num_words} words found in the document")
    characters=get_num_char(text)
    sorted_list=print_report(characters)
    print(f"Begin Report on {book_path}")
    print(f"{num_words} words found in the document")
    names=[d["name"] for d in sorted_list]
    nums=[d["num"] for d in sorted_list]
    for i in range(len(names)):
            print(f"The \'{names[i]}\' was found {nums[i]} times")
    print("end")



def get_num_words(text):
    words=text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    lower_txt=text.lower()
    listofchar=list(lower_txt)
    char_dict={}
    for char in listofchar:
        char_dict[char]=char_dict.get(char, 0)+1
    return char_dict

def sort_on(dict):
    return dict["num"]

def print_report(characters):
    keys=characters.keys()
    newlist=[]
    for key in keys:
        if key.isalpha():
            newlist.append({"name": key, "num": characters[key]})
    
    newlist.sort(reverse=True, key=sort_on)
    return newlist

        
main()