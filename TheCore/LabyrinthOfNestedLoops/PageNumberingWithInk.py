def pagesNumberingWithInk(current, numberOfDigits):
    pages = []
    to_print = numberOfDigits
    for i in range(current, current + numberOfDigits):
        pages.append(str(i))
    print pages
    completed = current
    index =
    while numberOfDigits >= len(pages[index]):
        print pages[index], len(pages[index]), numberOfDigits
        numberOfDigits -= len(pages[index])
        index += 1
        completed = int(pages[index])
        print pages[index], len(pages[index]), numberOfDigits, 'after'

    return completed
