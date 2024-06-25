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
            out_interface VARCHAR(50),
            sources INT,
            destinations INT,
            services INT,
            FOREIGN KEY (sources) REFERENCES HostObj(uid),
            FOREIGN KEY (destinations) REFERENCES HostObj(uid),
            FOREIGN KEY (services) REFERENCES ServiceObj(uid)
        );
        """)
        print("Tabella 'Policy' creata con successo.")
    else:
        print("La tabella 'Policy' esiste già.")


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

