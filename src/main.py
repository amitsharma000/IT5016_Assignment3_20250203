# main.py

from src.record_manager import StudentRecordManager

def main():
    manager = StudentRecordManager()

    manager.add_student("Alice", "S001")
    manager.add_student("Bob", "S002")

    print("All Students:")
    for student in manager.list_students():
        print(student)

    print("\nRemoving Bob...")
    manager.remove_student("S002")

    print("Updated Students:")
    for student in manager.list_students():
        print(student)

if __name__ == "__main__":
    main()
