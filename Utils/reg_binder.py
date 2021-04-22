# Imports
from Regs import NullReg
from itertools import count

def bind_id(binding_list, reg, index):
    """
    Function that will perform the REGs binding in order to identify the hierarchy.
    Object reg is modified inside the function.
    :param binding_list: list of reg objects
    :type binding_list: list
    :param reg: REG identifier
    :type reg: str
    :param index: current index of the reg to work as a pointer
    :type index: int
    :return: index of the super(pythonic) or father hierarchy reg
    :rtype: int
    """

    if reg.hierarchy == '0':
        reg.id_super = None
    elif isinstance(reg, NullReg):
        pass
    else:

        # pointer = index
        # while pointer >= 0:
        #
        #     if isinstance(binding_list[pointer], NullReg):
        #         pointer -= 1
        #         continue
        #
        #     pointer_h = binding_list[pointer].hierarchy
        #
        #     if pointer_h < reg.hierarchy:
        #         reg.id_super = binding_list[pointer].id
        #         break
        #     pointer -= 1

        # for pointer in range(index, -1, -1):
        #
        #     if isinstance(binding_list[pointer], NullReg):
        #         continue
        #
        #     pointer_h = binding_list[pointer].hierarchy
        #
        #     if pointer_h < reg.hierarchy:
        #         reg.id_super = binding_list[pointer].id
        #         break

        counter = count(index, -1)

        for pointer in counter:

            if pointer == -1:
                break

            if isinstance(binding_list[pointer], NullReg):
                continue

            pointer_h = binding_list[pointer].hierarchy

            if pointer_h < reg.hierarchy:
                reg.id_super = binding_list[pointer].id
                break
