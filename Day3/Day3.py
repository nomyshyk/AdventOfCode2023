import array

def test_return():
    mas = []
    with open('input3.txt') as fp:
        for line in fp:
            mas.append(line)
    some = 'nice'
    # print(some) 521393
    # 69527306
    # val = solve_task1(mas)
    val = solve_task2(mas)
    print(val)

    return some

# 4361
def solve_task1(list_of_strings):
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    coords = []
    summa = 0

    nums = []

    num_strok = len(list_of_strings)
    for idx_line, line in enumerate(list_of_strings):
        start_no = -1
        end_no = -1
        accumulate_number = ''
        # tuple3 = (-1, -1, -1)
        num_elem = len(line)
        for idx_symbol, symbol in enumerate(line):
            if start_no == -1 and symbol in number_list:
                start_no = idx_symbol
                end_no = idx_symbol
                accumulate_number += symbol
                if idx_symbol == num_elem-1:
                    # end_no = idx_symbol
                    nums.append(accumulate_number)
                    tuple3 = (idx_line, start_no, end_no)
                    addrs_to_check = locator(tuple3, num_strok, num_elem)
                    if checkMatrix(addrs_to_check, list_of_strings):
                        summa += int(accumulate_number)
                    coords.append(tuple3)
                    start_no = -1
                    end_no = -1
                    accumulate_number = ''
            elif start_no != -1 and symbol in number_list:
                end_no = idx_symbol
                accumulate_number += symbol
                if idx_symbol == num_elem-1:
                    end_no = idx_symbol
                    nums.append(accumulate_number)
                    tuple3 = (idx_line, start_no, end_no)
                    addrs_to_check = locator(tuple3, num_strok, num_elem)
                    if checkMatrix(addrs_to_check, list_of_strings):
                        summa += int(accumulate_number)
                    coords.append(tuple3)
                    start_no = -1
                    end_no = -1
                    accumulate_number = ''
                #print()
            elif start_no == -1 and symbol not in number_list:
                 start_no = -1
                 end_no = -1
                 accumulate_number = ''
            else:
                nums.append(accumulate_number)
                tuple3 = (idx_line, start_no, end_no)
                addrs_to_check = locator(tuple3, num_strok, num_elem)
                if checkMatrix(addrs_to_check, list_of_strings):
                    # print(int(accumulate_number))
                    summa += int(accumulate_number)
                coords.append(tuple3)
                start_no = -1
                end_no = -1
                accumulate_number = ''

        # print(line)
        # print(nums)
        # print(coords)
        #print("summa=")
        #print(summa)
    return summa

def locator(coordinate:tuple, maxX, maxY):
    y = coordinate[0]
    x_beg = coordinate[1]
    x_end = coordinate[2]
    # print(coordinate)
    search_mas = []
    for yC in range(y - 1, y + 2):
        for xC in range(x_beg-1, x_end+2):
            if -1 < yC < maxY and -1 < xC < maxX:
                if (yC == y and xC not in range(x_beg, x_end+1)) or yC != y:
                    search_mas.append((yC, xC))
    # print("Check here!")
    # print(search_mas)
    return search_mas

def checkMatrix(coordinateArray, matrix):
    for coord in coordinateArray:
        if matrix[coord[0]][coord[1]] != '.':
            # print(matrix[coord[0]][coord[1]])
            return True
    return False

def solve_task2(list_of_strings):
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    coords = []
    summa = 0

    nums = []

    num_strok = len(list_of_strings)
    hashCoordsDict = {}
    for idx_line, line in enumerate(list_of_strings):
        start_no = -1
        end_no = -1
        accumulate_number = ''
        # tuple3 = (-1, -1, -1)
        num_elem = len(line)
        for idx_symbol, symbol in enumerate(line):
            if start_no == -1 and symbol in number_list:
                start_no = idx_symbol
                end_no = idx_symbol
                accumulate_number += symbol
                if idx_symbol == num_elem - 1:
                    nums.append(accumulate_number)
                    tuple3 = (idx_line, start_no, end_no)
                    addrs_to_check = locator(tuple3, num_strok, num_elem)
                    star_coord = checkMatrix_task2(addrs_to_check, list_of_strings)
                    if star_coord:
                        for coor1 in star_coord:
                            hashCoordsDict[coor1] = hashCoordsDict.get(coor1, '') + str(accumulate_number) + ','
                        print(int(accumulate_number))
                        summa += int(accumulate_number)
                    coords.append(tuple3)
                    start_no = -1
                    end_no = -1
                    accumulate_number = ''
            elif start_no != -1 and symbol in number_list:
                end_no = idx_symbol
                accumulate_number += symbol
                if idx_symbol == num_elem - 1:
                    nums.append(accumulate_number)
                    tuple3 = (idx_line, start_no, end_no)
                    addrs_to_check = locator(tuple3, num_strok, num_elem)
                    star_coord = checkMatrix_task2(addrs_to_check, list_of_strings)
                    if star_coord:
                        for coor1 in star_coord:
                            hashCoordsDict[coor1] = hashCoordsDict.get(coor1, '') + str(accumulate_number) + ','
                        print(int(accumulate_number))
                        summa += int(accumulate_number)
                    coords.append(tuple3)
                    start_no = -1
                    end_no = -1
                    accumulate_number = ''
                # print()
            elif start_no == -1 and symbol not in number_list:
                start_no = -1
                end_no = -1
                accumulate_number = ''
            else:
                nums.append(accumulate_number)
                tuple3 = (idx_line, start_no, end_no)
                addrs_to_check = locator(tuple3, num_strok, num_elem)
                star_coord = checkMatrix_task2(addrs_to_check, list_of_strings)
                if star_coord:
                    for coor1 in star_coord:
                        hashCoordsDict[coor1] = hashCoordsDict.get(coor1, '') + str(accumulate_number) + ','
                    print(int(accumulate_number))
                    summa += int(accumulate_number)
                coords.append(tuple3)
                start_no = -1
                end_no = -1
                accumulate_number = ''

        # print(line)
        # print(nums)
        # print(coords)
        # print("summa=")
        # print(summa)

    result = 0
    for key in hashCoordsDict:
        # print(key + ' '+ hashCoordsDict.get(key))
        strMas = str(hashCoordsDict.get(key))[0:len(hashCoordsDict.get(key))-1].split(',')
        if len(strMas) == 2:
            result += (int(strMas[0]) * int(strMas[1]))
    return result

def checkMatrix_task2(coordinateArray, matrix):
    starCoords = []

    for coord in coordinateArray:
        if matrix[coord[0]][coord[1]] == '*':
            # print(matrix[coord[0]][coord[1]])
            starCoords.append((str(coord[0]) + ' ' + str(coord[1])))
    return starCoords