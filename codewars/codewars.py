# Digital Root
# my solution:
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))

# regular solution:
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# clever solution:
def digital_root(n):
    return n%9 or n and 9   # use the digital root formula

# Isograms
# my solution:
def is_isogram(string):
    if len(string) == 0:
        return True
    low_string = string.lower()
    word_set = set()
    for i in low_string:
        word_set.add(i)
    return False if len(word_set) < len(string) else True
    
# better version
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# Tribonacci Sequence
# my solution:
def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 4:
        return signature[0 : n]
    for i in range(n-3):
        signature.append(sum(signature[i : i + 3]))
    return signature

# better version
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

# format time
# my solution:
def make_readable(seconds):
    second = seconds % 60
    minute = seconds // 60 % 60
    hour = seconds // 3600
    return f'{hour:02}:{minute:02}:{second:02}'

# better version
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

# number of Duplicates
# my solution
def duplicate_count(text):
    duplicate_list = []
    low_text = list(text.lower())
    char_dic = {char: low_text.count(char) for char in low_text}
    for char in char_dic:
        if char_dic[char] > 1:
            duplicate_list.append(char)
    return len(duplicate_list)

# better version
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# digital game
# my solution
def dig_pow(n, p):
    num = str(n)
    left = 0
    for _ in range(len(num)):
        left += int(num[_]) ** (p + _)
    if left % n != 0:
        return -1
    return int(left / n)

# better version
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

# do some rank
# my solution
def order(sentence):
    index_list = []
    word_list = sentence.split()
    rank_dic = {}
    for li in word_list:
        for char in li:
            if char.isdigit():
                index_list.append(char)
    for i in range(len(word_list)):
        rank_dic[word_list[i]] = index_list[i]
    new_list = [''] * len(word_list)
    for j,k in rank_dic.items():
        new_list[int(k) - 1] = j
    return ' '.join(new_list)

# magic version
def order(sentence):
  return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))

# Valid Braces
# my solution:
def valid_braces(string):
    stack_list = []
    for brace in string:
        if brace in '([{':
            stack_list .append(brace)
        elif brace in ')]}':
            if not stack_list:
                return False
            top_brace = stack_list.pop()
            if brace == ')' and top_brace != '(':
                return False
            if brace == ']' and top_brace != '[':
                return False
            if brace == '}' and top_brace != '{':
                return False
    return not stack_list

# regular solution:
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  

# smart solution:
def validBraces(string):
  while '{}' in string or '()' in string or '[]' in string:
      string=string.replace('{}','')
      string=string.replace('[]','')
      string=string.replace('()','')
  return string==''

# find the repeat
# my solution:
def duplicate_encode(word):
    low_word = word.lower()
    multiple_char_list = []
    single_char_list = []
    new_word = ''
    count_dic = {char: low_word.count(char) for char in low_word}
    for i, j in count_dic.items():
        if j > 1:
            multiple_char_list.append(i)
        else:
            single_char_list.append(i)
    for char in low_word:
        if char in single_char_list:
            new_word += '('
        else:
            new_word += ')'
    return new_word

# better solution:
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# Equal Sides Of An Array
# solution:
def find_even_index(arr):
    list1 = []
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# RGB -> Hex
# my solution:
def rgb(r, g, b):
    def check(deci):
        if deci > 255:
            return 255
        if deci < 0:
            return 0
        return deci
    def two(hex):
        if len(hex) == 1:
            return '0' + hex
        return hex
    
    r_hex = two(hex(check(r))[2:]).upper()
    g_hex = two(hex(check(g))[2:]).upper()
    b_hex = two(hex(check(b))[2:]).upper()

    return r_hex + g_hex + b_hex

# better solution:
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

# snail sort
# my solution:
def snail(snail_map:list):
    
    def get_num():
        for i in range(len(snail_map)):
            result.append(snail_map[0][i])
        for j in range(1, len(snail_map)):
            result.append(snail_map[j][len(snail_map)-1])
        for k in range(len(snail_map)-2, -1, -1):
            result.append(snail_map[len(snail_map)-1][k])
        for l in range(len(snail_map)-2, 0, -1):
            result.append(snail_map[l][0])
    
    def pop_arr():
        snail_map.pop(0)
        snail_map.pop()
        for x in range(len(snail_map)):
            snail_map[x].pop(0)
            snail_map[x].pop(-1)

    result = []
    n = len(snail_map)
    while n >= 3:
        get_num()
        pop_arr()
        n -= 2   
    
    if snail_map[0] == []:
        return result
    elif n == 2:
        result.extend([snail_map[0][0], snail_map[0][1], snail_map[1][1], snail_map[1][0]])
        return result
    else:
        result.append(snail_map[0][0])
        return result
    
