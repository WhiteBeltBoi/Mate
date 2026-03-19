import os

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
base_folder = "/Users/johndoe/Mate/personal_projects/Mail_Merge_Project_Start"
def get_letter():
    with open (f"{base_folder}/Input/Letters/starting_letter.txt", "r") as f:
        letter = f.read()
        return letter

def get_names():
    with open(f"{base_folder}/Input/Names/invited_names.txt", "r") as f:
        names = f.read()
        return names

def delete_short_txt_files():
    output_folder = f"{base_folder}/Output/ReadyToSend"

    for filename in os.listdir(output_folder):
        if not filename.endswith(".txt"):
            continue

        name_without_extension = filename[:-4]

        if len(name_without_extension) < 2:
            os.remove(os.path.join(output_folder, filename))
            print(f"Deleted: {filename}")

def main():
    letter_body = get_letter()
    names = get_names().split("\n")
    print(names)


    for name in names:
        letter_body = letter_body.replace("[name]", name)
        with open(f"{base_folder}/Output/ReadyToSend/{name}.txt", "w") as f:
            f.write(letter_body)



if __name__ == "__main__":
    main()
