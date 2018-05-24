
def StartScanner(strOct1,strOct2,strOct3):
    try:
        import urlfetch

        i = 0
        j = 0
        while i <= 255:
            ip =  str(strOct1) + "." + str(strOct2) + "." + str(strOct3) + "." +  str(i)
            try:
                result = urlfetch.get(ip)
                print("IP [+] " + ip + result.status)
            except:
                print("Error")


            i = i + 1

        return True
    except:
        return False


if __name__ == "__main__":
    for i in range(255):
        StartScanner(strOct1=196, strOct2=2, strOct3=i)



