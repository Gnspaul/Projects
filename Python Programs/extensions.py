fileName = input("File name: ")
fileName.strip()

extension = fileName[-3:]
match extension:
    case  "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "peg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("document/pdf")
    case "txt":
        print("document/txt")
    case "zip":
        print("folder/zip")
    case "":
        print("application/octet-stream")
    case _:
        print("You need to enter a valid file with a valid type")