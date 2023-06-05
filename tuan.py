#Ham nhap ten nhan vien:
def insertName():
    name = input("Worker's name: ")
    splittedName = name.split(" ")
    splittedName = [chunk.isalpha() for chunk in splittedName]
    #print(splittedName)
    if not all(splittedName):
        print("\t\tOnly alphabet characters are acceptable\n\t\tPlease re-enter the name!")
        return insertName()
    return name.title()     #chuyen "return name" thanh "return name.title()": Nguyen van A thanh Nguyen Van A

#Ham nhap ID nhan vien:
def insertID():
    try:
        inputId = int(input("\nWorker's ID: "))
    except:
        print("\t\tOnly numeric characters are acceptable\n\t\tPlease re-enter the ID!")
        return insertID()
    return inputId



#Ham nhap ID khong trung ID cu:

#Code cu:dung cho menu 1: nhap thong tin nhan vien

def insertID_unique():
    try:
        inputId = int(input("\nWorker's ID: "))
    except:
        print("\t\tOnly numeric characters are acceptable\n\t\tPlease re-enter the ID!")
        return insertID_unique() #chuyen insertID() sang insertID_unique()
    db = open("db.txt", "r")
    workers = db.readlines()
    workers = [worker.split(", ") for worker in workers]
    idlist = [int(worker[0]) for worker in workers]
    
    if inputId not in idlist:       #Kiem tra neu inputId khong trong idlist (inputId chua ton tai) thi return inputId
        db.close()
        return inputId
    else:
        print("\t\tThis ID already existed!")
        db.close()
        return insertID_unique()


    
    
    
    
#Code moi: Thay doi ham insertID_unique() thanh insertID_unique(workerID): dung cho menu 3: sua thong tin nhan vien
# Sua thong tin nhan vien thi co the thay doi ten ma khong thay doi ID
    
def insertID_unique2(workerID):
    try:
        inputId = int(input("\nWorker's ID: "))
    except:
        print("\t\tOnly numeric characters are acceptable\n\t\tPlease re-enter the ID!")
        return insertID_unique2(workerID) #chuyen insertID() sang insertID_unique2(worker)
    db = open("db.txt", "r")
    workers = db.readlines()
    workers = [worker.split(", ") for worker in workers]
    idlist = [int(worker[0]) for worker in workers]

    if (inputId not in idlist) or (inputId == workerID):    
        db.close()
        return inputId
    else:
        print("\t\tThis ID already existed!")
        db.close()
        return insertID_unique2(workerID)

    
        
    
    
    
    
    
    

#Ham nhap tien luong nhan vien: Muc luong theo cong viec, chuc danh ( chua co khoan tro cap do DK cong viec nang nhoc,...)
def insertSalary():
    try:
        salary = float(input("Worker's salary: "))
    except:
        print("\t\tOnly numeric characters range from 0 to 10 are acceptable\n\t\tPlease re-enter the salary!")
        return insertSalary()
    return salary



#Ham nhap allowances and exemptions: 
def insertAllowances():
    try:
        allowance = float(input("Worker's allowances and exemptions: "))
    except:
        print("\t\tOnly float numbers are acceptable\n\t\tPlease re-enter the allowances and exemptions!")
        return insertAllowances()
    return allowance







#1. Ham thong tin nhan vien va luu vao file: db.txt:
def insertData():
    print("\nINSERT DATA")
    try:
        workerNumber = int(input("Number of workers: "))
    except:
        print("\t\tThe input must be a string containing numeric characters only.")
        return insertData()
    
    
    
    
    
    #Code cu:
    """db = open("db.txt", "a+")
    for i in range(workerNumber):
        workerID = insertID_unique()     #Nhap ID khong trung ID cu
        workerName = insertName()
        workerSalary = insertSalary()
        db.write(f'{workerID}, {workerName}, {workerSalary}\n')
    db.close()"""
    
    
    #Code moi: Nhap 2 nhan vien co ID giong nhau van luu vào file vi ID nhan vien 1 chua luu vào file db.txt nen ham iserID_unique() chua kiem tra
    #Luc nay, 2 nhan vien moi nhap co ID giong nhau luu vào file db.txt 
    #Tao db=open ben trong vong For de nhap Id thong tin nhan vien 1 no luu vao file txt chu khong nhap 2 nhan vien moi luu
        
        
        
    #Dung db=open()
    """for i in range(workerNumber):
        db = open("db.txt", "a+")
        workerID = insertID_unique()  # Nhap ID khong trung ID cu
        workerName = insertName()
        workerSalary = insertSalary()
        db.write(f'{workerID}, {workerName}, {workerSalary}\n')
        db.close()"""
    
    
    #Dung with open():
    for i in range(workerNumber): 
        
        workerID = insertID_unique()
        workerName = insertName()
        workerSalary = insertSalary()
        workerAllowance = insertAllowances() #Nhap tien tro cap DK lao dong, tinh chat phuc tap cua cong viec
        
        with open("db.txt", "a+") as db:    
            db.write(f'{workerID}, {workerName}, {workerSalary}, {workerAllowance}\n')
    
    
    
    

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
            print("\t\tThere is no worker matched with your query.\n\t\tPlease re-enter the ID!")  #Neu nhap khong dung ID thi quay lai nhap lai ID
            db.close()
            return deleteData()
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
        if int(processedData[0]) == workerID and processedData[1].lower() == workerName.lower(): #moi nhan vien co 1 ID rieng
                                                #Neu nhap ten nhan vien "Hoang van A" ma trong danh sach ten "Hoang Van A" thi van cho sua ten
                                                #Ten khong phan biet chu hoa khi nhap ID va ten nhan vien can sua
            print("\nNew information:") 
            #Co dong ngan giuwa thong tin cu va thong tin moi cua nhan vien vi su dung chung insert ID() va insertName()
            
            
            
            
            modifiedID = insertID_unique2(workerID) #Thay insertId thanh insertID_unique() thanh insertID_unique(workerID)
            #Sua thong tin nhan vien: co the thay doi ten mà khong thay doi ID nhan vien
            
            
            
            
            
            modifiedName = insertName()
            modifiedSalary = insertSalary()
            
            modifiedAllowance = insertAllowances()
            
            lines[line] = f'{modifiedID}, {modifiedName}, {modifiedSalary}, {modifiedAllowance}'
            db.close()
            db = open("db.txt", "w")
            for line in lines:
                db.write(line + "\n")
            break
        if line == len(lines) - 1:
            print("\t\tThere is no worker matched with your query.\n\t\tPlease re-enter the name and ID!") #Khong co nhan vien nào phu hop voi truy van cua ban
            return modifyData()
    db.close()    

