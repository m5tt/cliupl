class UplSitePlugin:
    """
    Abstract class for a upload site
    """

    def upload(self, img_file, args):
        raise NotImplementedError(
            f'Class {self.__class__.__name__} doesnt implement upload()')
