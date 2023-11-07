import random

def generate_squads(students, counselors, directors, num_days):
    # Initialize squads for each day
    squads = {
        'students': {
            'cooking': [],
            'table_service': [],
            'dishes': []
        },
        'counselors': {
            'cooking': [],
            'table_service': [],
            'dishes': []
        },
        'directors': {
            'cooking': [],
            'table_service': [],
            'dishes': []
        }
    }

    # Iterate through all days entered
    for day in range(num_days):

        # Shuffle the lists of students, counselors, and directors so that it's random every day
        random.shuffle(students)
        random.shuffle(counselors)
        random.shuffle(directors)

        # Divide students so that there are more in cooking and dishes
        student_group_size = len(students) // 5

        squads['students']['cooking'].append(students[:2 * student_group_size])
        squads['students']['table_service'].append(students[2 * student_group_size:3 * student_group_size])
        squads['students']['dishes'].append(students[3 * student_group_size:])

        # Divide counselors so that it is equal
        counselor_group_size = len(counselors) // 3
        squads['counselors']['cooking'].append(counselors[:1 * counselor_group_size])
        squads['counselors']['table_service'].append(counselors[1 * counselor_group_size:2 * counselor_group_size])
        squads['counselors']['dishes'].append(counselors[2 * counselor_group_size:])

        # Divide directors so that it is mostly equal
        director_group_size = len(directors) // 3
        squads['directors']['cooking'].append(directors[:1 * director_group_size])
        squads['directors']['table_service'].append(directors[1 * director_group_size:2 * director_group_size])
        squads['directors']['dishes'].append(directors[2 * director_group_size:])

    return squads

# Example usage
students = ['Heaven', 'Mackie', 'Orlando', 'Anthony', 'Joziah', 'My-My', 'Nyel', 'Chris', 'Serena', 'Destiny']
counselors = ['Bianca', 'Melody', 'Hannah', 'Jean-Michel', 'Laselle', 'Ale']
directors = ['Liz', 'Jess', 'Sam', 'Stephen']

num_days = 14

squad_assignments = generate_squads(students, counselors, directors, num_days)

# print("Squad Assignments:")
# for day in range(num_days):
#     print(f"Day {day + 1}: Students - Cooking: {', '.join(squad_assignments['students']['cooking'][day])}, Table Service: {', '.join(squad_assignments['students']['table_service'][day])}, Dishes: {', '.join(squad_assignments['students']['dishes'][day])}")
#     print(f"     Counselors - Cooking: {', '.join(squad_assignments['counselors']['cooking'][day])}, Table Service: {', '.join(squad_assignments['counselors']['table_service'][day])}, Dishes: {', '.join(squad_assignments['counselors']['dishes'][day])}")
#     print(f"     Directors - Cooking: {', '.join(squad_assignments['directors']['cooking'][day])}, Table Service: {', '.join(squad_assignments['directors']['table_service'][day])}, Dishes: {', '.join(squad_assignments['directors']['dishes'][day])}")