"Shutting Down Program Exercise 1"

def shut_down(s):
    if (s == "yes") :
        return "Shutting down"
    elif (s == "no") :
        return "Shutdown aborted"
    else :
        return "Sorry"

check = input("Want to shutdown your computer ?  ")

print(shut_down(check))