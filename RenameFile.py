# -*- coding: utf-8 -*-

import cv2


class GifReverser:
    global filename 
    filename = 'FILENAMEHERE'  # replace your filename here! DO NOT INCLUDE THE EXTENSION
    # DO NOT INCLUDE THE EXTENSION
    def __init__(self):
        pass

    def get_frames(gif_filename: str):
        vidcap = cv2.VideoCapture(gif_filename)
        framerate = vidcap.get(cv2.CAP_PROP_FPS)
        frames = []

        success, image = vidcap.read()
        while success:
            frames.append(image)
            success, image = vidcap.read()
        return (framerate, frames)

    # also works with mp4 files
    def reverse_gif(gif_filename: str, output_filename: str):
        framerate, frames = GifReverser.get_frames(gif_filename)
        height, width, layers = frames[0].shape
        size = (width, height)
        print('Your output file: ' + output_filename)
        print('Frame size: ' + str(size))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        print('Fourcc (video codec): ' + str(fourcc))
        print('Framerate: ' + str(framerate))
        print('...')
        out = cv2.VideoWriter(output_filename, fourcc, framerate, size, True)

        for i in range(len(frames)-1, -1, -1):
            out.write(frames[i])
        out.release()
        
if __name__ == '__main__':
    reversed_filename = filename + '_r'
    file = filename + '.mp4'
    reversed_file = reversed_filename + '.mp4'
    GifReverser.reverse_gif(file, reversed_file);
    print('Done!')