from augraphy.base.augmentation import Augmentation

class AugmentationSequence(Augmentation):
    """A list of Augmentations to be applied sequentially.

    :param augmentations: A list of Augmentation objects to be applied.
    :type augmentations: list
    :param p: The probability that this Augmentation will be applied.
    :type p: float, optional
    """

    def __init__(self, augmentations, p=0.5):
        """Constructor method"""
        self.augmentations = augmentations
        self.p = p

    def __repr__(self):
        output = f"AugmentationSequence([\n"
        for aug in augmentations:
            output += f"\t{repr(aug)}\n"

        output += "])"
        return output

    def __call__(self, data, force=False):
        if (force or self.should_run()):
            for augmentation in self.augmentations:
                augmentation(data)
