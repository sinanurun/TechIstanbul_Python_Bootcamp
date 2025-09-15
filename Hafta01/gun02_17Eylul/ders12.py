gun = int(input("haftanın kaçıncı günündeyiz"))
match gun:
    case 1:
        print("pazartesi")
    case 2:
        print("salı")
    case 3:
        print("çarşamba")
    case 4:
        print("perşembe")
    case 5:
        print("cuma")
    case 6:
        print("ctesi")
    case 7:
        print("pazar")
    case _ :
        print("hatalı")