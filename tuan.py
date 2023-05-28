def insertName():
    name = input("Worker's name:")
    splittedName = name.split(" ")
    splittedName = [chunk.isalpha() for chunk in splittedName]
    print(splittedName)
    if not all(splittedName):
        print("Only alphabet characters are acceptable\nPlease re-enter the name")
        return insertName()
    return name

def insertID():
    try:
        inputId = int(input("Worker's ID:"))
    except:
        print("Only numeric characters are acceptable\nPlease re-enter the ID")
        return insertID()
    return inputId

def insertSalary():
    try:
        salary = float(input("Worker's salary:"))
    except:
        print("Only numeric characters range from 0 to 10 are acceptable\nPlease re-enter the salary")
        return insertSalary()
    return salary

def insertData():
    print("INSERT DATA")
    try:
        workerNumber = int(input("Number of workers:"))
    except:
        print("The input must be a string containing numeric characters only.")
        return insertData()
    db = open("db.txt", "a+")
    for i in range(workerNumber):
        workerID = insertID()
        workerName = insertName()
        workerSalary = insertSalary()
        db.write(f'{workerID}, {workerName}, {workerSalary}\n')
    db.close()

def deleteData():
    print("REMOVE SELECTION DATA")
    workerID = insertID()
    db = open("db.txt", "r")
    lines = db.readlines()
    
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        print(processedData)
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

def modifyData():
    print("MODIFY WORKER'S DATA")
    db = open("db.txt", "r")
    lines = db.readlines()
    lines = [line[:-1] for line in lines]
    workerID = insertID()
    workerName = insertName()
    
    for line in range(len(lines)):
        processedData = lines[line].split(", ")
        if int(processedData[0]) == workerID and processedData[1] == workerName:
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
            print("There is no worker matched with your query")
    db.close()

def salaryExport():
    db = open("db.txt", "r")
    print("GET SALARY VIA ID")
    workerID = insertID()
    workers = [line[:-1] for line in db.readlines()]
    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            print(data[2])
            break
        if worker == len(workers) - 1:
            print("Wrong ID input")
    db.close()

def printInsuranceFee(rate):
    db = open("db.txt", "r")
    print("Personal Insurance")
    workerID = insertID()
    workers = [line[:-1] for line in db.readlines()]
    for worker in range(len(workers)):
        data = workers[worker].split(", ")
        if int(data[0]) == workerID:
            print(float(data[2]) * rate)
            break
        if worker == len(workers) - 1:
            print("Wrong ID input")
    db.close()

# App running from here
running = True
while(running):
    try:
        functionID = int(input("Enter a function ID:"))
    except:
        print("You must enter a number")
        continue
    if functionID == 0:
        running = False
    elif functionID == 1:
        insertData()
    elif functionID == 2:
        deleteData()
    elif functionID == 3:
        modifyData()
    elif functionID == 4:
        salaryExport()
    elif functionID == 5:
        printInsuranceFee(0.08)
    elif functionID == 6:
        printInsuranceFee(0.175)
    elif functionID == 7:
        pass
        # Lam not cai so 7 nhe
