# Fujian Electronic Trading Platform Data Fetching Project

This project is designed to fetch data from the Fujian Electronic Trading Platform, decrypt and process the data.

## Project Structure

```
.
├── src
│   └── crypto.js          # Encryption and decryption functions
├── main.py                # Main program
├── .env                   # Environment variable configuration file
├── package.json           # JavaScript dependency management
└── requirements.txt       # Python dependency management
```

## Features

1. Fetch data from the Fujian Electronic Trading Platform.
2. Decrypt the fetched data.
3. Process the data and output the results.

## Installation

1. Clone the project to your local machine:

   ```bash
   git clone <project-url>
   ```

2. Install JavaScript dependencies:

   ```bash
   npm install
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main program:

```bash
python main.py
```

## Configuration

The project uses a `.env` file to manage sensitive information. Ensure that the `.env` file contains the following:

```
AES_KEY=EB444973714E4A40876CE66BE45D5930
AES_IV=B5A8904209931867
```

---

# 福建省电子交易平台数据获取项目

这个项目用于从福建省电子交易平台获取数据，并对数据进行解密和处理。

## 项目结构

```
.
├── src
│   └── crypto.js          # 加密和解密功能
├── main.py                # 主程序
├── .env                   # 环境变量配置文件
├── package.json           # JavaScript依赖管理
└── requirements.txt       # Python依赖管理
```

## 功能

1. 从福建省电子交易平台获取数据。
2. 对获取的数据进行解密。
3. 处理数据并输出结果。

## 安装

1. 克隆项目到本地：

   ```bash
   git clone <项目地址>
   ```

2. 安装JavaScript依赖：

   ```bash
   npm install
   ```

3. 安装Python依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用

运行主程序：

```bash
python main.py
```

## 配置

项目使用 `.env` 文件来管理敏感信息。请确保 `.env` 文件中包含以下内容：

```
AES_KEY=EB444973714E4A40876CE66BE45D5930
AES_IV=B5A8904209931867
```