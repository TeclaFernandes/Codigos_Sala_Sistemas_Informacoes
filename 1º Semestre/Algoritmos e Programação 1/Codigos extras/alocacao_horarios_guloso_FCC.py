def greedy_timetabling(courses):
    # Dicionário para armazenar a cor (horário) de cada curso
    result = {}

    # Atribuir cores aos cursos um por um
    for course in courses:
        # Coletar as cores já usadas pelos cursos adjacentes (conflitantes)
        neighbor_colors = {result[neighbor] for neighbor in courses[course] if neighbor in result}

        # Encontrar a menor cor disponível
        color = 0
        while color in neighbor_colors:
            color += 1

        # Atribuir a cor ao curso
        result[course] = color

    return result

# Exemplo de conflitos entre cursos:
courses_conflicts = {
    'Math': ['Physics', 'Chemistry'],
    'Physics': ['Math', 'Biology'],
    'Chemistry': ['Math'],
    'Biology': ['Physics']
}

print(greedy_timetabling(courses_conflicts))
# Saída: {'Math': 0, 'Physics': 1, 'Chemistry': 1, 'Biology': 0}
