import random

characters = ["医师皮特", "实习警察", "小女孩凯瑟琳", "小男孩卢卡斯", "灵媒者艾琳", "狩魔猎人闪电", "神父迈克尔", "神秘女巫"]
parti = ["hd","xyf","hyx","hbh","zrx","fx","hwf","yzk"]

while characters:
    print(characters.pop(random.randrange(len(characters))) + ": " + parti.pop(random.randrange(len(parti))))