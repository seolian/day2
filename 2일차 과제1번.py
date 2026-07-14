import csv
import json

try:
    with open("students.csv", "r", encoding="utf-8"):
        pass
except FileNotFoundError:
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "score"])
        writer.writerow(["민준", "85"])
        writer.writerow(["서연", "92"])
        writer.writerow(["지우", "abc"])
        writer.writerow(["하늘", "105"])
        writer.writerow(["유진", "78"])


def reader_writer():
    valid_students = []
    scores = []

    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  

            for row_num, row in enumerate(reader, start=2):
                try:
                    score = int(row[1])

                    if score < 0 or score > 100:
                        raise ValueError("허용 범위 초과")

                    valid_students.append([row[0], score])
                    scores.append(score)

                except ValueError as e:
                    if str(e) == "invalid literal for int() with base 10: '{}'".format(row[1]):
                        print(f"{row_num}행 오류 : 숫자 변환 실패")
                    elif str(e) == "허용 범위 초과":
                        print(f"{row_num}행 오류 : 허용 범위 초과")
                    else:
                        print(f"{row_num}행 오류 : 숫자 변환 실패")

    except FileNotFoundError:
        print("students.csv 파일이 없습니다.")
        return

    with open("clean_students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "score"])
        writer.writerows(valid_students)

    summary = {
        "count": len(scores),
        "average": sum(scores) / len(scores) if scores else 0,
        "max": max(scores) if scores else 0
    }

    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)

    print("처리 완료")


def dict_reader_writer():
    valid_students = []
    scores = []

    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, start=2):
                try:
                    score = int(row["score"])

                    if score < 0 or score > 100:
                        raise ValueError("허용 범위 초과")

                    valid_students.append({
                        "name": row["name"],
                        "score": score
                    })
                    scores.append(score)

                except ValueError:
                    print(f"{row_num}행 오류")

    except FileNotFoundError:
        print("students.csv 파일이 없습니다.")
        return

    with open("clean_students_dict.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(valid_students)

reader_writer()
dict_reader_writer()