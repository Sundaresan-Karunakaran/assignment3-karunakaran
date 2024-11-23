class YtmdlError(Exception):
    """Base class for all ytmdl related exceptions."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class DownloadError(YtmdlError):
    """Exception for download error."""
    def __init__(self, link: str, error: str) -> None:
        message = f"Download failed for `{link}` with error: {error}"
        super().__init__(message)


class ConvertError(YtmdlError):
    """Exception for conversion errors."""
    def __init__(self, error: str) -> None:
        message = f"Conversion failed with error: {error}"
        super().__init__(message)


class NoMetaError(YtmdlError):
    """Exception for no metadata found."""
    def __init__(self, song: str) -> None:
        message = f"No metadata found for `{song}`"
        super().__init__(message)


class MetadataError(YtmdlError):
    """Exception for errors while setting metadata."""
    def __init__(self, song: str) -> None:
        message = f"Something went wrong while setting metadata for `{song}`"
        super().__init__(message)


class ExtractError(YtmdlError):
    """Exception for extraction-related errors."""
    def __init__(self, song: str) -> None:
        message = f"Couldn't extract data for: {song}"
        super().__init__(message)
