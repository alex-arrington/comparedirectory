import os
import time

def pwdcalc(src,dir):           #function adds files to a directory
    for file in os.listdir(src):
        dir.append(os.path.basename(file))

def comparetool(firdir,secdir,predir):     #finds files not present in dir2 and vice versa
    for j in range(len(firdir)):
        if firdir[j] not in secdir:
            predir.append(firdir[j])

def singleprint(prntdir):
    for i in range(len(prntdir)):
        print(f'{i+1} - {prntdir[i]}')

def printmenu(p1,p2):
    print(f'\nPrint Menu\n')
    print(f'1 - Files present in "{p1}" that are not in "{p2}"')
    print(f'2 - Files present in "{p2}" that are not in "{p1}"')
    print(f'3 - Print both')
    print(f"q - quit")

#directory lists set
dir1 = [] 
dir2 = []
predir1 = []
predir2 = []


#path's inputs
path1 = str(input('\nInput the first directory:\n'))
path2 = str(input('\nInput the secondary directory:\n'))

pwdcalc(path1,dir1)
pwdcalc(path2,dir2)

comparetool(dir1,dir2,predir1)
comparetool(dir2,dir1,predir2)

len1 = len(predir1)
len2 = len(predir2)


while (1):
    printmenu(path1,path2)
    menuinput = str(input("\nEnter an option from the Menu:\n"))

    if menuinput == '1':
        if len1 == 0:
            print(f'\n0 files present in "{path1}" that are not in "{path2}"\n')
            time.sleep(3)
        else:
            print(f'\nFiles present in "{path1}" that are not in "{path2}":\n')
            time.sleep(2)
            singleprint(predir1)
            time.sleep(3)
    
    elif menuinput == '2':
        if len2 == 0:
            print(f'\nNo files present in "{path2}" that are not in "{path1}"\n')
            time.sleep(3)
        else:
            print(f'\nFiles present in "{path2}" that are not in "{path1}":\n')
            time.sleep(2)
            singleprint(predir2)
            time.sleep(3)

    elif menuinput == '3':
        if len1 == 0:
            print(f'\n0 files present in "{path1}" that are not in "{path2}"...\n')
            time.sleep(5)
        else:
            print(f'\nFiles present in "{path1}" that are not in "{path2}":\n')
            time.sleep(2)
            singleprint(predir1)
            time.sleep(3)
        if len2 == 0:
            print(f'\n0 files present in "{path2}" that are not in "{path1}"...\n')
            time.sleep(5)
        else:
            print(f'\nFiles present in "{path2}" that are not in "{path1}":\n')
            time.sleep(2)
            singleprint(predir2)
            time.sleep(3)

    elif menuinput == 'q':
        print(f"\nThanks for using Alex's Data Loss Prevention Tool!!\n")
        time.sleep(5)
        break

    else:
        print(f'Menu input error.')
        time.sleep(1)
        