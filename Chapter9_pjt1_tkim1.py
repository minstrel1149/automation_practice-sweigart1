from pathlib import Path
import random

# capitals(주/주도)를 딕셔너리로 묶기
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 저장하고자 하는 폴더 지정
p1 = Path.cwd() / 'result_attachments' / 'walnut_os_mkdir'

# range(n)으로 n개 만큼의 퀴즈 파일 및 정답 파일 생성
for quizNum in range(15):
    quizFile = open(p1 / f'capitalsquiz{quizNum + 1}.txt', mode='w')
    answerFile = open(p1 / f'capitalsquiz_answer{quizNum + 1}.txt', mode='w')

    quizFile.write('Name: \n\nDate: \n\nPeriod: \n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # states라는 리스트를 만들어서 capitals.keys(), 즉 각 state들을 하나의 리스트에 포함
    states = list(capitals.keys())
    # states 리스트 셔플 진행
    random.shuffle(states)

    # range(n)으로 n개 만큼의 문제 생성
    for qNum in range(50):
        # 정답 지정 -> capitals[key] -> key == states[i]
        correctAnswer = capitals[states[qNum]]
        # 일단 모든 capitals.values()를 오답으로 지정한 뒤
        wrongAnswers = list(capitals.values())
        # 그 중 정답을 오답 리스트에서 제외 : del wrongAnswers[i] -> i == wrongAnswers.index(correctAnswer)
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # 오답 중 3개를 random.sample()을 활용하여 추출
        wrongAnswers = random.sample(wrongAnswers, 3)
        # 정답 옵션은 오답 3개 + 정답
        answerOptions = wrongAnswers + [correctAnswer]
        # answerOptions 셔플 진행
        random.shuffle(answerOptions)

        quizFile.write(f'{qNum + 1}. What is the capital of {states[qNum]}?\n')
        # range(4)를 통해 4개의 선택지를 순환하며 작성
        for i in range(4):
            # "ABCD"[i] + answerOptions[i]
            quizFile.write(f'{"ABCD"[i]}. {answerOptions[i]}\n')
        quizFile.write('\n\n')

        # 정답 파일에서는 "ABCD"[i] -> i == answerOptions.index(correctAnswer)
        answerFile.write(f'{qNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')

    quizFile.close()
    answerFile.close()

print('Process Done!')