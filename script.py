import os
import calendar
from cryptography.fernet import Fernet
from datetime import datetime
import time

PATH = "./files"
LOGO = '''
        ________                ____.                                 .__   
        \______ \ _____        |    | ____  __ _________  ____ _____  |  |  
        |    |  \\__  \       |    |/  _ \|  |  \_  __ \/    \\__  \ |  |  
        |    `   \/ __ \_ /\__|    (  <_> )  |  /|  | \/   |  \/ __ \|  |__
        /_______  (____  / \________|\____/|____/ |__|  |___|  (____  /____/
                \/     \/                                    \/     \/      
'''

def printAndClearTerminal(text):
    print(text)
    time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')

def checkAndCreateFolder():
    if not os.path.exists(PATH):
        os.makedirs(PATH)

def fileExists(fileName):
    return os.path.isfile(PATH+"/"+fileName+".txt")

def get_days_in_month(year, month):
    days = []
    c = calendar.monthcalendar(year, month)
    for week in c:
        for day in week:
            if day != 0:
                days.append(datetime(year, month, day).strftime("%d-%m-%Y"))
    return days

def createFilesForTheMonth():
    checkAndCreateFolder()
    now = datetime.now()
    daysArray = get_days_in_month(now.year,now.month)
    for day in daysArray:
        if fileExists(day):
            continue
        file = open(PATH+"/"+day+".md", "w")
        file.write(f'# Diary {day}\n\n')
        file.close()

def encrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_name, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file_name,key):
    with open(file_name, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as f:
        f.write(decrypted_data)

def encryptFiles():
    key = Fernet.generate_key()
    try:
        totalFiles = len(os.listdir(PATH))
    except Exception as e:
        print(f'There is no folder named files in the root folder that contains the files to be encrypted !')
        return
    for index, file in enumerate(os.listdir(PATH)):
        if file.endswith(".md"):
            printAndClearTerminal(f'Encrypting {index+1}/{totalFiles}')
            encrypt_file(PATH+"/"+file,key)
    with open("./key.key", "w") as f:
        f.write(key.decode(encoding='UTF-8'))
    print('Key saved in key.key file in the root folder !')

def decryptFiles():
    try:
        with open("./key.key", "r") as f:
            key = f.read()
        try:
            totalFiles = len(os.listdir(PATH))
        except Exception as e:
            print(f'There is no folder named files in the root folder that contains the files to be decrypted !')
            return
        for index, file in enumerate(os.listdir(PATH)):
            if file.endswith(".md"):
                printAndClearTerminal(f'Decrypting {index+1}/{totalFiles}')
                decrypt_file(PATH+"/"+file,key)
        print('Files decrypted successfully!')
    except Exception as e:
        if f'{e}'.__contains__(' No such file or directory: '):
            print('Key file not found !, please create a key file with the name key.key in the root folder !')
        else:
            print(f'{e}')

if __name__ == "__main__":
    print(f'''        
        {LOGO}
        1. Create files for the month
        2. Encrypt files
        3. Decrypt files
    ''')
    option = input('Enter your option \n')
    if option == '1':
        createFilesForTheMonth()
    elif option == '2':
        encryptFiles()
    elif option == '3':
        decryptFiles()
    else:
        print('Wrong input !')