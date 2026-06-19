
print("1. Current date/time\n"
      "2. Users logged in\n"
      "3. Current directory path\n"
      "4. See 'Hello World'\n"
      "5. Check the top processes running\n"
      "6. Check internet connectivity\n"
      "7. Exit")
import subprocess
def command(cmd):
    result = subprocess.run(cmd)


a = input("Hello, what would you like to know? ")
if a == "1":
    import subprocess
    subprocess.run(["date"])
elif a == "2":
    import subprocess
    subprocess.run(["users"])

elif a == "3":
    import subprocess
    subprocess.run(["pwd"])
elif a == "7":
   print("Exiting...")

elif a == "4":
    print("Hello World")
elif a == "5":
    command(["htop"])
elif a == "6":
    command(["ping", "-c", "4", "8.8.8.8"])
