# 함수 정의
def convert_score(grade):
    match grade:
        case 'A+':
            score = 4.5
        case 'A':
            score = 4.0
        case 'B+':
            score = 3.5
        case 'B':
            score = 3.0
        case 'C+':
            score = 2.5
        case 'C':
            score = 2.0
        case 'D+':
            score = 1.5
        case 'D':
            score = 1.0
        case 'F':
            score = 0.0


    return score


# 반복
submit_credit, archive_credit = 0, 0
submit_gpa, archive_gpa = 0.0, 0.0
while True:
    print('작업을 선택하세요.')
    print('    1.입력')
    print('    2.계산')

    user_value = input()
    value = int(user_value)

    match value:
        case 1:
            print('학점을 입력하세요.')
            user_value = input()
            credit = int(user_value)

            print('평점을 입력하세요.')
            user_value = input()
            gpa = convert_score(user_value)
            print('입력되었습니다.')

            #계산
            if gpa > 0:  #F학점일 경우(gpa==0)에만 제출용 학점에서 제외
                submit_credit += credit  #시그마 학점
                submit_gpa += gpa * credit  #시그마 평점 * 학점
            archive_credit += credit   #열람용 학점은 F학점도 포함
            archive_gpa += gpa * credit

        case 2:
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit
            print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str("%.2f" % submit_gpa) + ')')
            print('열람용: ' + str(archive_credit)+ '학점' + '(GPA: ' + str("%.2f" % archive_gpa) + ')')
            print('\n프로그램을 종료합니다.')
            break