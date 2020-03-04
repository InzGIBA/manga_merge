from PIL import Image
import os

LIMIT_PIXEL = 5000
PATH_FOLDER = 'source'
FILE_EXT = 'jpg'


def img_size(value1, value2=None):
    if value2:
        return (value1.size[0], value1.size[1] + value2.size[1])
    return (value1.size[0], value1.size[1])


def img_paste(path, source=None):
    if source:
        path_image = Image.open(path)
        temp = Image.new('RGB', img_size(path_image, source), 'white')
        temp.paste(source)
        temp.paste(path_image, (0, source.size[1]))
        return temp
    return Image.open(path)


def img_save(image, index):
    image.save(f'result_{index}.jpg', "JPEG", quality=100)


def clear_path(path):
    return path.split('.')[0]


def get_path(path):
    array = []
    for item in os.listdir(path):
        array.append(int(clear_path(item)))
    return sorted(array)


def count():
    for index in range(100):
        yield index


def main():
    try:
        paths = get_path(PATH_FOLDER)
    except:
        print('Path error')
    else:
        temp_image = None
        generator = count()
        for index in paths:
            temp_image = img_paste(f'{PATH_FOLDER}/{index}.{FILE_EXT}', temp_image)
            if temp_image.size[1] > LIMIT_PIXEL:
                img_save(temp_image, next(generator))
                temp_image = None
        else:
            img_save(temp_image, next(generator))


if __name__ == '__main__':
    main()
