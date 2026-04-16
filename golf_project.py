

 #test
 #github test1
 #fja;sldkfjsldkfjsdfj
# ---------- File Functions ----------
#read golf masters txt file to have all the golfer data
def read_file():
    golfer_ids = []
    player_names = []
    par_score = []
    rounds = []
    cut_status = []

    try:
        with open("golf_masters.txt", "r") as file:

            for line in file:
                line = line.strip()
                if line:  # skip empty lines
                    data = line.split(",")
                    golfer_ids.append(int(data[0]))
                    player_names.append(data[1])
                    par_score.append(int(data[2]))
                    rounds.append(int(data[3]))
                    cut_status.append(int(data[4]))
    except FileNotFoundError:
        print(f"File 'golf_masters.txt' not found. Starting with empty dataset.")
    return golfer_ids, player_names, par_score, rounds, cut_status


#saving data function
def save_file(golfer_ids, player_names, par_score, cut_status, rounds):
    with open("golf_masters.txt","w") as file:
        for i in range(len(golfer_ids)):
            line = f"{golfer_ids[i]},{player_names[i]},{par_score[i]},{rounds[i]},{cut_status[i]}\n"
            file.write(line)
    print("Data saved successfully.")





"""def main():
    filename = "golf_masters.txt"
    golfer_ids, player_names, par_score, cut_status = read_file(golfer.txt)
    choice = ""
while choice != "8":
    print("\nMenu")
    print("1. View Leaderboard")
    print("2. Delete a player")
    print("3. Add a new player")
    print("4. Update cut status")
    print("5. Placeholder for Exam")
    print("6. Placeholder for Exam")
    print("7. Placeholder for Exam")
    print("8. Quit and save")
    choice = input("Enter choice: ")
    if choice == "1":

    #display leader board
    elif choice == "2":
    # delete a player
    elif choice == "3":
    # add a new player
    elif choice == "4":
    # update cut status
    elif choice == "5":
#
# save data and quit
print("Data saved. Goodbye.")
else:
    print("Invalid choice.")
    if __name__ == '__main__':
=======
 #MOC starter code for main function US Golf Master's Leaderboard Project
def main():
    filename = "golf_masters.txt"
    golfer_ids, player_names, par_score, cut_status = read_file(golfer.txt)
    choice = ""
while choice != "8":
    print("\nMenu")
    print("1. View Leaderboard")
    print("2. Delete a player")
    print("3. Add a new player")
    print("4. Update cut status")
    print("5. Placeholder for Exam")
    print("6. Placeholder for Exam")
    print("7. Placeholder for Exam")
    print("8. Quit and save")
    choice = input("Enter choice: ")
    if choice == "1":

    #display leader board
    elif choice == "2":
    # delete a player
    elif choice == "3":
    # add a new player
    elif choice == "4":
    # update cut status
    elif choice == "5":
#
# save data and quit
print("Data saved. Goodbye.")
else:
    print("Invalid choice.")
    if __name__ == '__main__':
>>>>>>> e8c03bbda478e3723cd686f94e5796ab0962347f
    main()"""