# 캐릭터 좌표
# 0번째는 default 캐릭터
character_data = [
            {
                'character': 'licat',
                'character_obj': None,
                'x': 0,
                'y': 0,
                'directions': 0, # 0(동, 오른쪽), 1(북), 2(서, 왼쪽), 3(남)
                'items': {}
            }
]

# 맵 전역에 있는 아이템 데이터
# (x, y): {item: 'beeper', count: 1}
item_data = {} 

# 맵 크기
map_data = {
    'height': 5,
    'width': 5
}

running_speed = 1

# 맵에 있는 벽 데이터
# wall_data = [{'wall': [(6, 1)], 'door': [(6, 2)]}]
wall_data = {'wall': [], 'door': [(1, 6),(9,10)]}
