#!/usr/bin/env python3

class MatrixInverter():
    def __init__(self):
        self.matrix = []

    def invert_matrix(self):
        matrix = self.matrix

        n = len(matrix)
        m = len(matrix[0])

        # 创建一个增广矩阵，右半部分是单位矩阵
        augmented_matrix = []
        for i, row in enumerate(matrix):
            numb = []
            for j in range(n):
                if i == j:
                    numb.append(1)
                else:
                    numb.append(0)
            augmented_matrix.append(row + numb)

        # 高斯-约当消元法
        for col in range(n):
            # 寻找主元素所在行
            pivot_row = col
            for row in range(col + 1, n):
                if abs(augmented_matrix[row][col]) > abs(augmented_matrix[pivot_row][col]):
                    pivot_row = row

            # 交换行
            augmented_matrix[col], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[col]

            # 缩放主元素为1
            pivot_val = augmented_matrix[col][col]
            for j in range(n + m):
                augmented_matrix[col][j] /= pivot_val

            # 消元其他行的元素
            for row in range(n):
                if row != col:
                    factor = augmented_matrix[row][col]
                    for j in range(n + m):
                        augmented_matrix[row][j] -= factor * \
                            augmented_matrix[col][j]

        # 提取逆矩阵部分
        inverse_matrix = []
        for row in augmented_matrix:
            inverse_matrix.append(row[n:])

        return inverse_matrix

    def read_matrix_from_file(self, filename):
        matrix = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            dimensions = lines[0].split()  # 第一行包含维度信息
            num_rows = int(dimensions[0])
            num_cols = int(dimensions[1])

            # 从文件的第二行开始读取矩阵数据
            for line in lines[1:]:
                row = []
                for x in line.split():
                    row.append(int(x))

                matrix.append(row)

        return matrix

    def write_matrix_to_file(self, matrix, filename):
        with open(filename, 'w') as file:
            num_rows = len(matrix)
            num_cols = len(matrix[0])

            # 写入矩阵的维度信息
            file.write(f"{num_rows} {num_cols}\n")

            # 写入矩阵数据
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")

    def is_invertible(self):
        matrix = self.matrix

        # 检查矩阵是否为方阵
        n = len(matrix)
        m = len(matrix[0])
        if n != m:
            return False  # 非方阵不可逆

        # 如果矩阵是1x1矩阵，直接判断是否为零
        if n == 1:
            return matrix[0][0] != 0

        # 对于大于1x1的矩阵，计算行列式
        determinant = self.calculate_determinant(matrix)

        return determinant != 0

    def calculate_determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for col in range(n):
            submatrix = []
            for row in range(1, n):
                subrow = []
                for j in range(n):
                    if j != col:
                        subrow.append(matrix[row][j])
                submatrix.append(subrow)
            determinant += matrix[0][col] * \
                ((-1) ** col) * self.calculate_determinant(submatrix)

        return determinant

    def print_format_matrix(self, matrix):
        # 确定每列的最大宽度，以便对齐
        max_widths = [max([len(f"{row[i]:.2f}") for row in matrix])
                      for i in range(len(matrix[0]))]

        formatted_matrix = []
        for row in matrix:
            formatted_row = [f"{value:.2f}".rjust(
                max_widths[i]) for i, value in enumerate(row)]
            formatted_matrix.append(" ".join(formatted_row))

        print("\n".join(formatted_matrix))

    def main(self):
        # 从文件读取矩阵
        matrix_filename = input("请输入矩阵文件名：")
        self.matrix = self.read_matrix_from_file(matrix_filename)

        # 检查矩阵是否可逆
        if not self.is_invertible():
            print("矩阵不可逆")
            return

        # 求逆矩阵
        inverse_matrix = self.invert_matrix()

        # 将逆矩阵写入文件
        self.write_matrix_to_file(inverse_matrix, "matrix.out")

        # 打印逆矩阵
        print("逆矩阵：")
        self.print_format_matrix(inverse_matrix)


if __name__ == "__main__":
    matrix_inverter = MatrixInverter()
    matrix_inverter.main()
