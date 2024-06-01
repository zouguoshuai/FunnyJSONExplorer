from units.JsonLoader import *
from units.IconFamily import *
from AbstractJsonFactory import *
from Director import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # 添加命令行参数
    parser.add_argument("-f", "--file", help="Specify the JSON file")
    parser.add_argument("-s", "--style", help="Specify the style")
    parser.add_argument("-i", "--icon", help="Specify the icon family")
    # 解析命令行参数
    args = parser.parse_args()

    director = Director()
    builder = None
    icon = None

    data = JsonLoader(args.file)

    if args.style == 'tree':
        builder = TreeStyleJsonFactory()
    else:
        builder = RectangleStyleJsonFactory()

    icon = IconFamily(args.icon)
    director.Construct(builder)
    product = builder.getResult()
    product.show(data, icon)

