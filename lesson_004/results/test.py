import simple_draw as sd
import pprint
sveta_dict={1:sd.COLOR_RED,2:sd.COLOR_ORANGE,3:sd.COLOR_YELLOW,4:sd.COLOR_GREEN,5:sd.COLOR_CYAN,6:sd.COLOR_BLUE,7:sd.COLOR_PURPLE}
print("Введите, пожалуйста, номер цвета: 1:Красный,2:Оранжевый,3:Желтый,4:Зеленый,5:голубой,6:синий,7:фиолетовый")
user_input = input()
svet = int(user_input)
print(sveta_dict[svet])


sveta_dict={1:sd.COLOR_RED,2:sd.COLOR_ORANGE,3:sd.COLOR_YELLOW,4:sd.COLOR_GREEN,5:sd.COLOR_CYAN,6:sd.COLOR_BLUE,7:sd.COLOR_PURPLE}
print("Введите, пожалуйста, номер цвета: 1:Красный,2:Оранжевый,3:Желтый,4:Зеленый,5:голубой,6:синий,7:фиолетовый")
svet = int(input())

# print(sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
