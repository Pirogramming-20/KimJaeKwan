# 1단계
num = 0

#a에 대한 입력
# 3단게
while True:
    # 2단계
    input_num_a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    if input_num_a.isdigit():
        input_num_a = int(input_num_a)
        if 1<=input_num_a<=3:
            print("잘 입력했습니다")
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
    else:
        print("정수를 입력하세요")

#4단계
for i in range(1, input_num_a + 1):
    num += 1
    print(f"playerA : {num}")

#b에 대한 입력
while True:
    input_num_b = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    if input_num_b.isdigit():
        input_num_b = int(input_num_b)
        if 1<=input_num_b<=3:
            print("잘 입력했습니다")
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
    else:
        print("정수를 입력하세요")
#5단계
for i in range(1, input_num_b + 1):
    num += 1
    print(f"playerB : {num}")