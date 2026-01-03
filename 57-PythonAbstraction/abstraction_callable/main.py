from functools import partial

from filters.grayscale import apply_grayscale
from filters.invert import apply_invert
from PIL import Image
from process_img import ImageFilterFn, process_img


def make_grayscale_filter(intensity: float = 1.0) -> ImageFilterFn:
    def filter_func(image: Image.Image) -> Image.Image:
        return apply_grayscale(image, intensity)

    return filter_func


def make_invert_filter(enabled: bool = True) -> ImageFilterFn:
    def filter_func(image: Image.Image) -> Image.Image:
        if enabled:
            return apply_invert(image)
        return image

    return filter_func


def main() -> None:
    input_image: str = "../input.jpg"

    grayscale_fn = partial(apply_grayscale, intensity=0.6) # Fn with preset intensity to work with Fn Type of callable[[Image], Image]
    # grayscale_fn = make_grayscale_filter(intensity=0.6)
    process_img(input_image, "output_callable_grayscale.jpg", grayscale_fn)

    process_img(input_image, "output_callable_invert.jpg", apply_invert)


if __name__ == "__main__":
    main()