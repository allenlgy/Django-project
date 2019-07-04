import re,requests,json
# 使用 page 来实现翻页
# 用 requests 请求当当网
# 将返回的 HTML 进行正则解析
# 内容存到文件中



# 请求当当网，请求成功之后拿到原码
def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        return None


# 用正则表达获取想要的信息
# 封装数据
def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).<div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }

# 存到 book 文件

def write_item_to_file(item):
    print('开始写入数据 ====>'+ str(item))
    with open('book.txt','a',encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()

def main(page):
    url = 'http://bang.dangdang.com/bools/fivestars/01.00.00.00.00.00-rencent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)  # 解析过滤想要的信息

    for item in items:

        write_item_to_file(item)


# 获取 25 页 500条数据
if __name__ == '__main__':
    for i in range(1,26):
        main(i)




