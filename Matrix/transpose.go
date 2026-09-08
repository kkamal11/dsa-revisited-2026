func transpose(matrix [][]int) [][]int {
    rows := len(matrix)
    cols := len(matrix[0])

	/*
    result := [][]int{}
    for i:=0;i<cols;i++{
        result = append(result, make([]int, rows))
    }
		*/
	result := make([][]int, cols)
	for i:=0; i<cols; i++{
		result[i] = make([]int, rows)
	}

    for i:=0; i<rows;i++{
        for j:=0; j<cols; j++{
            result[j][i] = matrix[i][j]
        }
    }

    return result
}