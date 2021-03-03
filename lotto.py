from random import randint

# 번호 뽑기
def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        
        if num not in numbers:
            numbers.append(num)
	
    numbers.sort()
    return numbers
	
#당첨 번호 뽑기
def gacha():
    gacha = generate_numbers(7)

    # 6개의 일반 당첨 번호 + 1개의 보너스 번호
    result = sorted(gacha[:6]) + gacha[6:]
    return result
	
#겹치는 번호 개수 확인
def count_matches(numbers, win_numbers):
    count = 0

    for num in numbers:
        if num in win_numbers:
            count += 1

    return count
	
#당첨금 확인
def check_prize(numbers, win_numbers):
    count = count_matches(numbers, win_numbers[:6])
    bonus = count_matches(numbers, win_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0