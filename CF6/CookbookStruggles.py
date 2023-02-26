def reduce_measure(num, unit):
    teaspoons = 0
    
    if unit == 'teaspoons' or unit == 'teaspoon':
      teaspoons = num
    elif unit == 'tablespoons' or unit == 'tablespoon':
      teaspoons = num * 3
    elif unit == 'cups' or unit == 'cup':
      teaspoons = num * 48
      
    cups, rem = divmod(teaspoons, 48)
    tablespoons, teaspoons = divmod(rem, 3)
    
    result = []
    if cups > 0 :
      if cups == 1:
        result.append('1 cup')
      else:
        result.append(str(cups) + ' cups')
    if tablespoons > 0:
      if tablespoons == 1:
        result.append('1 tablespoon')
      else: 
        result.append(str(tablespoons) + ' tablespoons')
    if teaspoons > 0:
      if teaspoons == 1:
        result.append('1 teaspoon')
      else: 
        result.append(str(teaspoons) + ' teaspoons')
        
    if not result:
      return '0 teaspoons'
    else:
      return ', '.join(result)