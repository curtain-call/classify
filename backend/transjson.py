import csv
import json

def transjson(csvpath):
    tableData = []
    with open(csvpath, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 读取的内容是字典格式的
            tableData.append(dict(row))

        return json.dumps(tableData, sort_keys=True, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    transjson('./submissiontest.csv')