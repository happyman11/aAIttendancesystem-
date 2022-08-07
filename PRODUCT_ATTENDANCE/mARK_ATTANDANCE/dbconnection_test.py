import mysql.connector
from mysql.connector import Error

def dbconnectcion(hosting,user,pssd):
    try:
    
        mydb = mysql.connector.connect(
                                       host=hosting,
                                       user=user,
                                       password=pssd
                                       )
        msg="Connected"
        return(mydb,msg)
        
    except Error as e:
        mydb=0
        msg="Error while connecting to MySQL"+e
        print("Error while connecting to MySQL", e)
        return( mydb,msg)   

def dbconnectcion_database(hosting,user,pssd,database_name):
    try:
    
        mydb = mysql.connector.connect(
                                       host=hosting,
                                       user=user,
                                       password=pssd,
                                       database=database_name
                                      ) 
                                    
        msg="Connected"
        return(mydb,msg)
        
    except Error as e:
        mydb=0
        msg="Error while connecting to MySQL"+e
        print("Error while connecting to MySQL", e)
        return( mydb,msg) 

def checkdb_exist(hosting,user,pssd,database_name):
    
    mydb,status=dbconnectcion(hosting,user,pssd)
    
    if status =="Connected" :
      
        try:
            mycursor = mydb.cursor()
            querry="USE "+str(database_name)
            mycursor.execute(querry)
            print("Database Existed")
            flag=1
            return(flag)
        
        except Error as e:
            print("DataBase not Found", e)
            flag=0
            return(flag)
            
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                
        #mydb.close()
    
    print("Database is not Connected")
    


def create_database(hosting,user,pssd,database_name):



    mydb,status=dbconnectcion(hosting,user,pssd)
    
    if status =="Connected" :
    
        try:
           
            
            check_database=checkdb_exist(hosting,user,pssd,database_name)
            
            if not check_database:
                querry="CREATE DATABASE "+ database_name  
                mycursor = mydb.cursor()
                mycursor.execute(querry)
                mycursor.close()
                mydb.close()
                print("Database Created")
                flag=1
                return(flag)
                
                
        except Error as e:
            print("Error while creating Database", e)
            flag=0
            return(flag)
            
           
        
    else:
    
        print("Database is not Connected")


def create_table(hosting,user,pssd,database_name,table_name):
    
    check=create_database(hosting,user,pssd,database_name)
    
    if check:
    
        mydb,flag=dbconnectcion_database(hosting,user,pssd,database_name)
        
        if flag == "Connected":
        
        
        
            querry="CREATE TABLE " + table_name + "(EmpID varchar(255),Date varchar(255),Time varchar(255))"
            
            try:
            
                mycursor = mydb.cursor()
                mycursor.execute(querry)
                flag =1
                mycursor.close()
                mydb.close()
                print("Table Created")
            
            except Error as e:
                print("Error while creating Table", e)
                flag=0
                return(flag)
            
             
        
   
    else :

        print("Error while creating a database Table")    
    



def insert_data_login(hosting,user,pssd,database_name,table_name, Employee_Info):

    EMP_ID,Date,Time=Employee_Info[0],Employee_Info[1],Employee_Info[2]
    
    querry= "INSERT INTO "+table_name+ " (EmpID, Date,Time) VALUES (%s, %s,%s)"
    val=(EMP_ID,Date,Time)
    
    mydb,flag=dbconnectcion_database(hosting,user,pssd,database_name)
        
    if flag == "Connected":
        
        
        
            
            
        try:
            
            mycursor = mydb.cursor()
            mycursor.execute(querry)
            flag =1
            mycursor.close()
            mydb.close()
            print("Inserted")
            
        except Error as e:
            print("Error while Inserting Table", e)
            flag=0
            return(flag)
   
Employee_Info=("1","2","3")
flag=insert_data_login("localhost","root","Ravi99","Employee_attandance_db","attandance",Employee_Info)

print(flag)
#flag=create_table("localhost","root","Ravi99","Employee_attandance_db","attandance")

