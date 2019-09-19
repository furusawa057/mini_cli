def main():
    # 入力
    height_cm = int(input("身長(cm)："))
    weight = int(input("体重(kg)："))

    # 計算
    height = height_cm / 100

    # 変数のインライン化
    bmi = round(weight / (height ** 2), 2)

    # 出力
    print(bmi)


if __name__ == '__main__':
    main()
