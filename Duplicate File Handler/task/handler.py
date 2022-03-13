# -----------------------------------------STAGE 1------------------------------------------------------

# import os
# import sys
#
# args = sys.argv
# if len(args) == 1:
#     print("Directory is not specified")
# else:
#     for root, dirs, files in os.walk(args[1]):
#         for name in files:
#             print(os.path.join(root, name))

# -----------------------------------------STAGE 2------------------------------------------------------
#
# import os
# import sys
#
# args = sys.argv
# if len(args) == 1:
#     print("Directory is not specified")
# else:
#     file_format = input("Enter file format:\n")
#
#     files_all = {}
#
#     for root, dirs, files in os.walk(args[1]):
#         for name in files:
#             # print(os.path.join(root, name))
#             # print(os.path.getsize(os.path.join(root, name)))
#             if int(os.path.getsize(os.path.join(root, name))) in files_all:
#                 files_all[int(os.path.getsize(os.path.join(root, name)))].append(str(os.path.join(root, name)))
#             else:
#                 files_all[int(os.path.getsize(os.path.join(root, name)))] = [str(os.path.join(root, name))]
#
#     # print(files_all)
#
#     files_selected = {}
#     if file_format:
#         for key, value in files_all.items():
#             if value[len(value) - len(file_format):] == file_format:
#                 files_selected[key] = value
#     else:
#         files_selected = files_all
#
#     # print(files_selected)
#
#     print("Size sorting options: \n1. Descending \n2. Ascending")
#     choice = int(input("Enter a sorting option:\n"))
#
#     while choice not in [1, 2]:
#         print("Wrong option")
#         choice = int(input("Enter a sorting option:\n"))
#
#     files_selected_keys = list(files_selected.keys())
#     # print(type(files_selected.keys()))
#
#     if choice == 1:
#         files_selected_keys.sort(key=lambda x: -x)
#     else:
#         files_selected_keys.sort()
#
#     for key in files_selected_keys:
#         print(f"{key} bytes")
#         print(*files_selected[key], sep='\n')

#  # -----------------------------------------STAGE 3------------------------------------------------------
#
# import os
# import sys
# import hashlib
#
# args = sys.argv
# if len(args) == 1:
#     print("Directory is not specified")
# else:
#     file_format = input("Enter file format:\n")
#
#     files_all = {}
#
#     for root, dirs, files in os.walk(args[1]):
#         for name in files:
#             # print(os.path.join(root, name))
#             # print(os.path.getsize(os.path.join(root, name)))
#             if int(os.path.getsize(os.path.join(root, name))) in files_all:
#                 files_all[int(os.path.getsize(os.path.join(root, name)))].append(str(os.path.join(root, name)))
#             else:
#                 files_all[int(os.path.getsize(os.path.join(root, name)))] = [str(os.path.join(root, name))]
#
#     print("all files:", files_all)
#
#     files_selected = {}
#     if file_format:
#         for key, value in files_all.items():
#             for item in value:
#                 if item[len(item) - len(file_format):] == file_format:
#                     if key in files_selected:
#                         files_selected[key].append(item)
#                     else:
#                         files_selected[key] = [item]
#     else:
#         files_selected = files_all
#
#     print("selected files: ", files_selected)
#
#     print("Size sorting options: \n1. Descending \n2. Ascending")
#     choice = int(input("Enter a sorting option:\n"))
#
#     while choice not in [1, 2]:
#         print("Wrong option")
#         choice = int(input("Enter a sorting option:\n"))
#
#     files_selected_keys = list(files_selected.keys())
#     # print(type(files_selected.keys()))
#
#     if choice == 1:
#         files_selected_keys.sort(key=lambda x: -x)
#     else:
#         files_selected_keys.sort()
#
#     for key in files_selected_keys:
#         print(f"{key} bytes")
#         print(*files_selected[key], sep='\n')
#
#     while True:
#         answer = input("Check for duplicates?")
#         if answer in['yes', 'no']:
#             break
#         print("Wrong option")
#
#     if answer == 'yes':
#         number = 1
#         files_selected_hashed_duplicated = {}
#         for key in files_selected_keys:
#             files_selected_hashed_temp = {}
#             for item in files_selected[key]:
#                 m = hashlib.md5()
#                 m.update(open(item, 'rb').read())
#                 hash_score = m.hexdigest()
#                 if hash_score in files_selected_hashed_temp:
#                     files_selected_hashed_temp[hash_score].append(item)
#                 else:
#                     files_selected_hashed_temp[hash_score] = [item]
#             # print("aaa", files_selected_hashed_temp)
#             files_selected_hashed_duplicated[key] = {}
#             for hash_score in files_selected_hashed_temp.keys():
#                 if len(files_selected_hashed_temp[hash_score]) > 1:
#                     files_selected_hashed_duplicated[key][hash_score] = []
#                     for item in files_selected_hashed_temp[hash_score]:
#                         files_selected_hashed_duplicated[key][hash_score].append((number, item))
#                         number += 1
#             # print()
#             # print(f"{key} bytes")
#             # print(files_selected_hashed[key])
#
#         # print(files_selected_hashed)
#         for key in files_selected_keys:
#             print(f"{key} bytes")
#             for hash_score in files_selected_hashed_duplicated[key].keys():
#                 print(f"Hash: {hash_score}")
#                 for item in files_selected_hashed_duplicated[key][hash_score]:
#                     print(f"{item[0]}. {item[1]}")

