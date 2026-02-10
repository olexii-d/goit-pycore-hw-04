def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 2:
                    continue

                salary_str = parts[1]

                try:
                    salary = int(salary_str)
                except ValueError:
                    continue

                total += salary
                count += 1

    except FileNotFoundError:
        return 0, 0

    average = total / count if count else 0
    return total, average
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")