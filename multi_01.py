from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        for j in file.readline():
            all_data.append(j)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.now()
for number in range(1, 5):
    read_info(f'./file {number}.txt')
end = datetime.now()
result_time = end - start
print(f"Время работы линейного вызова: {result_time}")


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        start = datetime.now()
        p.map(read_info, filenames)
        end = datetime.now()
        result_time = end - start
        print(f"Время работы многопроцессного подхода: {result_time}")