try:
    file = open('blabla.txt')
except OSError as exc:
    print(f'вот что пошло не так - {exc} параметры {exc.args[2]}, но мы еще на плаву')