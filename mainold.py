def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents
def counting(file_contents):
    words= str(file_contents).split()
    count=len(words)
    print(count)

counting(main())