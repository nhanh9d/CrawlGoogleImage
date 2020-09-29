import requests
import os
import argparse

#thêm tham số nhận vào khi chạy command
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--txt", required=True,
	help="Duong dan den file txt")
ap.add_argument("-o", "--output", required=True,
	help="Duong dan den folder luu anh")
args = vars(ap.parse_args())

#tổng số ảnh
total = 0

#load file txt
f = open(args["txt"], "r")

#lưu thành list string url
urls = f.read().strip().split('\n')

#loop
for url in urls:
    try:
        #request lấy ảnh
        r = requests.get(url)

        #lấy được ảnh
        if(r.status_code == 200):
            #nối chuỗi file ảnh dạnh 00000001.jpg
            p = os.path.sep.join([args["output"], "{}.jpg".format(str(total).zfill(8))])
            #mở file ảnh
            image = open(p, "wb")
            #viết ảnh vào
            image.write(r.content)
            #đóng việc mở ảnh
            image.close()
            #tăng tổng số ảnh lên 1
            total += 1
            #thông báo
            print("[INFO] downloaded: {}".format(p))
    #xử lý trường hợp không load đc ảnh
    except:
        print("[INFO] downloaded: {}".format(p))
print("[INFO] done. Total images: {}".format(total))
