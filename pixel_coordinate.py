import cv2


def pixels(image, rgb_set):
    set = list()

    for j in range(0, image.shape[0]):
        for i in range(0, image.shape[1]):
            if image[j][i] == rgb_set:
                set.append([j, i])
    return set


image = cv2.imread("map_eng.jpg")
print('image.shape = ', image.shape)
print('image[0][0].shape = ', image[0][0].shape)
pinks = pixels(image, [255, 128, 255])

print(pinks)
