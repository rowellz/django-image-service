import imgaug.augmenters as iaa
from random import *
import imageio
import imgaug as ia
import os


class AugmentImageService:
    def aug_image(self, img_path: str):
        image = imageio.imread(img_path)
        image = ia.imresize_single_image(image, 0.5)

        image_list = []

        for i in range(10):
            rand_alpha = randint(1, 100)
            aug = iaa.ElasticTransformation(alpha=rand_alpha, sigma=10)
            image_aug_unaligned = aug(image=image)
            image_list.append(image_aug_unaligned)

        file_split = os.path.splitext(img_path)
        gif_path = f"{file_split[0]}.gif"
        print("Fdsafs", gif_path)
        imageio.mimwrite(gif_path, image_list, format= '.gif', fps = 5)

        return gif_path
 