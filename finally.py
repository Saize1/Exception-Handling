try:
    i=int(input("Enter a no."))
    c=1/i
 

except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Think Future Technologies")