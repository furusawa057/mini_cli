def main():
    totalpay = int(input("金額："))
    member = int(input("人数："))

    # 計算 //で0以上だけ残すわりざん
    # onepay = totalpay // member
    # amari = totalpay % member

    onepay, amari = divmod(totalpay, member)

    # 出力 f-string(f記法)という機能 python3.6から使える
    # print("1人当たり" + str(onepay) + "円です。端数は" + str(amari) + "円です。")
    print(f"1人当たり{onepay}円です。端数は{amari}円です。")


if __name__ == '__main__':
    main()
