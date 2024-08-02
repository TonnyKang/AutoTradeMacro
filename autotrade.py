import pyautogui
import time
import pytesseract

# 각 돔별로 계좌 저장
dom1 = dom2 = dom3 = []

# 화면 전체 사이즈 확인
print(pyautogui.size())


# Save Account
i = 1

x1 = 55 # 계좌목록 첫번째 위치
y1 = 355 # 계좌목록 첫번째 위치

while True:
    img = pyautogui.screenshot(region=(x1 , y1, 110, 30))  # (시작 x좌표, 시작 y좌표, x 길이, y 길이)

    text = pytesseract.image_to_string(img, lang='kor+eng') # 계좌 추출

    # PA로 시작하는 계좌만 dom에 저장
    if text.startswith('PA'):
        if i%3 == 1:    # 첫번째 dom 계좌 저장
            dom1.append(text)
        
        elif i%3 == 2:    # 두번째 dom 계좌 저장
            dom2.append(text)
        
        elif i%3 == 0:    # 세번째 dom 계좌 저장
            dom3.append(text)
        
        y1 += 30 # 다음 계좌 위치만큼
        i += 1

    else:
        break


# 각 dom 변수 지정

for x2, y2 in [(1000, 500), (1000, 1000), (1000, 1500)]:
    pyautogui.click(x2, y2)  # instrumet

    while True:
        img = pyautogui.screenshot(region=(x2+10 , y2+10, 110, 30))

        text = pytesseract.image_to_string(img, lang='kor+eng')

        if text == "NQ 09-24":
            pyautogui.click(x2+15, y2+15)   #클릭 에러 방지 좌표 여유
            
            break

        else:
            y2 += 100

    pyautogui.click(x2+500, y2)  # quantity
    pyautogui.dragTo(x2+520, y2)    # 드래그해서 숫자 변경
    pyautogui.write("1")

# 거래시작
