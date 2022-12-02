import os
import time
from datetime import datetime
from matplotlib import pyplot as plt


def read(path):
    root = '/home/zhujingqi/code/AFL++'
    file_path1 = os.path.join(root, path)
    images = []
    if os.path.isfile(file_path1):
        with open(file_path1, 'r') as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                data = line.split('/t/n')
                for str in data:
                    sub_str = str.split(', ')
                if sub_str:
                    images.append(sub_str)
    return images


def trans_time(time_now):
    # 转换成localtime
    time_local = time.localtime(time_now)

    # 转换成新的时间格式(如：2016-05-09 18:59:20)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    # 输出时间标准格式
    return dt


def draw():
    # 设置图片大小
    # fig = plt.figure(figsize=(20, 8), dpi=80)  # plt.figure用来设置图像大小，dpi参数调节图片清晰度
    fig = plt.figure(figsize=(40, 15), dpi=200)
    # 设置x轴刻度
    plt.xticks(x_range)  # 设置x轴刻度 可以以plt.xticks(range(2,26))的样式来调节x刻度参数
    # 绘图
    plt.plot(time_list6, cov6, color='skyblue', label='afl++_strip')
    plt.plot(time_list5, cov5, color='black', label='afl++_size')
    plt.plot(time_list4, cov4, color='blue', label='afl++_readelf')
    plt.plot(time_list3, cov3, color='red', label='afl++_objdump')
    plt.plot(time_list2, cov2, color='green', label='afl++_nm')
    plt.plot(time_list1, cov1, color='yellow', label='afl++_cxxfilt')# 传入x，y绘制出折线图
    # 显示图例
    plt.legend()
    # 横纵轴标签
    plt.xlabel("running time/min", fontdict={'size': 16})
    plt.ylabel("code coverage/%", fontdict={'size': 16})
    # 网格线
    plt.grid(True, linestyle='--', alpha=0.5)
    # 保存图片
    plt.savefig("./afl++_cov.png")  # 保存图片


if __name__ == '__main__':
    image = read('afl++_out/out_cxxfilt/default/plot_data')
    time_list1 = []
    cov1 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list1.append(period // 60)
            cov1.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    image = read('afl++_out/out_nm/default/plot_data')
    time_list2 = []
    cov2 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list2.append(period // 60)
            cov2.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    image = read('afl++_out/out_objdump/default/plot_data')
    time_list3 = []
    cov3 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list3.append(period // 60)
            cov3.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    image = read('afl++_out/out_readelf/default/plot_data')
    time_list4 = []
    cov4 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list4.append(period // 60)
            cov4.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    image = read('afl++_out/out_size/default/plot_data')
    time_list5 = []
    cov5 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list5.append(period // 60)
            cov5.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    image = read('afl++_out/out_strip/default/plot_data')
    time_list6 = []
    cov6 = []
    start_time = datetime.strptime(trans_time(int(image[0][0])), "%Y-%m-%d %H:%M:%S")
    cnt = 0
    for item in image:
        current_time = datetime.strptime(trans_time(int(item[0])), "%Y-%m-%d %H:%M:%S")
        period = (current_time - start_time).seconds
        if period // 60 >= cnt:
            time_list6.append(period // 60)
            cov6.append(float(item[6].replace("%", "")))
            cnt = period // 60 + 1

    x_range = range(0, 1 + max(time_list1[len(time_list1) - 1],
                               time_list2[len(time_list2) - 1],
                               time_list3[len(time_list3) - 1],
                               time_list4[len(time_list4) - 1],
                               time_list5[len(time_list5) - 1],
                               time_list6[len(time_list6) - 1]))
    draw()
