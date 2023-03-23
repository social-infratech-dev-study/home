def ask():
    print(">>> ", end="")
    answer = input()
    print()
    return answer

def printAskNumber():
    print("총 몇 명의 hjoo3355가 화가 났나요??")
    return ask()

def printAsk(i):
    print(str(i) + ": 이 hjoo3355는 왜 화가 났나요?")
    return ask()
    
print("\n(+_-)^ 오 이런...!\n")

n = int(printAskNumber())
reasons = [(i + 1, printAsk(i + 1)) for i in range(0, n)]

print()
print("(ㅜ^ㅠ) hjoo3355들이 화가 난 이유를 알려드리겠습니다...\n")

for data in reasons:
    i, r = data
    print(str(i) + ": " + r)