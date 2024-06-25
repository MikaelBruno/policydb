import mysql.connector

def process_result(device_id, in_interfaces, out_interfaces, sources, destinations, services):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="example",
      database="PolicyDB"
    )

    mycursor = mydb.cursor()
    sources_hostobj_id = []
    destinations_hostobj_id = []
    service_id = []
    
    
    for ip in sources:
        sql = "INSERT INTO HostObj (subnet_ipv4) VALUES (%s)"
        val = (ip)
        mycursor.execute(sql, val)
        mydb.commit()
        sources_hostobj_id.append(mycursor.lastrowid)
        
    for ip in destinations:
        sql = "INSERT INTO HostObj (subnet_ipv4) VALUES (%s)"
        val = (ip)
        mycursor.execute(sql, val)
        mydb.commit()
        destinations_hostobj_id.append(mycursor.lastrowid)
        
    for service in services:
        sql = "INSERT INTO ServiceObj (protocol) VALUES (%s)"
        val = (service)
        mycursor.execute(sql, val)
        mydb.commit()
        service_id.append(mycursor.lastrowid)