def hanoi(n, fro, to, tmp):
    global counter
    if n > 1:
        hanoi(n-1, fro, tmp, to)
        print("Move from", fro, "to", to)
        counter += 1
        hanoi(n-1, tmp, to, fro)
    else:
        print("Move from", fro, "to", to)
        counter += 1

number = int(input("원반의 개수를 입력하세요 : "))
counter = 0
hanoi(number, "A", "C", "B")
print("이동횟수 : ", counter)
