import subprocess

def checkYay(user):
    try:
        subprocess.Popen(["sudo", "-u", user, "yay", "-V"])
        return True
    except:
        return False

def getUser():
    proc = subprocess.Popen(["sudo", "sh", "-c", "'echo $SUDO_USER'"], shell=True, stdout=subprocess.PIPE)
    return proc.communicate()

def update():
    command = []

    user = getUser()
    print(user)

    if(checkYay(user)):
        command = ["sudo", "-u", user, "yay"]
    else:
        command = ["sudo", "pacman", "-Syu"]

    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
    print(proc.stdout)