#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import defaultdict
from collections import Counter
words=[]
data = str('Как и все млекопитающие, киты дышат воздухом при помощи лёгких, являются теплокровными,\n'
           ' кормят детёнышей молоком из молочных желёз и обладают волосяным покровом (хотя и довольно редуцированным).\n'
           'Тело веретенообразное, наподобие обтекаемого тела рыб. Плавники, иногда также называемые ластами, имеют лопастеообразный вид.\n'
           'На конце хвоста расположен плавник из двух горизонтальных лопастей, играющий роль двигателя и стабилизатора, \n'
           'обеспечивая движение вперёд благодаря волнообразным движениям в вертикальной плоскости (в отличие, например, \n'
           'от рыб и водных пресмыкающихся, у которых плоскость движения гребного хвоста горизонтальна). \n'
           'Для защиты кожи от пагубного действия ультрафиолетовых лучей Солнца у разных групп китообразных \n'
           'выработаны разные защитные приспособления: одни, например синий кит, способны увеличивать \n'
           'содержание в коже поглощающих ультрафиолет пигментов; другие, как кашалот, \n'
           'запускают особый стрессовый ответ, как для защиты от кислородных радикалов; третьи, \n'
           'как финвал, используют оба способа. В холодной воде киты поддерживают температуру \n'
           'своего тела благодаря толстому слою жира под кожей. Этот слой защищает внутренние органы от переохлаждения. \n'
           'Из-за того что китам, как и дельфинам, необходимо изредка подниматься на поверхность для дыхания, \n'
           'только половина их мозга может спать в определённый момент времени.')

words = re.split(r'[,.?\n ]+', data) # модуль re  разбивает текст, где разделителдями являются , . пробел и тд

print(f'Количество слов в строке: {len(words)}')
count = {}
for element in words:
    if count.get(element, None):
            # если в словаре ключ со значением элемента списка
            # присутствует, то увеличиваем счетчик на 1
        count[element] += 1
    else:
            # если в словаре ключа со значением элемента
            # списка НЕТ, то создаем ключ со значением 1
        count[element] = 1

    # сортируем словарь по количеству повторений слов в тексте
    sorted_values = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(sorted_values[:10])
