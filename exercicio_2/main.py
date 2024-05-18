from CLI_teacher import TeacherCLI
from query import Queries
from database import Database
from teacher_crud import TeacherCRUD


db = Database("bolt://54.208.2.27:7687", "neo4j", "identification-twenties-gum") 

teacher_crud = TeacherCRUD(db)

# Para testar a CLI descomentar o código, para rodar as querys deixar ele comentado
# teacher_cli = TeacherCLI(teacher_crud)
# teacher_cli.run()

# Query questão 1

queries = Queries(db)

renzo_info = queries.get_teacher_by_name("Renzo")
print("Teacher Renzo Info:", renzo_info)

teachers_m = queries.get_teachers_starting_with("M")
print("Teachers starting with M:", teachers_m)

cities = queries.get_all_city_names()
print("All cities:", cities)

schools = queries.get_schools_by_number_range(150, 550)
print("Schools with number in range 150-550:", schools)

# Query questão 2
youngest_oldest_years = queries.get_youngest_and_oldest_teacher_birth_years()
print("Youngest and Oldest Teacher Birth Years:", youngest_oldest_years)

average_population = queries.get_average_population()
print("Average Population of Cities:", average_population)

city_name_replaced = queries.get_city_by_cep_replace_letter_a("37540-000")
print("City Name with 'a' replaced by 'A':", city_name_replaced)

third_characters = queries.get_third_character_from_teacher_names()
print("Third Characters from Teacher Names:", third_characters)

# Entradas questão 3

teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")
teacher = teacher_crud.read("Chris Lima")
print("Read Teacher:", teacher)
teacher_crud.update(name="Chris Lima", new_cpf="162.052.777-77")
updated_teacher = teacher_crud.read("Chris Lima")
print("Updated Teacher:", updated_teacher)



db.close()
