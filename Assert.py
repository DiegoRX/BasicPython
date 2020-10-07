#assert <expresion booleana>, <mensaje de error>
def first_letter(list_of_words):
    first_letters = []

    for word in list_of_words:
        assert type(word) == str, f'{palabra} no es str'
        assert len(word) > 0, 'No se permiten str vacios'

        first_letters.append(word[0])
    
    return first_letters