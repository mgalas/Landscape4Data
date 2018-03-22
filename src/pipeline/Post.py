import psycopg2


def main():
    try:
        conn = psycopg2.connect("host=udltest1.cs.ac.uk:5432 dbname=test user=aniraula")
        cur = conn.cursor()
        print(cur.execute('SELECT * FROM notes'))
    except Exception as e:
        print("ERROR")
        print(e)


if __name__ == "__main__":
    main()
