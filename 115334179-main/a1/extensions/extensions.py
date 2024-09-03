myInput = input("File name: ").lower().rstrip()

if myInput.endswith(".gif"):
    print("image/gif")
elif myInput.endswith(".jpg") or myInput.endswith(".jpeg"):
    print("image/jpeg")
elif myInput.endswith(".png"):
    print("image/png")
elif myInput.endswith(".pdf"):
    print("application/pdf")
elif myInput.endswith(".txt"):
    print("text/plain")
elif myInput.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
