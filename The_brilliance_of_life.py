# PythonとOpenCVでいのちを輝かせる
# https://qiita.com/Takayoshi_Makabe/items/07e4553362fc14d7ddb1

# Pythonでグラフのアニメを作る（OpenCVでmp4ファイルを出力編）
# https://water2litter.net/rum/post/python_matplotlib_anime_opencv/

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib
matplotlib.use('TkAgg')
FIG_SIZE = 512


def get_coordinates(center_x: int, center_y: int, rotate_val: int, speed: int):
    radius = 10
    theta = (rotate_val / speed) * 2 * np.pi
    x = center_x + int(radius * np.sin(theta))
    y = center_y + int(radius * np.cos(theta))
    return x, y


def make_like_image(rotate_val: int):
    # back groud
    back = np.ones((FIG_SIZE, FIG_SIZE, 3), np.uint8) * 255

    # red circle
    cv2.circle(back, (80, 160), 53, (231, 0, 18), -1)
    cv2.circle(back, (160, 186), 47, (231, 0, 18), -1)
    cv2.circle(back, (162, 115), 47, (231, 0, 18), -1)
    cv2.circle(back, (225, 60), 50, (231, 0, 18), -1)
    cv2.circle(back, (330, 90), 65, (231, 0, 18), -1)
    cv2.ellipse(back, (380, 170), (76, 36), 0, 0, 360, (231, 0, 18), -1)
    cv2.ellipse(back, (370, 250), (45, 55), 0, 0, 360, (231, 0, 18), -1)
    cv2.ellipse(back, (352, 350), (70, 65), 0, 0, 360, (231, 0, 18), -1)
    cv2.circle(back, (262, 422), 66, (231, 0, 18), -1)
    cv2.circle(back, (170, 408), 46, (231, 0, 18), -1)
    cv2.ellipse(back, (128, 340), (30, 54), 0, 0, 360, (231, 0, 18), -1)
    cv2.circle(back, (95, 258), 60, (231, 0, 18), -1)

    # eyes
    center_x, center_y = 68, 152
    cv2.circle(back, (center_x, center_y), 28, (255, 255, 255), -1)
    cv2.circle(back, get_coordinates(center_x, center_y, rotate_val, 10), 13, (29, 143, 255), -1)

    center_x, center_y = 350, 70
    cv2.circle(back, (center_x, center_y), 28, (255, 255, 255), -1)
    cv2.circle(back, get_coordinates(center_x, center_y, rotate_val+1, 25), 13, (29, 143, 255), -1)

    center_x, center_y = 378, 355
    cv2.ellipse(back, (center_x, center_y), (33, 30), 0, 0, 360, (255, 255, 255), -1)
    cv2.circle(back, get_coordinates(center_x, center_y, rotate_val+4, -25), 15, (29, 143, 255), -1)

    center_x, center_y = 253, 442
    cv2.circle(back, (center_x, center_y), 25, (255, 255, 255), -1)
    cv2.circle(back, get_coordinates(center_x, center_y, rotate_val+3, 25), 10, (29, 143, 255), -1)

    center_x, center_y = 105, 275
    cv2.circle(back, (center_x, center_y), 26, (255, 255, 255), -1)
    cv2.circle(back, get_coordinates(center_x, center_y, rotate_val+2, -25), 12, (29, 143, 255), -1)

    # plt.imshow(back)
    # plt.show()

    return back


if __name__ == '__main__':
    # OpenCVの設定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('out.mp4', fourcc, 20.0, (FIG_SIZE, FIG_SIZE))

    for i in range(200):
        # 描画
        fig = plt.figure(figsize=(FIG_SIZE / 100, FIG_SIZE / 100))

        life_img = make_like_image(i)
        plt.imshow(life_img)
        fig.canvas.draw()

        # VideoWriterへ書き込み
        image_array = np.array(fig.canvas.renderer.buffer_rgba())
        im = cv2.cvtColor(image_array, cv2.COLOR_RGBA2BGR)
        video.write(im)
        plt.close()

    video.release()
