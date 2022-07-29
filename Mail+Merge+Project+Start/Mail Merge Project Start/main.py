#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', mode='r') as file1:
    names_list = file1.readlines()
    for i in range(len(names_list)):
        names_list[i] = names_list[i].strip()
with open('./Input/Letters/starting_letter.txt', mode='r') as file_2:
    lines = file_2.readlines()
    for names in names_list:
        with open(f'./Output/ReadyToSend/letter_for_{names}.txt', mode='w')as file3:
            new = lines[0].replace("[name]", names)
            file3.write(new)
            for i in lines[1:]:
                file3.write(i)
        # with open(f'./Output/ReadyToSend/{names}.txt', mode='a')as file3:




