import subprocess
import csv


def click(tap_x, tap_y):
    adb("adb shell input tap {} {}".format(tap_x, tap_y))


def adb(command):
    proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    return out.decode('utf-8')


def send_msg(phone, message):
    adb(f'adb shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone={phone}"')
    adb('ping 127.0.0.1 -n 2 > nul')
    adb(f'adb shell input text "{message}"')
    adb(f'adb shell input keyevent 22 adb shell input keyevent 22  adb shell input keyevent 66')
    print(f'Message sent to {phone}')


def send_img(whatsapp_name, img_name, img_path,name):
    adb(f"adb push {img_path}\{img_name} /sdcard/")
    adb(f"adb shell am start -a android.intent.action.SEND -t  text/plain -e jid '+919566341405@s.whatsapp.net' --eu android.intent.extra.STREAM file:///storage/emulated/0/{img_name}  -p com.whatsapp")
    adb('ping 127.0.0.1 -n 1 > nul')
    click(1003, 129)
    adb(f'adb shell input text "{whatsapp_name}"')
    adb('ping 127.0.0.1 -n 1 > nul')
    click(309, 398)
    adb('ping 127.0.0.1 -n 1 > nul')
    click(953, 1281)
    adb('ping 127.0.0.1 -n 2 > nul')
    click(456, 2127)
    adb('ping 127.0.0.1 -n 1 > nul')
    adb(f'adb shell input text "Congratulations *{name}*!!!.All the best for your Future Goals"')
    adb('ping 127.0.0.1 -n 1 > nul')
    adb(f"adb shell input keyevent 61 adb shell input keyevent 61 adb shell input keyevent 66")
    adb('ping 127.0.0.1 -n 1 > nul')
    print(f"sent to {name}")

# driver code
d = {}
with open('Data.csv', mode='r') as inp:
    reader = csv.reader(inp)
    a = True
    for i in reader:
        if a is True:
            header = i
            header[0] = header[0].replace("ï»¿", '')
        else:
            i[5] = i[5].replace('"', "")
            d[i[1]] = {header[2]: i[2], header[3]: i[3], header[4]: i[4], header[5]: i[5]}
        a = False

for i in d:
    name = d[i]['Student-Name']
    whatsapp_name = d[i]['Whatsapp-Name']
    whatsapp_number = d[i]['Whatsapp-Number']
    message = f"Hello {name}"
    img_name = d[i]['Certificate-ID']
    img_path = 'C:\\Users\\visha\\Documents\\PPP\\Demo-Certificates'
    # send_img(whatsapp_name, img_name, img_path,name)
    send_msg(whatsapp_number,message)