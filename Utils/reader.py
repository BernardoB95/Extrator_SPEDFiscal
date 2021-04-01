import os


class Reader:

    _file_names = []
    _file_dict = {}

    def __init__(self, dir_path):
        self._path = dir_path

        for file in os.listdir(dir_path):
            if file.endswith('.txt'):
                self._file_names.append(os.path.join(self._path, file))

    def ReadFiles(self):
        """
        This method creates a key, value pair in a dictionary for each file retrieved in the
        directory.

        :return: _file_dict
        :rtype: Dict{string: List}
        """

        for file in self._file_names:
            file_list = []

            with open(file, 'r', encoding='mbcs') as sped:
                file_list = sped.read().splitlines()

            if not self.isSigned(file_list):
                file_list = self.stripSignature(file_list)

            self._file_dict[file] = file_list

        return self._file_dict

    @staticmethod
    def isSigned(file):
        """
        Checks if the file has a signature embeded or not.

        :param file: Sped Fiscal
        :type file: list
        :return: True or False statemente
        :rtype: boolean
        """

        if '|9999|' in file[-1]:
            return True
        else:
            return False

    @staticmethod
    def stripSignature(file):
        """
        Strips out all lines from the digital signature.

        :param file: Sped Fiscal
        :type file: list
        :return: Stripped Sped Fiscal
        :rtype: list
        """

        while '|9999|' not in file[-1]:
            file.pop(-1)

        return file