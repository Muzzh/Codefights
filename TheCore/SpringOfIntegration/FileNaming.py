def fileNaming(names):
    files = []
    for f in names:
        if f in files:
            k =1
            while True:
                new_file = '{0}({1})'.format(f, k)
                if new_file not in files:
                    files.append(new_file)
                    break
                k += 1

        else:
            files.append(f)
    return files
