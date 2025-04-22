def can_brick_pass():
    A = int(input("Введите размер А кирпича: "))
    B = int(input("Введите размер B кирпича: "))
    C = int(input("Введите размер C кирпича: "))
    D = int(input("Введите размер D кирпича: "))
    E = int(input("Введите размер E кирпича: "))

    if (A <= D and C <= E) or (C<=D and A<=E):
        print("Кирпич проходит через отверстие")
        return
    if (B<=D and C<=E) or (C<=D and B<=E):
        print("Кирпич проходит через отверстие")
can_brick_pass()
