from pip._vendor.distlib.compat import raw_input

a = raw_input();
print(a)
print(type(a))
try:
    a = int(a)
    print(type(a))
    print(a)
except:
    print("No era el numero")
