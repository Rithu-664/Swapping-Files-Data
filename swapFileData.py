def swapFileData():
        fileNo1 = str(input('Enter source file name: '))
        fileNo2 = str(input('Enter destination file name: '))

        with open(fileNo1, 'r') as file1:
                dataA = file1.read()

                with open(fileNo2, 'r') as file2:
                        dataB = file2.read()

        with open(fileNo1, 'w') as file1:
                file1.write(dataB)

        with open(fileNo2, 'w') as file2:
                file2.write(dataA)

swapFileData()