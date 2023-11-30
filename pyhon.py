import pandas as pd
import psycopg

with psycopg.connect("postgres://hackathon_2z5k_user:uF2wUEjFpjdKcNwvH3k2Vhx0U6dTPRKv@dpg-cljqanh8mmjc73dbc9t0-a.oregon-postgres.render.com/hackathon_2z5k") as conn:
    with conn.cursor() as cur:

        cur.execute(
            "INSERT INTO test (num, data) VALUES (%s, %s)",
            (100, "abc'def"))

        cur.execute("SELECT * FROM test")
        cur.execute("SELECT * FROM TB_USUARIOS")
        cur.fetchone()
        
        
        for record in cur:
            print(record)

        conn.commit()