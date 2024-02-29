import aiohttp
from config import *
import os
import base64
import hashlib
import json
from time import sleep


def calc_md5(content):
    try:
        h = hashlib.md5()
        h.update(content.encode())
        return h.hexdigest()
    except Exception as e:
        print(f"出现错误：{e}")
        pass


async def upload_file(file_md5, file_text):
    try:
        conn = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            headers = {"Content-Type": "application/json"}
            data = {"webshell_text": str(base64.b64encode(bytes(file_text, encoding='utf-8')).decode())}
            # print(data)
            # print(url+"/api/v1/anonymous_see_file?apikey="+apikey+"&md5="+file_md5)

            async with session.get(url + "/api/v1/anonymous_see_file?apikey=" + apikey + "&md5=" + file_md5, json=data,
                                   headers=headers) as check_resp:
                print("正在进行历史结果探测")
                resp = await check_resp.text()
                result = json.loads(resp)["result"]
                if result != "":
                    print(f"云端结果已存在,云端扫描结果为：{result}")
                else:
                    print("云端结果不存在,开始上传")
                    async with session.post(url + "/api/v1/anonymous_up_file?apikey=" + apikey + "&md5=" + file_md5,
                                            json=data, headers=headers) as resp:
                        print(resp.status)
                        print(await resp.json())
                        print("文件上传成功")
                        print()
                        for i in range(0, 10):
                            print("正在等待云端扫描返回结果")
                            async with session.get(url + "/api/v1/anonymous_see_file?apikey=" + apikey + "&md5=" + file_md5,
                                                   json=data, headers=headers) as upload_resp:
                                response = await upload_resp.text()
                                print(json.loads(response))
                                result = json.loads(response)["result"]
                                print(f"云端扫描结果为：{result}")
                                if result != "":
                                    break
                                elif i == 12 and result == "" :
                                    print("云端响应结果超时")
                            sleep(3)
    except Exception as e:
        print(f"出现错误：{e}")
        pass

async def list_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            print(os.path.join(root, f))
            await upload_file(calc_md5(file_text(os.path.join(root, f))), file_text(os.path.join(root, f)))


async def get_type(filepath):
    if os.path.exists(filepath):
        if os.path.isdir(filepath):
            print("{} 是一个文件夹".format(filepath))
            await list_files(filepath)
        else:
            print("{} 是一个文件".format(filepath))
            await upload_file(calc_md5(file_text(filepath)), file_text(filepath))
            # file_text(path)
    else:
        print("{} 不存在或者不是一个文件或文件夹".format(filepath))


def file_text(path):
    try:
        text = open(path, 'r', encoding='utf-8').read()
        return text
    except Exception as e:
        print(f"出现错误：{e}")
        pass


# get_type(path)


# print(os.stat(path).st_size)
# print(os.path.basename(path))
