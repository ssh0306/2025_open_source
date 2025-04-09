# while 반복문 안쪽 코드 업데이트

def select_menu(i):
    menus[i][1] = menus[i][1] + 1
    print(f"{menus[i][0]} {menus[i][1]}잔 주문...")
    subtotal = 0
    for j in range(len(menus)):
        subtotal = subtotal + (prices[j] * menus[j][1])
    print(f"소계 : {subtotal}")


def print_receipt():
    print("=" * 38)
    # print("품명\n단가 / 수량 / 금액")
    total_price = 0
    for j in range(len(menus)):
        if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
            print(f"품명: {menus[j][0]}\n\t단가: {prices[j]} / 수량: {menus[j][1]:2} / 금액: {menus[j][1] * prices[j]:6}")
            total_price = total_price + (menus[j][1] * prices[j])  # 가격 리스트에서 가격 추출해서 합산
    print(f"총 금액은 {total_price}원 입니다.")


menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0], ["자바칩 프라푸치노", 0]]  # [[메뉴, 수량], ...]
prices = [2000, 2500, 2400, 7000]

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "

while True:
    menu = input(f"{menu_lists}{len(menus)+1}) 주문 종료 : ")
    #if int(menu) > 0 and int(menu) < len(menus):
    if 0 < int(menu) <= len(menus):  # 1 ~ 4
        select_menu(int(menu)-1)
    elif menu == "5":
        print("주문을 종료합니다")
        break
    else:
        print("잘못된 주문입니다")


print_receipt()
