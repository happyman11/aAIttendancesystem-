import mysql.connector
from mysql.connector import Error

def dbconnectcion_database(database_name):
    try:
    
        mydb = mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="Ravi99",
                                       database=database_name,
                                       )
        
        flag=1
        return(mydb,flag)
        
    except Error as e:
        flag=0
        mydb=0
        print("Error while connecting to MySQL", e)
        return(mydb,flag) 

def dbconnectcion():
    try:
    
        mydb = mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="Ravi99"
                                       )
        flag=1
        return(mydb,flag)
        
    except Error as e:
        flag=0
        mydb=0
        print("Error while connecting to MySQL", e)
        return( mydb,flag)           

def create_database(database_name):



    mydb,check=dbconnectcion()
    
    if check:
    
        try:
            #querry="CREATE DATABASE "+ database_name  
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE {}".format(database_name ))
            flag=1
            return(flag)
        except Error as e:
            print("Error while creating Database", e)
            flag=0
            return(flag)   

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()            
        
    else: 

        print("Cannot Connected to Database")    
    
    
def create_table(database_name,table_name):
    
   
    
    mydb,check=dbconnectcion_database(database_name)
        
    if check == 1:
        
        
        
        #querry="CREATE TABLE " + table_name + "(EmpID varchar(255),Date varchar(255),Time varchar(255))"
            
        try:
            
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE {} (EmpID varchar(255),Date varchar(255),Time varchar(255))".format(table_name))
            flag =1
            print("Table Created Sucessfully")
            return(flag) 
            
        except Error as e:
        
            print("Error while creating Table", e)
            flag=0
            return(flag)
            
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()  
        
   
    else :

        print("Error while database connection")    
    
def check_existtable(database_name, table_name):

    mydb,flag=dbconnectcion_database(database_name)
        
    if flag == 1:
        
        try:
            
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {}".format(table_name))
            flag =1
            return(flag) 
        
        except Error as e:
        
            print("Error while Checkin Existing Table", e)
            flag=0
            return(flag)
            
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()  
    else :

        print("Error while database connection") 


def insert_data_login(database_name,table_name, Employee_Info):

    mydb,check=dbconnectcion_database(database_name)
        
    if check == 1:
    
        try:
            EMP_ID,Date,Time=Employee_Info[0],Employee_Info[1],Employee_Info[2]
    
            querry= "INSERT INTO {} (EmpID, Date,Time) VALUES (%s, %s,%s)".format(table_name)
            val=(EMP_ID,Date,Time)
            mycursor = mydb.cursor()
            mycursor.execute(querry,val)
            mydb.commit()
            flag =1
            print("Data Logged")
            return(flag)
            
        except Error as e:
            print("Error while Inserting Table", e)
            flag=0
            return(flag)
            
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()      
    else :

        print("Error while database connection") 

def database_wrapper(Id,date,time):
  
  database_name="Ravi123111222"
  table_name="Attandance_Logging"
  Employee_Info=(Id,date,time)
  
  
  mydb,check_dbconn=dbconnectcion_database(database_name)
  print(check_dbconn)
  if check_dbconn == 0:
      #create dbconnectcion
        
        check=create_database(database_name)
        if check:
            print("Database Created")
            
            check_table=create_table(database_name,table_name)
            
            if check_table:
            
                print("Table Created")
                check_insert=insert_data_login(database_name,table_name, Employee_Info)
                
                if check_insert:
                
                
                   print("Data Inserted")
                   #return 1
                else: 
                
                    print("Data Insertion Failed")
                    #return 0
            else:
                print("Table not Created")           
            #create table
          
        else:

            print("Database did not created")        
                    
  else:
  
        check_table= check_existtable(database_name,table_name)
        
        if check_table==1:
        
            print("Table Exist")
            
            check_insert=insert_data_login(database_name,table_name, Employee_Info)
                
            if check_insert:
                
                
                print("Data Inserted")
                   #return 1
            else: 
                
                print("Data Insertion Failed")
                    #return 0
            
        else:
        
            check_table=create_table(database_name,table_name)
            
            if check_table:
            
                print("Table Created")
                
                check_insert=insert_data_login(database_name,table_name, Employee_Info)
                
                if check_insert:
                
                
                   print("Data Inserted")
                   #return 1
                else: 
                
                    print("Data Insertion Failed")
                    #return 0
                
            else:
                print("Table not Created") 
        
        

  

      

   