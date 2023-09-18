import js

from coordinate import character_data, map_data
from item import Item


# 이전 코드
# def print(*args):
#     '''
#     html 문서 내 출력
#     '''
#     output = js.document.getElementById('output')
#     result = ''
#     for arg in args:
#         result += str(arg) + '\n'
#     result = output.value + result
#     output.value = result

def print(*args):
    '''
    html 문서 내 출력
    '''
    output = js.document.getElementById('output')
    result = ''
    for arg in args:
        result += str(arg)

    if output:
        paragraph = js.document.createElement('p')
        paragraph.innerHTML = result
        paragraph.classList.add('output-item')
        output.appendChild(paragraph)
    else:
        js.console.log(result)

def say(text='', character=None, speech_time=5000):
    '''
    charecter의 말풍선에 출력
    '''
    if character != None:
        character.say(text)
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].say(text, speech_time)
        else:
            print('캐릭터가 없습니다.')

def directions(character=None):
    '''
    character의 방향을 right, left, top, bottom으로 반환
    '''
    d = {0:'right', 1:'top', 2:'left', 3:'bottom'}
    if character != None:
        # TODO: 0번째가 아니라 순회 돌면서 self.name으로 찾아서 directions 반환 
        # return d[character.directions] # self.directions가 제대로 반영 안되어 있음
        return d[character_data[0]['directions']]
    else:
        if character_data[0]['character_obj'] != None:
            # return d[character_data[0]['character_obj'].directions] # self.directions가 제대로 반영 안되어 있음
            return d[character_data[0]['directions']]
        else:
            print('캐릭터가 없습니다.')
            return None
        
def show_item(character=None):
    '''
    character가 가지고 있는 아이템을 보여주는 함수
    '''
    if character != None:
        # TODO: 0번째가 아니라 순회 돌면서 self.name으로 찾아서 items 반환 
        return character_data[0]['items']
    else:
        if character_data[0]['character_obj'] != None:
            # return d[character_data[0]['character_obj'].directions] # self.directions가 제대로 반영 안되어 있음
            return character_data[0]['items']
        else:
            print('캐릭터가 없습니다.')
            return None

def set_item(x, y, name, count=1, description={}, character=None):
    if not (isinstance(x, int) and isinstance(y, int)):
        js.alert('좌표를 확인해주세요')
        print('error.TypeError: Coordinates must be integer')
        return None
       
    if (x<0 or x > map_data['width']-1 or y<0 or y > map_data['height']-1):
        js.alert('월드를 벗어나서 아이템을 추가할 수 없습니다.')
        print('error.TypeError: Coordinates must be integer')
        return None

         
        
    item = Item(x, y, name, count, description)
    item.draw()
    character_data[0]['character_obj'].pick()

def move(character=None):
    if character != None:
        character.move()
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].move()
        else:
            print('캐릭터가 없습니다.')

def turn_left(character=None):
    if character != None:
        character.turn_left()
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].turn_left()
        else:
            print('캐릭터가 없습니다.')

def pick(character=None):
    if character != None:
        character.pick()
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].pick()
        else:
            print('캐릭터가 없습니다.')

def put(character=None):
    if character != None:
        character.put()
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].put()
        else:
            print('캐릭터가 없습니다.')

def repeat(count, f):
    if isinstance(count, int) == True:
        for i in range(0, count):
            f()
    elif isinstance(f, int) == True:
        for i in range(0, f):
            count()

def front_is_clear():
    pass

def left_is_clear():
    pass

def attack(character=None):
    if character != None:
        character.attack()
    else:
        if character_data[0]['character_obj'] != None:
            character_data[0]['character_obj'].attack()
        else:
            print('캐릭터가 없습니다.')