
def find_most_common_surnames():
    
    n = int(input("Введите количество сотрудников: "))
    
    
    employees = []
    
    
    surname_count = {}
    
    print("Введите данные сотрудников (Фамилия Имя):")
    for _ in range(n):
        full_name = input().strip()
        if full_name:  
            surname = full_name.split()[0]  
            employees.append(full_name)
            
            
            if surname in surname_count:
                surname_count[surname] += 1
            else:
                surname_count[surname] = 1
    
    
    max_count = max(surname_count.values())
    
    
    most_common_surnames = [surname for surname, count in surname_count.items() if count == max_count]
    
    
    print("Самые часто встречающиеся фамилии:")
    print(" ".join(most_common_surnames))


find_most_common_surnames()
