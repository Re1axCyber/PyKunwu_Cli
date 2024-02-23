import argparse
from logo import *
from Scripts import Scan
import asyncio


async def main():
    parser = argparse.ArgumentParser(description="一个简单的命令行参数解析示例")
    parser.add_argument("--CloudScan", help="是否启用云端扫描", default="True", type=bool)
    parser.add_argument("--path", '-p', help="扫描文件的路径",type=str)
    args = parser.parse_args()
    await Scan.get_type(args.path)


if __name__ == '__main__':

    print(kw_logo)
    print("--------------------------start----------------------------\n")
    asyncio.run(main())
    print("--------------------------end----------------------------\n")
