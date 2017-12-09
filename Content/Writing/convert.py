import os

if __name__ == '__main__':
    for filename in os.listdir(os.getcwd()):
        if filename == 'Ref.txt' or filename.find('Parsed') != -1 or filename == 'convert.py' or filename[0] == '.' or os.path.isdir(filename):
            continue
        f = open(filename, 'r')
        writefile = open(filename[0:-4] + 'Parsed.txt', 'w')
        filetext = f.read()
        filetext = filetext.strip()
        split_text = filetext.split('\n')
        interim_list = []
        for line in split_text:
            if line[0] == 'n':
                continue
            interim_list.append(line)
        result_string = "\n".join(interim_list)
        no_newline = result_string.replace('\n', '<br>')
        writefile.write(no_newline)
        f.close()
        writefile.close()
