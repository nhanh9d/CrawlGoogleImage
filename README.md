# Hướng dẫn sử dụng trước khi dùng :v

# crawl từ google về
## Crawl
1. Mở google image như thế này:
![ảnh](https://github.com/nhanh9d/CrawlGoogleImage/blob/master/1.PNG)
2. Mở Developer tools bằng F12 và chọn tab Console
3. Paste đoạn script trong crawl.js vào và nhấn enter
## Option
1. maxImage: số ảnh tối đa cần lấy
2. interval: khoảng cách mỗi lần lấy ảnh (Nên để 1000 tương đương 1s trở lên)

# crawl từ file txt đã lưu
## cài cắm
1. Mở cmd folder git này lên 
2. Chạy pip install -r requirements.txt
## crawl về folder
1. Tiếp tục với màn cmd thì chạy:
   python crawl.py -t duong-dan-den-file-txt -o duong-dan-den-folder-can-luu-anh
