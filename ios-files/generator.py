import os
dirStr = os.getcwd() + "/ios-files/"
bg = dirStr + "before-vc.md"
ios = dirStr + "ios.md"
af = dirStr + "after-vc.md"
iosFile = open(ios, "w")


print("generating beginning doc...")
beforeFile = open(bg, "r")
iosFile.write(beforeFile.read())
iosFile.close()
beforeFile.close


print("generating vc ...")
iosFile = open(ios, "a")
iosFile.write("\n\n")
for filename in os.listdir(dirStr + "view-controllers"):
  with open(os.path.join(dirStr, "view-controllers", filename), "r") as vc:
    iosFile.write(vc.read())
    iosFile.write("\n\n")
    vc.close
iosFile.close
print("generating after vc ...")
iosFile = open(ios, "a")
afterFile = open(af, "r")
iosFile.write(afterFile.read())
iosFile.close
afterFile.close()