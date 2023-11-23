import imgaug.augmenters as iaa
from random import *
import imageio
import imgaug as ia
import os


class AugmentImageService:
    def create_gif(self, img_path: str, min: int, max: int, fps: int):
        image = imageio.imread(img_path)
        image = ia.imresize_single_image(image, 0.5)

        image_list = []

        for i in range(10):
            distorted_image = self.distort_image(image, min, max)
            image_list.append(distorted_image)

        file_split = os.path.splitext(img_path)
        gif_path = f"{file_split[0]}.gif"
        imageio.mimwrite(gif_path, image_list, format='.gif', fps=fps, loop=0)

        return gif_path

    def distort_image(self, image, min: int, max: int):
            rand_alpha = randint(int(min), int(max))
            aug = iaa.ElasticTransformation(alpha=rand_alpha, sigma=10)
            aug_image = aug(image=image)
            return aug_image