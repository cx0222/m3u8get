import os


def get_from_m3u8(filename: str, *args) -> list:
    with open(filename) as f:
        content: list = f.readlines()
    res: list = []
    for i in content:
        if i.startswith("http"):
            res.append(i.strip())
    print("[Begin]:", res[0])
    print("[End]:  ", res[-1])
    print("[Count]:", res.__len__())
    return res


def get_ts(li: list, *args) -> None:
    num: int = li.__len__()
    print(f"--> 一共有{num}个.ts文件")
    for i in range(0, num):
        print(f"\n\033[0;33m--开始获取第{i + 1}个.ts文件--\033[0m")
        os.system(f"wget \"{li[i]}\" --quiet --show-progress")
        print(f"\nwget \"{li[i]}\" --quiet --show-progress")
        print(f"\033[0;32m--第{i + 1}个.ts文件已获取--\033[0m")
        print("\n--进度：%.2f--" % ((i + 1) / num))
    print("--> 全部下载完成！")


def combine(li: list, *args) -> None:
    print("\n--> 开始合并.ts文件")
    command0 = f"cp \"{li[0].split('/')[-1]}\" \"0.ts\""
    os.system(command0)
    for i in range(1, li.__len__()):
        os.system(f"cat {i - 1}.ts {li[i].split('/')[-1]} > {i}.ts")
        os.system(f"rm {i - 1}.ts")
    print("--> 全部合并完成！")


if __name__ == "__main__":
    li: list = get_from_m3u8(input("请输入.m3u8文件名："))
    count: int = 0
    get_ts(li)
    combine(li)
