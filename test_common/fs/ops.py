"""
Functions for file operations (copy, delete, etc).
"""
import typing


def delete_file(file_path: str) -> None:
    """ Delete an specific file.

    :param file_path: string with the absolute path to file.
    :raise: FileNotFoundError if given file is not found.
    """
    raise NotImplementedError


def delete_files(files: typing.List[str], ignore_missing: bool) -> None:
    """ Delete all files set in given list.

    :param files: List with absolute pathname for files to remove.
    :param ignore_missing: If true does not return an error if any of files actually does not exists.
    :raise: FileNotFoundError if given file is not found unless ignore_missing was true.
    """
    raise NotImplementedError


def copy_file(source_file_path: str, destination_file_path: str) -> None:
    """ Copy an specific file.

    :param source_file_path: String with absolute pathname to original file.
    :param destination_file_path: String with absolute pathname to copied file.
    :raise: FileNotFoundError if any given source file is not found.
    """
    raise NotImplementedError


def copy_files(files: typing.List[str], destination_folder_path: str) -> None:
    """ Copy all files in an given list to a given destination folder.

    Original file names are kept untouched.

    :param files: List with absolute file path names as strings.
    :param destination_folder_path: Absolute path name to folder where to copy files into.
    :raise: FileNotFoundError if any given source file is not found.
    """
    raise NotImplementedError

