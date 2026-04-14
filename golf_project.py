 #MOC starter code for main function US Golf Master's Leaderboard Project
def main():
    filename = "golf_masters.txt"
    golfer_ids, player_names, par_score, cut_status = read_file(golfers.txt)
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
# TODO in exam
elif choice == "6":
# TODO in exam
elif choice == '7':
# TODO in exam
elif choice == "8":
# save data and quit
print("Data saved. Goodbye.")
else:
print("Invalid choice.")
if __name__ == '__main__':
main()