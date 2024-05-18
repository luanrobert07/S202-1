from database import Database


class Queries:
    def __init__(self, db):
        self.db = db

    def get_teacher_by_name(self, name):
        query = "MATCH (t:Teacher{name:$name}) RETURN t.ano_nasc, t.cpf"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def get_teachers_starting_with(self, initial):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH $initial RETURN t.name, t.cpf"
        parameters = {"initial": initial}
        return self.db.execute_query(query, parameters)

    def get_all_city_names(self):
        query = "MATCH (c:City) RETURN c.name"
        return self.db.execute_query(query)

    def get_schools_by_number_range(self, min_number, max_number):
        query = "MATCH (s:School) WHERE s.number >= $min_number AND s.number <= $max_number RETURN s.name, s.address, s.number"
        parameters = {"min_number": min_number, "max_number": max_number}
        return self.db.execute_query(query, parameters)

    def get_youngest_and_oldest_teacher_birth_years(self):
        query = """
        MATCH (t:Teacher)
        WITH COLLECT(t) AS teachers
        RETURN MIN(teachers[0].ano_nasc) AS youngest, MAX(teachers[-1].ano_nasc) AS oldest
        """
        return self.db.execute_query(query)

    def get_average_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS average_population"
        return self.db.execute_query(query)

    def get_city_by_cep_replace_letter_a(self, cep):
        query = """
        MATCH (c:City)
        WHERE c.cep = $cep
        RETURN REPLACE(c.name, 'a', 'A') AS city_name
        """
        parameters = {"cep": cep}
        return self.db.execute_query(query, parameters)

    def get_third_character_from_teacher_names(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 3, 1) AS third_character
        """
        return self.db.execute_query(query)