import random

num = 0

def brGame():
    global num
    while True:
        # 2단계
        input_num_a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        if input_num_a.isdigit():
            input_num_a = int(input_num_a)
            if 1<=input_num_a<=3:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")
        else:
            print("정수를 입력하세요")
    #4단계
    for i in range(1, input_num_a + 1):
        num += 1
        print(f"player : {num}")

while num < 31:
    brGame()
    if num >= 31:
        print("computer win!")
        break
    
    computerInput = random.randint(1,3)
    for i in range(1, computerInput + 1):
        num += 1
        print(f"computer : {num}")
    
    if num >= 31:
        print("player win!")
        break