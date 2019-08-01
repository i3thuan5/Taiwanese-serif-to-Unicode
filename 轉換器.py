import csv

def 轉換(text):
    with open('unicode.csv') as csvfile:
        對應表 = csv.DictReader(csvfile)
        for row in 對應表:
            text = text.replace(chr(int(row['原始編碼'], 16)), row['對應編碼'])
    return text
# def 掠出對應表():
#     with open('unicode.csv') as csvfile:
#         對應表 = csv.DictReader(csvfile)
#         for row in 對應表:
#             print(row['對應編碼'], row['原始編碼'])
#     return 對應表
# 
# 對應表 = 掠出對應表()
# 
# if __name__ == '__main__':
#     掠出對應表()