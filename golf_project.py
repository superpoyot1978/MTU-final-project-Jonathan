

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

# ---------- Menu Functions ----------
#function to view leaderboard table
def view_leaderboard(golfer_ids, player_names, par_score, cut_status, rounds):
    print("\n# Leaderboard after Round 2\n")
    print("{:<6} {:<20} {:<5} {:<6} {:<2}".format("ID", "Player", "Par", "Round", "Cut"))
    print("-"*45)
    for i in range(len(golfer_ids)):
        par_str = f"+{par_score[i]}" if par_score[i] > 0 else f"{par_score[i]}" if par_score[i] < 0 else "0"
        cut_emoji = "\U0001F601" if cut_status[i] == 1 else "\u2639\ufe0f"
        print("{:<6} {:<20} {:<5} {:<6} {:<2}".format(golfer_ids[i], player_names[i], par_str, rounds[i], cut_emoji))
    print()

#delete player/s
#gid = golfer id
def delete_player(golfer_ids, player_names, par_score, cut_status, rounds):
    try:
        gid = int(input("Enter Golfer ID to delete: "))
    except ValueError:
        print("Invalid input. Must be an integer.")
        return

    if gid in golfer_ids:
        index = golfer_ids.index(gid)
        # remove player info from all lists
        golfer_ids.pop(index)
        player_names.pop(index)
        par_score.pop(index)
        cut_status.pop(index)
        rounds.pop(index)
        print(f"Golfer ID {gid} deleted successfully.")
    else:
        print("Golfer ID not found.")

#adding player/s
def add_player(golfer_ids, player_names, par_score, cut_status, rounds):
    try:
        gid = int(input("Enter new Golfer ID: "))
    except ValueError:
        print("Error,please input a valid id")
        return
    if gid in golfer_ids:
        print("Golfer ID already exits.")
        return

    name = input("Enter Player Name: ")
    try:
        par = int(input("Enter Score Relative to Par (can be negative): "))
    except ValueError:
        print("Invalid input. Must be an integer.")
        return

    golfer_ids.append(gid)
    player_names.append(name)
    par_score.append(par)
    rounds.append(2)  # default round = 2
    cut_status.append(1)  # default made cut
    print(f"Golfer {name} added successfully.")


#updating status
def update_cut_status(golfer_ids, player_names, cut_status):
    try:
        gid = int(input("Enter Golfer ID to update cut status: "))
    except ValueError:
        print("Invalid input. Must be an integer.")
        return
    if gid not in golfer_ids:
        print("ID not found")
        return

    #varibles and touch up
    index = golfer_ids.index(gid)
    status = cut_status[index]
    name = player_names[index]
    status_str = "made the cut" if status == 1 else "missed the cut"
    print(f"{name} has {status_str}.")
    choice = input("Do you want to change this? (y/n): ").lower()
    if choice == "y":
        cut_status[index] = 0 if status == 1 else 1
        print("Cut status updated successfully.")
    else:
        print("No changes made.")

#------ Main Function---------
## MOC starter code for main function US Golf Master's Leaderboard Project

def main():
    golfer_ids, player_names, par_score, cut_status, rounds = read_file()
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
            view_leaderboard(golfer_ids, player_names, par_score, cut_status, rounds)
        elif choice == "2":
            delete_player(golfer_ids, player_names, par_score, cut_status, rounds)
        elif choice == "3":
            add_player(golfer_ids, player_names, par_score, cut_status, rounds)
        elif choice == "4":
            update_cut_status(golfer_ids, player_names, cut_status)
        elif choice in ["5", "6", "7"]:
            print("to do in exam.")
        elif choice == "8":
            save_file(golfer_ids, player_names, par_score, cut_status, rounds)
            print("data saved. goodbye.")
        else:
            print("invalid choice.")

if __name__ == '__main__':
    main()


