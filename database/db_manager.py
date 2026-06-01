import sqlite3


def init_db():

    conn = sqlite3.connect("fraud_patterns.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scam_patterns (
        pattern TEXT PRIMARY KEY,
        count INTEGER
    )
    """)

    conn.commit()
    conn.close()


def update_pattern(pattern):

    conn = sqlite3.connect("fraud_patterns.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT count FROM scam_patterns WHERE pattern=?",
        (pattern,)
    )

    row = cursor.fetchone()

    if row:
        new_count = row[0] + 1

        cursor.execute(
            "UPDATE scam_patterns SET count=? WHERE pattern=?",
            (new_count, pattern)
        )

    else:

        cursor.execute(
            "INSERT INTO scam_patterns VALUES (?, ?)",
            (pattern, 1)
        )

    conn.commit()
    conn.close()


def get_network_alerts():

    conn = sqlite3.connect("fraud_patterns.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT pattern, count FROM scam_patterns WHERE count >= 3"
    )

    rows = cursor.fetchall()

    conn.close()

    alerts = []

    for pattern, count in rows:
        alerts.append(
            f"Scam pattern '{pattern}' detected across {count} job posts"
        )

    return alerts