import pyinputplus as pyip
import random
import time

# 전체 문항 수
numOfquestions = 3
# 정답 개수 -> 정답일 경우 1씩 증가하도록
correctAnswer = 0

# 전체 문항을 순환하면서 문항 번호로 지정
for qNum in range(numOfquestions):
    # 구구단 형태이므로 num1의 범위는 (2, 9)
    num1 = random.randint(2, 9)
    # 구구단 형태이므로 num2의 범위는 (1, 9)
    num2 = random.randint(1, 9)
    # inputStr() 함수에 사용할 prompt 설정
    prompt = f'No.{qNum + 1}: {num1} x {num2} = '

    try:
        # allowRegexes에서 f-string 사용 가능 + '^'와 '$'를 통해 전체 일치
        # blockRegexes를 튜플로 묶어서 첫 번째 인자는 금지(모든 답변), 두 번째 인자는 금지 표현식 작성 시 회신
        pyip.inputStr(prompt=prompt, allowRegexes=[f'^{num1 * num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=5, limit=2)
    except:
        print('Chance missed')
    # try 문을 통과했을 경우의 반응
    else:
        print('Correct!')
        correctAnswer += 1
    
    time.sleep(0.5)

print(f'Score: {correctAnswer} / {numOfquestions}')