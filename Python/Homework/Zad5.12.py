tablica = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

# 11 22 33    11 44 77
# 44 55 66 => 22 55 88
# 77 88 99    33 66 99

# 11: [0][0] => [0][0]    // [rId][cId] =>  [cId][rId]
# 22: [0][1] => [1][0]    //
# 33: [0][2] => [2][0]    //
# 44: [1][0] => [0][1]    //
# 55: [1][1] => [1][1]    //
# 66: [1][2] => [2][1]    //
# 77: [2][0] => [0][2]    //
# 88: [2][1] => [1][2]    //
# 99: [2][2] => [2][2]    //
#   [rId][cId] =>

pomocniczaTablica = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
rowsCount = len(tablica)
columnCount = len(tablica[0])

for rowIndex in range(rowsCount):
    for columnIndex in range(columnCount):
        pomocniczaTablica[columnIndex][rowIndex] = tablica[rowIndex][columnIndex]

print(pomocniczaTablica)

































































