import psycopg2   
import psycopg2.extras  #for getting in dictionary

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '12345678'
port_id = 5001
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password= pwd,
        port = port_id)
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS employee')

    create_script = '''CREATE TABLE IF NOT EXISTS employee (
                            id  int PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            salary int,
                            dept_id varchar(30)) '''
    
    cur.execute(create_script)

    insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    insert_value = (1, 'Vivek', 50000, 'A1'), (2, 'Teja', 50000 , 'A2'), (3, 'Sai', 45000, 'A3')
    for record in insert_value:
        cur.execute(insert_script, record)

    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall():
        print(record[1], record[2])  #or we can use record['column name'] , record['colum_name] we can acces directly using colums name

    conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()