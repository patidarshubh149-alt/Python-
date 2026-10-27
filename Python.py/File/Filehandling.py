                            #open and close file & Read
# f = open("data.txt","r")
# content = f.read()
# print(content)
# f.close()

                            #auto close file
# with open("data.txt","r") as f:
#     content = f.read()
#     print(content)

                            #Readline

# with open("data.txt","r") as f:
#     content = f.readline()
#     print(content)

                            #Readlines

# with open("data.txt","r") as f:
#     content = f.readlines()
#     print(content)
#     print(len(content))

                            #Creating file and Adding data.

# with open ("Laptop.txt","w") as  f:
#     f.write("Laptop is a electronic device.")

# print("File Created.....!!!")

                            # Append data in File.

# with open ("Laptop.txt","a") as f:
#     f.write("Laptop is very usfull for Programmers.")

# print("Data is succesful append.")   

                            #Writelines in list 

# with open("Laptop.txt","a") as f:
#     f.writelines(["\nPython is a programing language.","\nPython is easy to understand","\nPython are also high level language"])

                            #Copied first file data in second file.

