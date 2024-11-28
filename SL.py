# 8620型保存機リスト
saved_locomotives_8620 = {
    8622, 48624, 48640, 78653, 68691, 78693, 58680, 58683,
    8620, 28651, 58623, 8630, 78675, 48650, 58685, 68692,
    78626, 48696, 88622, 58654, 48647
}

# 9600型保存機リスト
saved_locomotives_9600 = {
    49648, 59601, 69644, 39628, 49643, 59683, 19671, 59672,
    59611, 49600, 29638, 9645, 59609, 49694, 9615, 9613,
    9616, 79616, 59614, 79615, 9643, 9625, 9667, 49671,
    9687, 9608, 29622, 9628, 9646, 19648, 49616, 9633,
    79642, 59634, 19633, 49627, 59647, 59684, 29611, 69665, 29612
}

def calculate_8620_production_order(number):
    """8620形の製造順を計算"""
    ten_thousands = int(number // 10000)  # 万の位
    last_two_digits = int(number % 100)  # 下2桁
    return ten_thousands * 80 + (last_two_digits - 20) + 1

def calculate_9600_production_order(number):
    """9600形の製造順を計算"""
    ten_thousands = int(number // 10000)  # 万の位
    last_two_digits = int(number % 100)  # 下2桁
    return ten_thousands * 100 + last_two_digits + 1

def determine_locomotive_type_and_calculate(number):
    """千の位と百の位で形式を判定し、対応する製造順を計算"""
    middle_digits = (number // 100) % 100  # 千の位と百の位を抽出
    if middle_digits == 86:  # 86なら8620型
        production_order = calculate_8620_production_order(number)
        is_saved = number in saved_locomotives_8620
        return "8620型", production_order, is_saved
    elif middle_digits == 96:  # 96なら9600型
        production_order = calculate_9600_production_order(number)
        is_saved = number in saved_locomotives_9600
        return "9600型", production_order, is_saved
    else:
        raise ValueError("無効な機関車番号です（86または96が必要です）。")

# 機関車番号を入力
try:
    locomotive_number = int(input("機関車の番号を入力してください: "))
    if locomotive_number < 0:
        print("エラー: 正の整数を入力してください。")
    else:
        locomotive_type, production_order, is_saved = determine_locomotive_type_and_calculate(locomotive_number)
        status = "保存機" if is_saved else "解体済み"
        print(f"機関車番号 {locomotive_number} は {locomotive_type} の製造順 {production_order} 両目 ({status}) です。")
except ValueError as e:
    print(f"エラー: {e}")

