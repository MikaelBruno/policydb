import mysql.connector

def create_database(mycursor):
    mycursor.execute("SHOW DATABASES")
    existing_databases = [db[0] for db in mycursor]
    if "PolicyDB" not in existing_databases:
        mycursor.execute("CREATE DATABASE PolicyDB")
        print("Database 'PolicyDB' creato con successo.")
    else:
        print("Il database 'PolicyDB' esiste già.")

def create_tables(mycursor):
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    existing_tables = [table[0] for table in tables]

    if 'HostObj' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE HostObj (
           uid INT AUTO_INCREMENT PRIMARY KEY,
           subnet_ipv4 VARCHAR(18)
        );
        """)
        print("Tabella 'HostObj' creata con successo.")
    else:
        print("La tabella 'HostObj' esiste già.")

    if 'ServiceObj' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE ServiceObj (
           uid INT AUTO_INCREMENT PRIMARY KEY,
           protocol VARCHAR(18)
        );
        """)
        print("Tabella 'ServiceObj' creata con successo.")
    else:
        print("La tabella 'ServiceObj' esiste già.")

    if 'Policy' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE Policy (
            id INT AUTO_INCREMENT PRIMARY KEY,
            device_id VARCHAR(50),
            in_interface VARCHAR(50),
            out_interface VARCHAR(50)
        );""")
        print("Tabella 'Policy' creata con successo.")
    else:
        print("La tabella 'Policy' esiste già.")
        
    if 'Policy_Source_HostObj' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE Policy_Source_HostObj (
            policy_id INT,
            host_id INT,
            FOREIGN KEY (policy_id) REFERENCES Policy(id),
            FOREIGN KEY (host_id) REFERENCES HostObj(uid),
            PRIMARY KEY (policy_id, host_id)
        );""")
        print("Tabella 'Policy_Source_HostObj' creata con successo.")
    else:
        print("La tabella 'Policy_Source_HostObj' esiste già.")
        
    if 'Policy_Destination_HostObj' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE Policy_Destination_HostObj (
            policy_id INT,
            host_id INT,
            FOREIGN KEY (policy_id) REFERENCES Policy(id),
            FOREIGN KEY (host_id) REFERENCES HostObj(uid),
            PRIMARY KEY (policy_id, host_id)
        );""")
        print("Tabella 'Policy_Destination_HostObj' creata con successo.")
    else:
        print("La tabella 'Policy_Destination_HostObj' esiste già.")
        
    if 'Policy_Service' not in existing_tables:
        mycursor.execute("""
        CREATE TABLE Policy_Service (
            policy_id INT,
            service_id INT,
            FOREIGN KEY (policy_id) REFERENCES Policy(id),
            FOREIGN KEY (service_id) REFERENCES ServiceObj(uid),
            PRIMARY KEY (policy_id, service_id)
        );""")
        print("Tabella 'Policy_Service' creata con successo.")
    else:
        print("La tabella 'Policy_Service' esiste già.")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example"
)

mycursor = mydb.cursor()
create_database(mycursor)
    
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example",
  database="PolicyDB"
)

mycursor = mydb.cursor()

create_tables(mycursor)

mydb.commit()
mycursor.close()
mydb.close()

