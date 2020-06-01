-- 创建表空间
CREATE DATABASE my_suppliers;
SHOW DATABASES;

-- 创建表
CREATE TABLE IF NOT EXISTS Suppliers
(Supplier_Name VARCHAR(20),
 Invoice_Number VARCHAR(20),
 Part_Number VARCHAR(20),
 Cost FLOAT,
 Purchase_Date DATE);

-- 查看表结构
DESCRIBE Suppliers;

-- 创建用户并授权
CREATE USER 'ffawp'@'localhost' IDENTIFIED BY 'Aa123456';
GRANT ALL PRIVILEGES ON my_suppliers.* TO 'ffawp'@'localhost';
FLUSH PRIVILEGES;

-- 排错
-- 如果报Library not loaded: libcrypto.1.0.0.dylib
-- Library not loaded: libssl.1.0.0.dylib, Library not loaded: @rpath/libmysqlclient.21.dylib等
-- ln -s /usr/local/mysql/lib/libmysqlclient.21.dylib /usr/local/lib/libmysqlclient.21.dylib
-- ln -s /usr/local/mysql/lib/libssl.1.0.0.dylib /usr/local/lib/libssl.1.0.0.dylib
-- ln -s /usr/local/mysql/lib/libcrypto.1.0.0.dylib /usr/local/lib/libcrypto.1.0.0.dylib