# better expression:
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                ret.append(array[n][x])
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in range(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
    return ret

# clever solution:
import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

# let's be greedy
# my solution
def score(dice: list):
    score = 0
    score_dic = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200,
        11: 100,
        15: 50
    }
    dice_dic = {x: dice.count(x) for x in dice}
    
    
    
    for num, count in dice_dic.items():
        if num == 1 or num == 5:
            if count >= 3:
                score += (score_dic.get(num) + score_dic.get(num + 10) * (count - 3))
            else:
                score += score_dic.get(num + 10) * count
        else:
            if count >= 3:
                score += score_dic.get(num)
    return score

# other version
def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

# PaginationHelper
# my solution:
# TODO: complete this class

import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
 
    # returns the number of pages
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= math.ceil(len(self.collection) / self.items_per_page):
            return -1
        if page_index == math.ceil(len(self.collection) / self.items_per_page) - 1:
            return len(self.collection) % self.items_per_page
        return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        return int(item_index / self.items_per_page)
    
# move zero
# my solution
def move_zeros(lst: list):
    for num in lst:
        if num == 0:
            lst.append(0)
            lst.remove(0)
    return lst

# better version:
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

# String incrementer
# my solution:

def increment_string(string):
    check = []
    result = ''
    
    if string == '':
        return '1'
    
    if string[-1].isalpha():
        return string + '1'
    
    for i in range(len(string), 0, -1):
        if not string[i-1].isdigit():
            break
        check.append(string[i-1])
    
    for num in range(len(check), 0, -1):
        result += check[num-1]
    n = len(result)
    result = int(result)
    result += 1
    result = str(result)
    if len(result) < n:
        result = '0' * (n-len(result)) + result

    return string[:len(string)-len(check)] + result

# better version:
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

# prod of fib
# my solution
def productFib(prod):
    
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    j = 0
    while fib(j) * fib(j+1) < prod:
        j += 1
        
    if fib(j) * fib(j+1) == prod:
        return [fib(j), fib(j+1), True]
    return [fib(j), fib(j+1), False]

# better version:
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:               # *将fib数列与循环结合
    a, b = b, a + b
  return [a, b, prod == a * b]      # *将布尔值与判断结合

# Sum of Intervals
# my solution:  
def sum_of_intervals(intervals):
    
    def merge(array):
        result = [array[0]]
        for tup in array:
            if tup[0] < result[-1][1]:
                result[-1] = (result[-1][0], max(result[-1][1], tup[1]))
            else:
                result.append(tup)
        return result

    if intervals == []:
        return 0
    return sum([x[1] - x[0] for x in merge(sorted(intervals))])
    
# better solution:
def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

# str to num
# my solution:
def parse_int(string: str):
   
    def trans(less_than_thousand: list):
        
        word_to_num = {'zero': '0', 
                       'one': '1', 
                       'two': '2', 
                       'three': '3', 
                       'four': '4', 
                       'five': '5', 
                       'six': '6', 
                       'seven': '7', 
                       'eight': '8', 
                       'nine': '9',
                       'ten': '10',
                       'eleven': '11',
                       'twelve': '12',
                       'thirteen': '13',
                       'fourteen': '14',
                       'fifteen': '15',
                       'sixteen': '16',
                       'seventeen': '17',
                       'eighteen': '18',
                       'nineteen': '19',
                       'twenty': '20',
                       'thirty': '30',
                       'forty': '40',
                       'fifty': '50',
                       'sixty': '60',
                       'seventy': '70',
                       'eighty': '80',
                       'ninety': '90'}
        
        if 'hundred' in less_than_thousand:
            hun = less_than_thousand[0]
            if len(less_than_thousand) == 3:
                ten = less_than_thousand[-1]
            else:
                ten = 'zero'
        else:
            ten = less_than_thousand[0]
            hun = 'zero'
            
        hun_num = int(word_to_num[hun]) * 100
        if '-' in ten:
            ten_num = int(word_to_num[ten.split('-')[0]]) + int(word_to_num[ten.split('-')[1]])
        else:
            ten_num = int(word_to_num[ten])
            
        return hun_num + ten_num    
    
    if string == 'one million':
        return 1000000
    num_list = string.split()
    while 'and' in num_list:
        num_list.remove('and')
    
    if 'thousand' in num_list:
        if num_list[-1] != 'thousand':
            return trans(num_list[:num_list.index('thousand')]) * 1000 + trans(num_list[num_list.index('thousand') + 1:])
        return trans(num_list[:num_list.index('thousand')]) * 1000
    return trans(num_list)

# better version:
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)

# clever version:
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': group *= words[w]
        elif w in words: group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group