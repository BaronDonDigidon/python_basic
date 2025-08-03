from JSONComparator import JSONComparator

if __name__ == "__main__":
    diff_keys = ["services", "staff", "datetime"]  # список ключей для отслеживания

    comparator = JSONComparator("json_old.json", "json_new.json", diff_keys)
    result = comparator.compare()
    print(result)
    comparator.save_result()
