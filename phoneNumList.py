'''
출처 : Phone number list
'''

"""
def solution(phone_book):
    c=0
    seek = min(phone_book)

    for i in phone_book:
        if not i.find(seek):
            c+=1
            if c>1:
                return False
    return True
"""

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    print(hash_map)

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            print("number",number,"phone_number",phone_number)
            temp += number
            print(temp)
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer



print("1",solution(["119", "97674223", "1195524421"])) # return false
print("2",solution(["123","456","789"])) # return true
print("3",solution(["12","123","1235","567","88"])) # return false