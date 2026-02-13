def get_cats_info(path: str) -> list[dict]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                cat_id, name, age = parts

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except UnicodeDecodeError:
        print("Помилка кодування файлу (encoding).")
    except OSError as e:
        print(f"Помилка роботи з файлом: {e}")

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)