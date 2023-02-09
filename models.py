def add_data(lst):
    for i in range(len(lst)):
        with open("txt1.txt", 'a') as file1:
            file1.writelines(lst[i]+'\n')
        with open('txt2.txt', 'a') as file2:
            file2.writelines(f'{lst[i]};\t')
    with open("txt1.txt", 'a') as file1:
        file1.writelines(' \n')
    file1.close()


