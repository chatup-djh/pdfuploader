from bs4 import BeautifulSoup

# 打开你的HTML文件
with open("data/123.html", "r", encoding='utf-8') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    # 找到class为"amz-preview-content"的元素
    elements = soup.find_all(class_="amz-preview-content")

    # 创建一个空列表来保存找到的信息
    info_list = []

    # 在每个"amz-preview-content"元素中找到所有class为"amz-tab-wrapper"的div
    for element in elements:
        divs = element.find_all('div', class_="amz-tab-wrapper")

        # 在每个div中找到所有class为"amz-item"的元素
        for div in divs:
            items = div.find_all(class_="amz-item")

            # 在每个item中找到class为"amz-item-title"和"amz-item-intro description"的元素，以及href属性
            for item in items:
                title = item.find(class_="amz-item-title").text
                description = item.find(class_="amz-item-intro description").text
                href = item.find('a')['href']

                # 将这些信息保存在一个字典中，并添加到列表中
                info = {'title': title, 'description': description, 'href': href}
                info_list.append(info)

    # 现在，info_list包含了所有找到的信息
    for info in info_list:
        print(info_list)
html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #F5F5F5;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .item {
            flex: 0 0 calc(16.66667% - 20px);
            margin: 10px;
            padding: 20px;
            background-color: #FFFFFF;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .item h2 {
            margin: 0;
            font-size: 16px;
            color: #333;
        }
        .item p {
            margin: 10px 0 0;
            font-size: 14px;
            color: #999;
        }
        .item a {
            color: inherit;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>AI工具导航</h1>
    <div class="container">
"""

for info in info_list:
    html += f"""
        <div class="item">
            <a href="{info['href']} " target="_blank">
                <h2>{info['title']}</h2>
                <p>{info['description']}</p>
            </a>
        </div>
    """

html += """
    </div>
</body>
</html>
"""

# 将生成的HTML保存到一个文件中
with open("../../templates/index/AIIndex.html", "w", encoding='utf-8') as f:
    f.write(html)
