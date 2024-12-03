def calculate_feedback(secret, guess):
    """
    根據謎底和猜測計算提示（XAYB）。
    X: 位置正確且數字正確的個數。
    Y: 數字正確但位置不對的個數。
    """
    A = sum(s == g for s, g in zip(secret, guess))
    B = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - A
    return f"{A}A{B}B"


def generate_combinations(digits, length):
    """
    手動生成指定長度的數字排列。
    """
    if length == 0:
        return [""]
    smaller_combinations = generate_combinations(digits, length - 1)
    combinations = []
    for combo in smaller_combinations:
        for digit in digits:
            if digit not in combo:  # 確保不重複
                combinations.append(combo + digit)
    return combinations


def computer_guess(secret):
    """
    電腦猜測謎底的主邏輯。
    """
    digits = "0123456789"
    all_combinations = generate_combinations(digits, 5)

    guess_count = 0
    while True:
        guess = all_combinations[0]  # 挑選列表中的第一個猜測
        guess_count += 1
        feedback = calculate_feedback(secret, guess)
        print(f"程式猜測數字：{guess}")
        print(f"程式根據謎底判斷：{feedback}")

        if feedback == "5A0B":
            print(f"猜中謎底！共猜測次數：{guess_count}")
            return guess

        # 篩選出符合當前提示的所有可能性
        all_combinations = [
            num
            for num in all_combinations
            if calculate_feedback(num, guess) == feedback
        ]


if __name__ == "__main__":
    # 使用者輸入謎底數字
    secret_number = input("請輸入謎底數字（5碼且不重複）：")
    while (
        len(secret_number) != 5
        or len(set(secret_number)) != 5
        or not secret_number.isdigit()
    ):
        secret_number = input("輸入格式錯誤，請重新輸入謎底數字（5碼且不重複）：")

    result = computer_guess(secret_number)
    print(f"謎底為：{result}")
