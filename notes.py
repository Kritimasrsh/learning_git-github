import os

FILE_NAME = "notes.txt"

# Add a note
def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!\n")

# View notes
def view_notes():
    if not os.path.exists(FILE_NAME):
        print("No notes found!\n")
        return

    print("\n--- Your Notes ---")
    with open(FILE_NAME, "r") as file:
        notes = file.readlines()
        if not notes:
            print("No notes yet!\n")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
    print()

# Delete all notes
def delete_notes():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("All notes deleted!\n")
    else:
        print("No notes file found!\n")

# Menu
while True:
    print("===== NOTES APP =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")


