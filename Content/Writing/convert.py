import os

if __name__ == '__main__':
    for filename in os.listdir(os.getcwd()):
        if filename == 'Ref.txt' or filename.find('Parsed') != -1 or filename == 'convert.py':
            continue
        f = open(filename, 'r')
        writefile = open(filename[0:-4] + 'Parsed.txt', 'w')
        filetext = f.read()
        filetext = filetext.strip()
        no_newline = filetext.replace('\n', '<br>')
        writefile.write(no_newline)
        f.close()
        writefile.close()
