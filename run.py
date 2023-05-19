from mjclone.kand import fuse_images

img1_path = "./data/test_00.jpeg"
img2_path = "./data/test_01.jpeg"


if __name__ == "__main__":
    rets = fuse_images(img1_path, img2_path)
    for i, ret in enumerate(rets):
        ret.save(f"assets/img_{i}.png")
