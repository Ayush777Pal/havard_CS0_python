n=input("File name: ")
b,i=n.split(".")
#i=b[-1].lower().strip()
match i:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "txt":
        print("image/txt")
    case "zip":
        print("image/zip")
    case _ :
        print("application/octet-stream")
        


