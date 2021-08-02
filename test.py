from kitchen import *

add_empty_bowls('pie tin', 'mixing bowl')
add_ingredients(apple='granny smith', sugar='brown sugar', crust='crispy crust')
move('apple', origin='ingredient box', destination='mixing bowl')
move('sugar', origin='ingredient box', destination='mixing bowl')
mix('apple', 'sugar', location='mixing bowl', new_name='apple pie goo filling')
move('apple pie goo filling', origin='mixing bowl', destination='pie tin')
move('crust', origin='ingredient box', destination='pie tin')
bake('pie tin', function=lambda b: 'apple pie' if b.__dict__['crust'] and b.__dict__['apple pie goo filling'] else 'gross pie', new_name='pie')

print('done')