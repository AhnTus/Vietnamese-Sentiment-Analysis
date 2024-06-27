-- Tạo cơ sở dữ liệu SalesPhone
CREATE DATABASE SalesPhone;
GO

-- Sử dụng cơ sở dữ liệu SalesPhone
USE SalesPhone;
GO

-- Tạo bảng users
CREATE TABLE users (
    id INT IDENTITY PRIMARY KEY,
    username VARCHAR(255) unique,
    full_name NVARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
GO

-- Tạo bảng phone
CREATE TABLE phone (
    id INT IDENTITY PRIMARY KEY,
    phone_name NVARCHAR(MAX),
    specifications NVARCHAR(MAX),
	photo NVARCHAR(MAX)
);
GO

-- Tạo bảng comment
CREATE TABLE comment (
    id INT IDENTITY PRIMARY KEY,
    user_id INT,
    comment NVARCHAR(MAX),
    predict NVARCHAR(MAX)
    FOREIGN KEY (user_id) REFERENCES users(id)
);
GO

-- Tạo bảng comment_phone
CREATE TABLE comment_phone (
    id_phone INT NOT NULL, 
    id_comment INT NOT NULL,
    PRIMARY KEY (id_phone, id_comment),
    FOREIGN KEY (id_phone) REFERENCES phone(id),
    FOREIGN KEY (id_comment) REFERENCES comment(id)
);
GO
INSERT INTO users (username, full_name, password) VALUES
('user1', N'Nguyễn Văn A', '123'),
('user2', N'Trần Thị B', '123'),
('user3', N'Lê Văn C', '123'),
('user4', N'Phạm Thị D', '123');
GO
INSERT INTO phone (phone_name, specifications, photo) VALUES
(N'iPhone 12', '[12MP, 4GB, 64GB, 2815mAh, Iphone(Apple)]', 'https://cdn.tgdd.vn/Products/Images/42/213031/iphone-12-trang-13-600x600.jpg'),
(N'iPhone 12 Pro', '[12MP, 6GB, 128GB, 2815mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2020/10/thumb_IP12Pro_3.jpg'),
(N'iPhone 12 Pro Max', '[12MP, 6GB, 128GB, 3687mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2020/10/thumb_IP12Pro_3.jpg'), 
(N'iPhone 13', '[12MP, 4GB, 128GB, 3240mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/x/media/catalog/product/1/5/15_2_8_1.jpg'),
(N'iPhone 13 Pro', '[12MP, 6GB, 128GB, 3095mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/4/_/4_36_3_2_1_5.jpg'),
(N'iPhone 13 Pro Max', '[12MP, 6GB, 128GB, 4352mAh, Iphone(Apple)]', 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/4/_/4_36_3_2_1_9.jpg'),
(N'iPhone 14', '[12MP, 6GB, 128GB, 3279mAh, Iphone(Apple)]', 'https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/2222.png'),
(N'iPhone 14 Pro', '[48MP, 6GB, 128GB, 3200mAh, Iphone(Apple)]', 'https://clickbuy.com.vn/uploads/images/2023/10/4.jpg'),
(N'iPhone 14 Pro Max', '[48MP, 6GB, 512GB, 4323mAh, Iphone(Apple)]','https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-tim-thumb-600x600.jpg'),
(N'Samsung Galaxy S21', '[12MP, 8GB, 128GB, 4000mAh, Samsung]', 'https://cdn.tgdd.vn/Products/Images/42/220833/samsung-galaxy-s21-tim-600x600.jpg'),
(N'Samsung Galaxy S21 Ultra', '[108MP, 12GB, 128GB, 5000mAh, Samsung]', 'https://thanhdatmobile.vn/wp-content/uploads/2022/11/samsung-galaxy-s21-ultra-bac-600x600-1-200x200-1.jpg'),
(N'Samsung Galaxy Note 20', '[12MP, 8GB, 256GB, 4300mAh, Samsung]', 'https://cdn.xtmobile.vn/vnt_upload/product/08_2019/thumbs/(600x600)_crop_Untitled_1.png'),
(N'Samsung Galaxy Note 20 Ultra', '[108MP, 8GB, 256GB, 4500mAh, Samsung]', 'https://cdn.tgdd.vn/Products/Images/42/220522/samsung-galaxy-note-20-ultra-vangdong-600x600-600x600.jpg'),
(N'Samsung Galaxy Z Fold 3', '[12MP, 12GB, 256GB, 4400mAh, Samsung]', 'https://product.hstatic.net/1000370129/product/22e4948bac3a33f22cdcc20_master_4111be7b3f1a4d92af8093a4cb5a53ef_master_afca7ce5a359420ba6640bdceff4524f_grande.png'), 
(N'Samsung Galaxy Z Flip 3', '[12MP, 8GB, 128GB, 3300mAh, Samsung]','https://cdn.tgdd.vn/Products/Images/42/248283/samsung-galaxy-z-flip-3-violet-1-600x600.jpg'),
(N'Xiaomi Mi 11', '[108MP, 8GB, 256GB, 4600mAh, Xiaomi]', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyq2s2Q4DKD7pu_XY70smU3RqGVtEdR2gJK_Z9Qb6RCA&s'),
(N'Xiaomi Mi 11 Ultra', '[50MP, 12GB, 412GB, 5000mAh, Xiaomi]', 'https://cdn.tgdd.vn/Products/Images/42/235578/xiaomi-mi-11-ultra-600x600-2-600x600.jpg'),
(N'Xiaomi Redmi Note 10', '[48MP, 6GB, 128GB, 5000mAh, Xiaomi]', 'https://cdn.tgdd.vn/Products/Images/42/222758/xiaomi-redmi-note-10-thumb-white-200x200.jpg'),
(N'OnePlus 9', '[50MP, 8GB, 128GB, 4500mAh, OnePlus]', 'https://cdn.tgdd.vn/Products/Images/42/222758/xiaomi-redmi-note-10-thumb-white-200x200.jpg'),
(N'OnePlus 9 Pro', '[50MP, 12GB, 256GB, 4500mAh, Google]', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0LlvUPw0XeZwWQbzF30d-_MOAbqNDlgPxdrLXZfh8tw&s'),
(N'Google Pixel 5', '[12.2MP, 8GB, 128GB, 4085mAh, Google]', 'https://cdn.tgdd.vn/Products/Images/42/198422/google-pixel-5-600jpg-600x600.jpg'),
(N'Google Pixel 6', '[50MP, 8GB, 128GB, 4614mAh, Google]', 'https://cdn.tgdd.vn/Products/Images/42/233009/google-pixel-6-600x600.jpg'),
(N'Google Pixel 6 Pro', '[50MP, 12GB, 128GB, 5003mAh, Google]','https://cdn.tgdd.vn/Products/Images/42/240166/google-pixel-6-pro-1-600x600.jpg'),
(N'Oppo Find X3 Pro', '[50MP, 12GB, 256GB, 4500mAh, OPPO]', 'https://cdn.xtmobile.vn/vnt_upload/product/12_2023/thumbs/(600x600)_crop_oppo-find-x3-pro-8gb-128gb-cu-99-xtmobile_1.jpg'),
(N'Oppo Reno 6', '[64MP, 8GB, 128GB, 4300mAh, OPPO]', 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/o/p/oppo-reno-6.png'),
(N'Vivo X60 Pro', '[48MP, 12GB, 256GB, 4200mAh, Vivo]', 'https://sc04.alicdn.com/kf/Hd8349d90071d43cfa75be96cb6b19353m.jpg'),
(N'Sony Xperia 1 III', '[12MP, 12GB, 256GB, 4500mAh, Sony]', 'https://cdn.viettablet.com/images/thumbnails/480/516/detailed/48/sony-xperia-1-iii--cau-hinh.jpg'),
(N'Sony Xperia 5 III', '[12MP, 8GB, 256GB, 4500mAh, Sony]', 'https://cdn.tgdd.vn/Products/Images/42/237591/sony-xperia-5-iii-600x600.jpg'),
(N'Asus ROG Phone 5', '[64MP, 16GB, 256GB, 6000mAh, Asus]', 'https://anhduongstore.net/wp-content/uploads/2021/08/asus-rog-phone-5-black.jpg'),
(N'Nokia 8.3', '[64MP, 8GB, 128GB, 4500mAh, Asus]', 'https://cdn2.cellphones.com.vn/x/media/catalog/product/n/o/nokia_8.3.jpg');
