def insertName():
    name = input("Worker's name:")
    splittedName = name.split(" ")
    splittedName = [chunk.isalpha() for chunk in splittedName]
    #print(splittedName)
    if not all(splittedName):
        print("\t\tOnly alphabet characters are acceptable\n\t\tPlease re-enter the name!")
        return insertName()
    return name

#Ham nhap ID nhan vien:
def insertID():
    try:
        inputId = int(input("\nWorker's ID: "))
    except:
        print("\t\tOnly numeric characters are acceptable\n\t\tPlease re-enter the ID!")
        return insertID()
    return inputId
#Nhap ten ID khong trug ID da ton tai
#Try-except-else: else: thuc thi khi chuong trinh khong co loi

def insertID_unique():
    try:
        inputId = int(input("\nWorker's ID: "))
    except:
        print("\t\tOnly numeric characters are acceptable\n\t\tPlease re-enter the ID!")
        return insertID()
    db = open("db.txt", "r")
    workers = db.readlines()
    workers = [worker.split(", ") for worker in workers]
    idlist = [int(worker[0]) for worker in workers]
    if inputId not in idlist:
        db.close()
        return inputId
    else:
        print("This ID already existed")
        db.close()
        return insertID_unique()



#Ham nhap tien luong nhan vien:
def insertSalary():
    try:
        salary = float(input("Worker's salary: "))
    except:
        print("\t\tOnly numeric characters range from 0 to 10 are acceptable\n\t\tPlease re-enter the salary!")
        return insertSalary()
    return salary

#1. Ham thong tin nhan vien va luu vao file: db.txt:
def insertData():
    print("\nINSERT DATA")
    try:
        workerNumber = int(input("Number of workers: "))
    except:
        print("The input must be a string containing numeric characters only.")
        return insertData()
    db = open("db.txt", "r+")
    for i in range(workerNumber):
        workerID = insertID_unique()
        workerName = insertName()
        workerSalary = insertSalary()
        db.write(f'{workerID}, {workerName}, {workerSalary}\n')
    db.close()
    
    

#2. Xoa thong tin nhan vien: 
def deleteData():
    print("\nREMOVE SELECTION DATA")
    print("Input ID employee to delete: ")
    workerID = insertID()   #Id nhan vien can xoa
    db = open("db.txt", "r")
    lines = db.readlines()
    
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        #print(processedData)
        if int(processedData[0]) == workerID:
            lines.pop(line)
            break
        if line == len(lines) - 1:
            print("There is no worker matched with your query.")
            db.close()
            return False
    db.close()
    db = open("db.txt", "w+")
    for line in lines:
        db.write(line)
    db.close()

#3. Sua thong tin nhan vien: 
def modifyData():
    print("\nMODIFY WORKER'S DATA")
    db = open("db.txt", "r")
    lines = db.readlines()
    lines = [line[:-1] for line in lines]
    
    
    
    
    print("Input ID and name of employee to corect information:")
    
    
    
    
    workerID = insertID()
    workerName = insertName()
    
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        if int(processedData[0]) == workerID and processedData[1] == workerName: #moi nhan vien co 1 ID rieng
            print("\nNew information:") 
            #Co dong ngan giuwa thong tin cu va thong tin moi cua nhan vien vi su dung chung insert ID() va insertName()
            modifiedID = insertID()
            modifiedName = insertName()
            modifiedSalary = insertSalary()
            
            lines[line] = f'{modifiedID}, {modifiedName}, {modifiedSalary}'
            db.close()
            db = open("db.txt", "w")
            for line in lines:
                db.write(line + "\n")
            break
        if line == len(lines) - 1:
            print("There is no worker matched with your query") #Khong co nhan vien nào phu hop voi truy van cua ban
            return modifyData()
    db.close()    

def salaryExport():
    db = open("db.txt", "r")
    print("\nGET SALARY VIA ID")
    workerID = insertID()
    workers = [line[:-1] for line in db.readlines()] #line[:-1]: lay tu dau den gia tri cuoi cung
    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            print("Salary of employee with ID: "+str(workerID)+" is: "+ data[2])
            break
        if worker == len(workers) - 1:
            print("Wrong ID input")
            
            
            
            
            return salaryExport() # Neu "wrong ID" thi yeu cau nhap lai ID
        
        
        
    db.close()
    
#5 6. In tien bao hiem XH nhan vien phai dong hay cong ty dong cho moi nhan vien tuong ung voi luong thang cua moi nhan vien:    
def printInsuranceFee(rate):
    db = open("db.txt", "r")
    print("\nSOCIAL INSURANCE")
    workerID = insertID() #Nhap ID nhan vien can in bao hiem XH
    workers = [line[:-1] for line in db.readlines()]   #workers: list ca 1 dong line trong f.readlines():
#VD: wokers for line[0]: workers=["100, Trang,11.000"]

    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            
            
            
            #print(float(data[2]) * rate)
#Sua "print" sang return: khi goi ham 5 hoa 6 se co print("The amount of Social Insurance the company must to pay: ", printInsuranceFee(rate))
            return (float(data[2]) * rate)
        
        
        
        
        
            break
        if worker == len(workers) - 1:
            print("Wrong ID input")
            return printInsuranceFee(rate)
            
    db.close()    

    
#7. In Tong tien bao hiem cong ty phai dong cho Bao hiem XH VN:    
def totalInsuranceFee():
    
    print("\nTotal Insurance: ")
    
    db = open("db.txt", "r")
    lines = db.readlines()
    lines = [line[:-1] for line in lines]
   
    sumSalary=0
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        sumSalary=sumSalary+float(processedData[2])
    
    totalFee=sumSalary*0.175
    return totalFee
    #print("Total Social Insurance the company must pay: ", totalFee())
    
    db.close()    





while True:
    print(f'''\n
    0. Exit the program
    1. Input employee information
    2. Delete employee information
    3. Edit employee information
    4. Print employee'salary
    5. Print the amount of Social Insurance that the employee has to pay
    6. Print the amount of Social Insurance the company must pay for each employee
    7. Print Total amount of Social Insurance the company must pay to Social Insurance Vietnam
    ''')
    
    try:
        functionID = int(input("\nEnter a function ID: "))
    except:
        print("You must enter a number. Please reenter!")
        continue
    
    if functionID == 0:
        break
        
    elif functionID == 1:
        insertData()
        
    elif functionID == 2:
        deleteData()
        
    elif functionID == 3:
        modifyData()
        
    elif functionID == 4:
        salaryExport()
        
    elif functionID == 5:
        print("The amount of Social Insurance that the employee has to pay: ", printInsuranceFee(0.08))
        #printInsuranceFee(0.08)
        
    elif functionID == 6:
        print("The amount of Social Insurance the company must pay for each employee: ", printInsuranceFee(0.175))
        #printInsuranceFee(0.175)
        
    elif functionID == 7:
        print("Total Social Insurance the company must pay: ", totalInsuranceFee())
    else:
        print("Syntax error. Please reenter !")
