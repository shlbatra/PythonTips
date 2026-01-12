import duckdb


def main() -> None:
    with duckdb.connect() as conn:
        # Read data from CSV file
        employees = conn.read_csv("/Users/shlba/Desktop/Docs/Study/code/PythonTips/68-PythonDuckdb/data/employees.csv") # Run in memory so deleted when connection closes

        # Preview data from the employees table
        data = conn.execute("SELECT * FROM employees").fetchdf()
        print(data)


if __name__ == "__main__":
    main()
