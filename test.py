from kitchen import *

add_empty_bowls('pie_tin', 'mixing_bowl')
add_ingredients(apple='granny smith', sugar='brown sugar')
move('apple', origin='ingredient_box', destination='mixing_bowl')
move('sugar', origin='ingredient_box', destination='mixing_bowl')
combine('apple', 'sugar', location='mixing_bowl', new_name='apple pie goo filling')

print('done')