# -----------------------------------------STAGE 4------------------------------------------------------

import os
import sys
import hashlib

args = sys.argv
if len(args) == 1:
    print("Directory is not specified")
else:
    file_format = input("Enter file format:\n")

    files_all = {}

    for root, dirs, files in os.walk(args[1]):
        for name in files:
            # print(os.path.join(root, name))
            # print(os.path.getsize(os.path.join(root, name)))
            if int(os.path.getsize(os.path.join(root, name))) in files_all:
                files_all[int(os.path.getsize(os.path.join(root, name)))].append(str(os.path.join(root, name)))
            else:
                files_all[int(os.path.getsize(os.path.join(root, name)))] = [str(os.path.join(root, name))]

    print("all files:", files_all)

    files_selected = {}
    if file_format:
        for key, value in files_all.items():
            for item in value:
                if item[len(item) - len(file_format):] == file_format:
                    if key in files_selected:
                        files_selected[key].append(item)
                    else:
                        files_selected[key] = [item]
    else:
        files_selected = files_all

    print("selected files: ", files_selected)

    print("Size sorting options: \n1. Descending \n2. Ascending")
    choice = int(input("Enter a sorting option:\n"))

    while choice not in [1, 2]:
        print("Wrong option")
        choice = int(input("Enter a sorting option:\n"))

    files_selected_keys = list(files_selected.keys())
    # print(type(files_selected.keys()))

    if choice == 1:
        files_selected_keys.sort(key=lambda x: -x)
    else:
        files_selected_keys.sort()

    for key in files_selected_keys:
        print(f"{key} bytes")
        print(*files_selected[key], sep='\n')

    while True:
        answer = input("Check for duplicates?\n")
        if answer in['yes', 'no']:
            break
        print("Wrong option\n")

    if answer == 'yes':
        number = 1
        files_selected_hashed_duplicated = {}
        for key in files_selected_keys:
            files_selected_hashed_temp = {}
            for item in files_selected[key]:
                m = hashlib.md5()
                m.update(open(item, 'rb').read())
                hash_score = m.hexdigest()
                if hash_score in files_selected_hashed_temp:
                    files_selected_hashed_temp[hash_score].append(item)
                else:
                    files_selected_hashed_temp[hash_score] = [item]
            # print("aaa", files_selected_hashed_temp)
            files_selected_hashed_duplicated[key] = {}
            for hash_score in files_selected_hashed_temp.keys():
                if len(files_selected_hashed_temp[hash_score]) > 1:
                    files_selected_hashed_duplicated[key][hash_score] = []
                    for item in files_selected_hashed_temp[hash_score]:
                        files_selected_hashed_duplicated[key][hash_score].append((number, item))
                        number += 1
            # print()
            # print(f"{key} bytes")
            # print(files_selected_hashed[key])

        # print(files_selected_hashed)
        for key in files_selected_keys:
            print(f"{key} bytes")
            for hash_score in files_selected_hashed_duplicated[key].keys():
                print(f"Hash: {hash_score}")
                for item in files_selected_hashed_duplicated[key][hash_score]:
                    print(f"{item[0]}. {item[1]}")

        while True:
            answer2 = input("Delete files?\n")
            if answer2 in ['yes', 'no']:
                break
            print("Wrong option\n")

        if answer2 == 'yes':
            while True:
                try:
                    num_to_delete = list(map(lambda x: int(x), input("Enter file numbers to delete:\n").split()))
                except ValueError:
                    print("Wrong format\n")
                    continue
                # files_to_delete = [int(x) for x in input("Enter file numbers to delete:\n").split()]
                if num_to_delete and len(num_to_delete) == len(set(num_to_delete)) and \
                        all(item in set(map(lambda x: x, range(1, number))) for item in num_to_delete):
                    break
                print("Wrong format\n")

            space_freed = 0
            files_to_delete = []

            for key in files_selected_keys:
                for hash_score in files_selected_hashed_duplicated[key].keys():
                    for item in files_selected_hashed_duplicated[key][hash_score]:
                        if item[0] in num_to_delete:
                            files_to_delete.append(item[1])

            for file_ in files_to_delete:
                space_freed += os.path.getsize(file_)
                # print(file_)
                os.remove(file_)

            print(f"Total freed up space: {space_freed} bytes")



