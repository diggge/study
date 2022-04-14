# Параметры передаются как ссылка

def elephant_to_free(some_list):
    elephant_found = 'elephant' in some_list
    if elephant_found:
        some_list.remove('elephant')
        print('Слон на свободе!!!')
    return elephant_found


zoo = ['lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant']

elephant_to_free(some_list=zoo)
print(zoo)

elephant_to_free(some_list=zoo)
print(zoo)

elephant_to_free(some_list=zoo)
print(zoo)

# это т.н. функции с побочными эффектами, они меняют контекст выполнения.
# можно заблокировать изменение параметров - передать тьюпл
zoo = ('lion', 'elephant', 'monkey', 'skunk', 'horse', 'elephant')