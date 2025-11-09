from functions.get_files_info import get_files_info


def main():
    print("Result for current directory:")
    test1 = get_files_info("calculator", ".")
    print(f'  {test1}')

    print("Result for 'pkg' directory:")
    test2 = get_files_info("calculator", "pkg")
    print(f'  {test2}')

    print("Result for '/bin' directory:")
    test3 = get_files_info("calculator", "/bin")
    print(f'  {test3}')

    print("Result for '../' directory:")
    test4 = get_files_info("calculator", "../")
    print(f'  {test4}')


main()
