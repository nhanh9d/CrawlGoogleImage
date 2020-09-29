# Hướng dẫn sử dụng trước khi dùng :v
Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh (LMAOOOOO)
# Crawl từ google về
## Crawl
1. Mở google image như thế này:
![ảnh](https://github.com/nhanh9d/CrawlGoogleImage/blob/master/1.PNG)
2. Mở Developer tools bằng F12 và chọn tab Console
3. Paste đoạn script trong crawl.js vào và nhấn enter
## Option
1. maxImage: số ảnh tối đa cần lấy
2. interval: khoảng cách mỗi lần lấy ảnh (Nên để 1000 tương đương 1s trở lên)

# Crawl từ file txt đã lưu
## Cài cắm
1. Mở cmd folder git này lên 
2. Chạy pip install -r requirements.txt
## Crawl về folder
1. Tiếp tục với màn cmd thì chạy:
- python crawl.py -t duong-dan-den-file-txt -o duong-dan-den-folder-can-luu-anh
- duong-dan-den-file-txt: Giống như tên :v là đường dẫn đến file nodepad của bạn (Ví dụ: E:\Projects\Python\CrawlGoogleImage\sample.txt)
- duong-dan-den-folder-can-luu-anh: Giống như tên :v là đường dẫn đến folder mà bạn cần lưu (Ví dụ: E:\Projects\Python\CrawlGoogleImage\Data)
