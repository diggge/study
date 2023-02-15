import simple_draw as sd
n=5
i=1
vector1=sd.get_vector(start_point=sd.get_point(300,300), angle=30, length=100, width=3)
next_vector=vector1
next_angle=27
vector1.draw()
while i<n:
    i = i + 1
    next_angle=next_angle+360/n
    print(i)
    next_vector = sd.get_vector(start_point=next_vector.end_point, angle=next_angle, length=100, width=3)
    print(next_vector)
    next_vector.draw()
sd.pause()