#Thay doi ten nhan vien, k thay doi ID nhan vien:  Neu dung insertID_unique() thi ID cu cua nhan vien da luu trong file db.txt nen k dung lai ID ma phai nhap ID moi=====>>LOiiiii   
    
    
    
#4. In tien luong thuc te cua moi nhan vien:    
def salaryExport():
    db = open("db.txt", "r")
    print("\nGET SALARY VIA ID")
    workerID = insertID()
    workers = [line[:-1] for line in db.readlines()] #line[:-1]: lay tu dau den gia tri cuoi cung
    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            salary= float(data[2]) + float(data[3])
            actualsalary= salary * 0.92   #luong sau dong bao hiem xa hoi
            print("\nSalary of employee with name: "+data[1]+" and ID: "+str(workerID)+" is: "+ str("{:.2f}".format(salary))+ " (VND)")
            print("Actual Salary of employee with name: "+data[1]+" and ID: "+str(workerID)+" is: "+str("{:.2f}".format(actualsalary))+" (VND)")
            break
        if worker == len(workers) - 1:
            print("\t\tWrong ID input. Please re-enter the ID!")
            
            return salaryExport() # Neu "wrong ID" thi yeu cau nhap lai ID
        
    db.close()
#Tien luong dong bao hiem XH: muc luong theo cong viec, chuc danh + phu cap luong bu dap yeu to ve Dk lao dong, tinh chat phuc tap cong viec, DK sinh hoat, muc do thu hut lao dong + khoan bo sung xac dinh cu the duoc tra thuong xuyen trong tra luong    
    
    
    
    
    
    
    
#5 6. In tien bao hiem XH nhan vien phai dong hay cong ty dong cho moi nhan vien tuong ung voi luong thang cua moi nhan vien:    

#Code cu: return (float(data[2])+float(data[3]))*rate

"""def printInsuranceFee(rate):
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
            return (( float(data[2]) + float(data[3]) ) * rate)
        
            break
        if worker == len(workers) - 1:
            print("\t\tWrong ID input. Please re-enter the ID!")
            return printInsuranceFee(rate)     #Neu "wrong ID input" thi quay lai nhap lai ID
            
    db.close()  """  

    

#Code moi: return data[1], workerID, (float(data[2])+float(data[3])) *rate

def printInsuranceFee(rate):
    db = open("db.txt", "r")
    print("\nSOCIAL INSURANCE")
    workerID = insertID() #Nhap ID nhan vien can in bao hiem XH
    workers = [line[:-1] for line in db.readlines()]   #workers: list ca 1 dong line trong f.readlines():
#VD: wokers for line[0]: workers=["100, Trang,11.000"]

    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            return data[1], workerID, (( float(data[2]) + float(data[3]) ) * rate)
        
        if worker == len(workers) - 1:
            print("\t\tWrong ID input. Please re-enter the ID!")
            return printInsuranceFee(rate)     #Neu "wrong ID input" thi quay lai nhap lai ID

    db.close()
    
    
    
#7. In Tong tien bao hiem cong ty phai dong cho Bao hiem XH VN:    
def totalInsuranceFee():
    
    print("\nTOTAL INSURANCE: ")
    
    db = open("db.txt", "r")
    lines = db.readlines()
    lines = [line[:-1] for line in lines]
   
    sumSalary=0
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        sumSalary=sumSalary + float(processedData[2]) + float(processedData[3])
    
    totalFee=sumSalary*0.175+sumSalary*0.08 #Tong tien bao hiem =tien bao hiem cua nhan vien+ tien bao hiem cong ty dong cho nhan vien
    db.close()
    return totalFee
    





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
        functionID = int(input("\n\t\tEnter a function ID: "))
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
        pay1 = printInsuranceFee(0.08)
        print(f"The amount of Social Insurance the employee with name: {pay1[0]} and ID: {pay1[1]} has to pay: {pay1[2]:.2f} (VND)")

        #printInsuranceFee(0.08)
        
    elif functionID == 6:
        pay2 = printInsuranceFee(0.175)
        print(f"The amount of Social Insurance the company must to pay the employee with name: {pay2[0]} and ID: {pay2[1]} is: {pay2[2]:.2f} (VND)")    
        
        #printInsuranceFee(0.175)
        
    elif functionID == 7:
        print("Total Social Insurance the company must pay to Social Insurance Vietnam: %.2f (VND)" % totalInsuranceFee())
    else:
        print("\n\t\tSyntax error. Please re-enter !")
