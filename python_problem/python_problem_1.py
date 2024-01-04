# 1단계
num = 0

# 3단게
while True:
    # 2단계
    input_num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    if input_num.isdigit():
        input_num = int(input_num)
        if 1<=input_num<=3:
            print("잘 입력했습니다")
            break
        else:
            print("1,2,3 중 하나를 입력하세요")
    else:
        print("정수를 입력하세요")

#4단계
for i in range(1, input_num + 1):
    print(f"playerA : {i}")