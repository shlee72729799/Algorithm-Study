def find_max_num(array):
    max_number = array[0]

    for number in array:
        if number > max_number:
            max_number = number
    return max_number




print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))


#어떻게 하면은 정답을 찾아낼 수 있을지에 대해 아이디어를 글로 써본 다음에 코드를 작성하기

# 1. 하나의 원소를 다른 원소들과 비교해서 최대값인지 분석하는 방법
# 2. 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법.
