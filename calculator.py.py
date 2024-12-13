MAX_ERROR = 1e-5
print('Welcome to interactive calculator')

end_of_input = False

while not end_of_input:

    expression = input('Enter mathematical expression : ')

    for char in '() ':
        expression = expression.replace(char, '') # remove parentheses

    if expression == 'q':
        # write your code here #
        break                                       #종료
        continue                                   # skip below codes

    elif '+' in expression:
        n1, n2 = expression.split('+')  
        a = float(n1)
        b = float(n2)
        print(format(a + b, '.3f'))
    
    elif '*' in expression:
        n1, n2 = expression.split('*')
        a = float(n1)
        b = float(n2)
        print(format(a * b, '.3f'))

    elif '//' in expression:
        n1, n2 = expression.split('//')
        a = int(n1)                                 #정수만 입력 받으므로 int 사용
        b = int(n2)
        if b == 0:
            print("Division by zero error")
        else:
            print(format(a // b))                    #몫이나 나머지는 항상 정수이므로 .3f 필요 없다

    elif '/' in expression:
        n1, n2 = expression.split('/')
        a = float(n1)
        b = float(n2)
        if b == 0:
            print("Division by zero error")        #0으로 나누면 에러 발생
        else:
            print(format(a / b, '.3f'))
   
    elif '%' in expression:
        n1, n2 = expression.split('%')
        a = int(n1)
        b = int(n2)
        if b == 0:
            print("Division by zero error")
        else:
            print(format(a % b))
    
    elif '^' in expression:
        n1, n2 = expression.split('^')
        a = float(n1)
        b = float(n2)
        print(format(a ** b, '.3f'))

    elif 'P' in expression:
        n1, n2 = expression.split('P')
        a = int(n1)
        b = int(n2)
        c = 1
        if a >= b:
            for i in range(b):              #0~(b-1), 즉 b번을
                c = c * a                   # c에다 a를 곱하고    
                a = a-1                     # a에서 1을 뺀 후 곱하는 것을 for 함수로 b번 반복한다
        else:
             break           
        print(c)
    
    elif 'C' in expression:
        n1, n2 = expression.split('C')
        a = int(n1)
        b = int(n2)
        c = 1
        d = 1
        if a >= b:
            for i in range(b):                 #우선 a P b를 계산하고
                c = c * a
                a = a-1
            for i in range(b):                 #그것을 1로 나누고 그 후에 1을 더하는 것을 b번 반복
                c = c / d
                d = d + 1
        else:
             break           
        print(c)
    
    


    # write your code here (*, /, //, %, ^, P, C)

    elif 'r' in expression:
        n1 = expression.replace('r', '')
        a = float(n1)
        MAX_ERROR = 0.00001                     
        y = 1
        q = a / y                                               #초기 q 변수 정의
        while  max((q,y))-min((q,y)) > MAX_ERROR:               #뉴턴 근사법에서 오차범위가 q-y의 절댓값이므로 그것이 최대 오차보다 작거나 같지 않을때 while문이 반복
            q = a / y                                           # q는 Qoutient 값
            y = (y + q) / 2                                     #y는 Guess 이자 Average 값
        print(format(y, '.3f'))
        # write your code here #

    elif 'g' in expression:
        n1, n2 = expression.replace('g', '').split(',')
        a = int(n1)
        b = int(n2)
        c = max((a,b))                                          #유클리드 호제법을 쓰기 위해 더 큰 값을 c로 두고 작은 값을 d로 둠
        d = min((a,b))
        if c % d == 0:                                          #더 큰 값이 작은 값으로 나누어 진다면 작은값이 최대 공약수
            print(d)
        else:
            while c % d != 0:                                   #유클리드 호제법은 remainder 즉 나머지가 0일때까지 반복되므로 이를 while 문으로 구현
                e = d                                           #d값을 c에 assign 해야하는데 밑에서 d 값이 바뀌어 버리므로 미리 e라는 변수에 초기 d값을 설정 해놓고 이를 밑에 c에 적용
                d = c % d
                c = e        
            print(d)
       
    elif 'b' in expression:
        n1 = expression.replace('b', '')
        a = int(n1)   
        b = 1    
        c = 0    
        if a > 0:                                               #입력값이 양수인 경우와 음수인 경우를 분류
            while 2**b <= a:                                    #2진수의 자릿수를 계산
                b = b + 1                                     
            for i in range(b):
               c = c + (a // 2**(b - 1)) * 10**(b - 1)          #입력값을 입력값보다 크지 않은 2의 최대 거듭제곱수로 나누고 그 값을 구한 자릿수에 입력
               a = a % 2**(b-1)                                 #a를 위에서 사용한 값을 뺀 값이지만 그것을 나머지로 구현
               b = b - 1                                        #그 다음으로 큰 2의 거듭제곱수로 나누기 위해 b에서 1을 빼고 이를 while문으로 끝까지 반복
            print(c)
        elif a < 0: 
            while 2**b * (-1) >= a:                             #a가 음수일 때, a값에 -1을 곱해서 2진수 변환을 진행
                b = b + 1
            for i in range(b):
               c = c + (-a // 2**(b - 1)) * 10**(b - 1)
               a = -(-a % 2**(b-1))
               b = b - 1
            print(-c)                                           #입력 때 -부호를 곱해준다
        else: 
            print(c)

    elif 'd' in expression:
        n1 = expression.replace('d', '')                        
        a = int(n1)
        b = 0
        c = 0
        if a > 0:                                               #2진수 때와 마찬가지로 양수와 음수의 입력값을 구분
            while a != 0:                                       #입력값에서 숫자를 빼는 방식으로 진행하여 a가 0이 될때까지 while문으로 반복
                b = b + (a % 10) * (2**c)                       #입력값의 맨 마지막 자릿수를 나머지로 구하고 이것에다 2의 0승을 곱한 후 a에서 그 자릿수를 빼고 나누기를 하여 마지막 자릿수를 한칸 낮추고 곱해지는 수에 2를 한번더 곱하는 과정을 반복
                a = (a - (a % 10)) // 10                        #실수 입력 시 큰 수 계산의 오류 방지를 위해 나누기를 몫으로 구현
                c = c + 1
        elif a < 0:
            while a != 0:                                       #음수 일때는 입력값에 -1을 곱하고 결과를 구한 후 다시 -부호를 씌워서 계산 
                b = b - (-a % 10) * (2**c)
                a = -(-a - (-a % 10)) // 10
                c = c + 1
        print(b)

    elif 's' in expression:
        n1 = expression.replace('s', '')
        a = float(n1)
        b = 0                                                   #첫번째 테일러항
        c = 1                                                   #비교할 b다음의 테일러항 -> 계산의 정확성을 위해 c로 답을 출력
        d = 1                                                   #d는 (2n+1)! 에서의 2n+1의 역할
        e = 1                                                   #e는 (2n+1)! 에서의 (2n+1)!의 역할
        f = 0                                                   #f는 (-1)**n 의 n의 역할
        MAX_ERROR = 0.00001
        while max((b,c)) - min((b,c)) > MAX_ERROR:                                  #하나의 항과 그 다음 항의 오차가 0.00001보다 작아질 때까지 함수 반복
            for i in range(d):                                                      #for 함수 이용해 (2n+1)! 값 구하기
                e = e * (i+1)
            b = b + ((a**d) / e) * (-1)**(f)                                          #b에다 각 항의 값을 하나하나 더해가고 이를 그 다음 항까지 더한 c와 while 문에서 비교
            c = b + ((a**(d+2)) / (e * (d+1) * (d+2))) * (-1) **(f+1)                 #b의 다음 급수
            d = d + 2                                                                 #2n+1 이므로 2를 더함
            f = f + 1
            e = 1
        print(format(c,'.3f'))

    elif 'c' in expression:
        n1 = expression.replace('c', '')
        a = float(n1)
        b = 1                                                   #첫번째 테일러항
        c = 0                                                   #비교할 b다음의 테일러항 -> 계산의 정확성을 위해 c로 답을 출력 -> b에 첫번째 항은 1이므로 b에 1을 입력시켜놓고 그 이후 항부터 while함수로 추가
        d = 2                                                   #d는 (2n)! 에서의 2n의 역할
        e = 1                                                   #e는 (2n)! 에서의 (2n)!의 역할
        f = 1                                                   #f는 (-1)**n 의 n의 역할 -> b에 추가되는 항이 테일러 급수의 2번째 항부터이므로 1로 시작
        MAX_ERROR = 0.00001
        while max((b,c)) - min((b,c)) > MAX_ERROR:                                  #하나의 항과 그 다음 항의 오차가 0.00001보다 작아질 때까지 함수 반복
            for i in range(d):                                                      #for 함수 이용해 (2n)! 값 구하기
                e = e * (i+1)
            b = b + ((a**d) / e) * (-1)**(f)                                          #b에다 각 항의 값을 하나하나 더해가고 이를 그 다음 항까지 더한 c와 while 문에서 비교
            c = b + ((a**(d+2)) / (e * (d+1) * (d+2))) * (-1) **(f+1)                 
            d = d + 2                                                                 
            f = f + 1
            e = 1
        print(format(c,'.3f'))
        # write your code here #

    # write your code here (b, d, s, c)

    #####################################################
    ################### Do not change ###################
    #####################################################

    elif '-' in expression:
        try:
            if '--' in expression:
                n1, n2 = expression.split('--')
                a = float(n1)
                b = - float(n2)
                
            else:
                if expression[0] != '-':
                    n1, n2 = expression.split('-')
                    a = float(n1)
                    b = float(n2)
            
                else:
                    _, n1, n2 = expression.split('-')
                    a = -float(n1)
                    b = float(n2)
            
            print(format(a - b, '.3f'))
            continue

        except:
            print("Unknown expression")

    else:
        print("Unknown expression")