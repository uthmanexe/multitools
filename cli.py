from tools import qrcoder, websrcape, psswrdgen, ytdwnldr


def main():
    print("===============================================")
    print("          Python Multipurpose Program          ")
    print("===============================================")
    print("Available Tools:")
    print("1. QR Code Generator")
    print("2. Web Scraper")
    print("3. Password Generator")
    print("4. Video Downloader")
    print("5. BMI calculator")
    print("q. Exit")
    print("===============================================")

    case = input("What tool would you like to use?: ").strip()

    if case == "1":
        qrcoder.qrcodify()
    elif case == "2":
        websrcape.scraper()
    elif case == "3":
        psswrdgen.password()
    elif case == "4":
        ytdwnldr.downloader()
    elif case == "5":
        BMI.calculate()
    elif case == "q":
        print("Goodbye!")
    else:
        print("Unknown option selected.")


main()
