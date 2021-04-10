import os

filename = input("Please enter the filename: ")
# Check if File Exists
if os.path.isfile("./" + filename):
    print("Looking for file {}...".format(filename))
    print("File Found")
    action = input("Enter one option\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\n")
    if action == "A":
        print("The content of the file:")
        with open(filename, "r") as read_file:
            print(read_file.read())

    elif action == "B":
        os.remove("./" + filename)
        
        # Recreate the file
        with open(filename, "w") as write_file:
            write_file.write("")
        print("{} have been deleted and recreated.".format(filename))
        
    elif action == "C":
        text = input("Please enter your note: ")
        with open(filename, "a") as append_file:
            append_file.write(text + "\n")

    elif action == "D":
        line_num = int(
            input("Please enter the line number to update: "))
        text = input("Please enter your note: ")
        with open(filename, "r") as read_file:
            lines = read_file.readlines()
        with open(filename, "w") as write_file:
            for idx, line in enumerate(lines):
                
                # print(idx, line)
                if idx == line_num - 1:
                    print("Line num {} needs to be replaced!".format(line_num))
                    write_file.write(text + "\n")
                else:
                    
                    write_file.write(line)

    else:
        print("Invalid Input")
else:
    print("File does not exist. Creating file")
    text = input("Please enter your note: ")
    with open(filename, "w") as write_file:
        write_file.write(text + "\n")
