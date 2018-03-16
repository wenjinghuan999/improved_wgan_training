
import os
import imageio

DIR = 'result/gan_cifar/'
TITLE = 'samples_'
IMAGE_SUFFIX = '.jpg'
IMAGE_MAX = 25000
GIF_SUFFIX = '.gif'
GIF_DURATION = 0.5


def images_to_gif(root_dir, input_filenames, output_filename):
    with imageio.get_writer(os.path.join(root_dir, output_filename), mode='I') as writer:
        writer.duration = GIF_DURATION
        for filename in input_filenames:
            image = imageio.imread(os.path.join(root_dir, filename))
            writer.append_data(image)
        print('GIF GENERATED:', output_filename, '-', len(input_filenames), 'frames')
        print('FILES:', input_filenames)


def check_numbers(names):
    assert names
    i = 0
    j = 0
    while i < len(names):
        if names[i][0] == j:
            i += 1
            j += 1
            continue
        elif names[i][0] < j:
            print(i, 'duplicated or negative?!')
            i += 1
        else:
            print(j, 'missing')
            j += 1


def main():
    root_dir = DIR
    for path, dirs, files in os.walk(root_dir):
        files = [file for file in files if os.path.splitext(file)[1] == IMAGE_SUFFIX]
        names = [(os.path.splitext(file)[0], file) for file in files]
        names = [(name[len(TITLE):], file) for name, file in names if name.startswith(TITLE)]
        names = [(int(nostr), file) for nostr, file in names if nostr.isdigit() and int(nostr) < IMAGE_MAX]

        names.sort(key=lambda x: x[0])
        # check_numbers(names)
        input_filenames = [file for _, file in names]
        output_filename = TITLE + GIF_SUFFIX
        images_to_gif(path, input_filenames, output_filename)

if __name__ == '__main__':
    main()
