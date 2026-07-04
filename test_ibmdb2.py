import ibm_db
import script_vars
from datetime import datetime

# Connection setup for your Db2 v11.5 Database
dsn = (
    f"DATABASE={script_vars.database};"
    f"HOSTNAME={script_vars.hostname};"
    f"PORT={script_vars.port};"
    f"PROTOCOL={script_vars.protocol};"
    f"UID={script_vars.uid};"
    f"PWD={script_vars.pwd};"
)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Connecting via ibm_db v3.2.3 to Db2 v11.5 inside WSL...")

try:
    conn = ibm_db.connect(dsn, "", "")
    print("✅ Connection successful!")

    # Extract data from the store table you created
    stmt = ibm_db.exec_immediate(conn, "SELECT * FROM store")
    row = ibm_db.fetch_assoc(stmt)

    print("\n--- Current Data in 'store' ---")
    while row:
        print(f"ID: {row['ID']} | Name: {row['NAME']} | Cost: ${row['COST']} | Qty: {row['QUANTITY']}")
        row = ibm_db.fetch_assoc(stmt)

    ibm_db.close(conn)
    print("\n✅ Connection safely closed.")

except Exception as e:
    print(f"❌ Connection Failed:\n{str(e)}")

