import sys
import os
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    try:
        parts = line.split(" ", 3)
        date = parts[0]
        time = parts[1]
        level = parts[2]
        message = parts[3]
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }
    except IndexError:
        return None

def load_logs(file_path: str) -> list:
    logs = []
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл за шляхом {file_path} не знайдено!")
    
    with open(file_path, 'r') as file:
        for line in file:
            log_entry = parse_log_line(line.strip())
            if log_entry:
                logs.append(log_entry)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    level_counts = defaultdict(int)
    for log in logs:
        level_counts[log['level']] += 1
    return dict(level_counts)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")


def main():

    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
        
        log_counts = count_logs_by_level(logs)
        
        display_log_counts(log_counts)

        if level_filter:
            filtered_logs = filter_logs_by_level(logs, level_filter)
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
