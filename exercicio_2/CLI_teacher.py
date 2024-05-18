from teacher_crud import TeacherCRUD


class TeacherCLI:
    def __init__(self, teacher_crud):
        self.teacher_crud = teacher_crud

    def run(self):
        while True:
            print("\nTeacher CRUD CLI")
            print("1. Create Teacher")
            print("2. Read Teacher")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_teacher()
            elif choice == '2':
                self.read_teacher()
            elif choice == '3':
                self.update_teacher()
            elif choice == '4':
                self.delete_teacher()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_teacher(self):
        name = input("Enter name: ")
        ano_nasc = int(input("Enter year of birth: "))
        cpf = input("Enter CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print("Teacher created successfully.")

    def read_teacher(self):
        name = input("Enter name: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print("Teacher details:")
            print(f"Name: {teacher['name']}")
            print(f"Year of Birth: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")
        else:
            print("Teacher not found.")

    def update_teacher(self):
        name = input("Enter name: ")
        new_cpf = input("Enter new CPF: ")
        self.teacher_crud.update(name, new_cpf)
        print("Teacher updated successfully.")

    def delete_teacher(self):
        name = input("Enter name: ")
        self.teacher_crud.delete(name)
        print("Teacher deleted successfully.")