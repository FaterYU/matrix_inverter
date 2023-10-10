# Lab 2 Testing Report

## Data Reference 

- &#10004; Does a referenced variable have a value that is unset or uninitialized?
  - If there is a value that is unset or uninitialized in a python program, the python interpreter throws an exception. The tested code runs normally and does not throw an unset or uninitialised variable exception. So this test passes in this programme.
- &#10004; For all array references, is each subscript value within the defined bounds of the corresponding dimension?
  - If an array (list) reference is out of range in a python application, the python interpreter will throw an `IndexError: list index out of range` exception. The tested code runs normally and does not throw this exception. So this test passes in this programme.
- &#10004; For all array references, does each subscript have an integer value?
  - Checked by accessing subscripts through all lists in the code under test. The code contains both direct access to array references via integers and traversal using the `range()` function. They are both integers. So this test passes in this programme.
- **Not Applicable** For all references through pointer or reference variables, is the referenced memory currently allocated?
  - Memory allocation and access in python programs is done by the interpreter, there are no pointers to unallocated memory. So this test is not applicable to python program.
- **Not Applicable** When a memory area has alias names with differing attributes, does the data value in this area have the correct attributes when referenced via one of these names?
  - Memory allocation and access in python programs is done by the interpreter, and there are no variables that refer to memory directly through pointer variables. So this test is not applicable to python program.
- **Not Applicable** Does a variable’s value have a type or attribute other than what the compiler expects?
  - Python is a dynamically typed language, and the interpreter will automatically convert the type of the variable to the type required by the operation. So this test is not applicable to python program.
- **Not Applicable** Are there any explicit or implicit addressing problems if, on the computer being used, the units of memory allocation are smaller than the units of addressable memory?
  - Memory allocation and access in python programs is done by the interpreter, and there is no user-level memory allocation space discontinuity. So this test is not applicable to python program.
- **Not Applicable** If pointer or reference variables are used, does the referenced memory location have the attributes the compiler expects?
- **Not Applicable** If a data structure is referenced in multiple procedures or subroutines, is the structure defined identically in each procedure?
- &#10004; When indexing into a string, are the limits of the string off by one in indexing operations or in subscript references to arrays?
  - No strings exist in this program that need to be indexed. So this test passes in this programme.
- &#10004; For object-oriented languages, are all inheritance requirements met in the implementing class?
  - There is no inheritance for the classes in this programme. So this test passes in this programme.

## Data Declaration

- **Not Applicable** Have all variables been explicitly declared?
  - Python is a dynamically typed programming language, so you don't need to use the type keyword to declare the type of a variable when defining it, as you would in a statically typed programming language like C/C++.
- **Not Applicable** If all attributes of a variable are not explicitly stated in the declaration, are the defaults well understood?
  - In Python, variable attributes (such as data type and length) are determined dynamically, so there is no need to declare them explicitly.
- &#10004; Where a variable is initialized in a declarative statement, is it properly initialized?
  - Variables in the code are properly initialised when needed. For example, the `self.matrix` variable is initialised in the constructor.
- &#10004; Is each variable assigned the correct length and data type?
  - Python is a dynamically typed language, so the data types of variables are determined automatically based on the values assigned to them. The code handles data types correctly.
- **Not Applicable** Is the initialization of a variable consistent with its memory type?
- &#10004; Are there any variables with similar names (e.g., VOLT and VOLTS)?
  - This code does not have variables named similarly.

## Computation

- &#10004; Are there any computations using variables having inconsistent (such as nonarithmetic) data types?
  - Obviously inconsistent datatype calculations don't usually happen in Python because Python is a dynamically typed language that automatically performs type conversions based on operands. Therefore, upon inspection, this code does not have inconsistent datatype calculations.
- &#10008; Are there any mixed-mode computations?
  - Mixed-mode calculations are usually allowed in Python, but the results may change depending on the data type of the operand. For example, calculations between integers and floating-point numbers may cause precision problems, but this is not usually considered an error. Mixed-mode calculations exist in this code.
- **Not Applicable** Are there any computations using variables having the same data type but of different lengths?
  - In Python, you usually don't need to worry about calculations with data types of different lengths because it automatically does the type conversion to make the calculation valid. This situation exists in this code, but it is not considered an error.
- **Not Applicable** Is the data type of the target variable of an assignment smaller than the data type or a result of the right-hand expression?
  - In Python, it is usually not necessary to explicitly declare the data type of the target variable because Python automatically handles the type conversion to match the result of the expression on the right-hand side.
- **Not Applicable** Is an overflow or underflow expression possible during the computation of an expression?
  - Python usually handles overflows or underflows automatically and does not make errors when doing large integer or floating point calculations. It will automatically adjust data types as needed.
- &#10004; Is it possible for the divisor in a division operation to be zero?
  - There are no obvious cases of division by zero in the code.
- **Not Applicable** If the underlying machine represents variables in base-2 form, are there any sequences of the resulting inaccuracy?
  - In Python, there is usually a problem with decimal point precision because it is represented using binary floating point numbers. This is a common occurrence, but is not usually considered an error.
- &#10004; Where applicable, can the value of a variable go outside the meaningful range?
  - There are no obvious cases in the code where the value of a variable is outside a meaningful range.
- &#10004; For expressions containing more than one operator, are the assumptions about the order of evaluation and precedence of operators correct?
  - The code makes correct assumptions about order of evaluation and operator precedence.
- &#10004; Are there any invalid uses of integer arithmetic, particularly divisions?
  - This is not the case in the code.

## Comparison

- &#10004; Are there any comparisons between variables having different data types, such as comparing a character string to an address, date, or number?
  - In Python, variables of different data types are usually not explicitly compared, because Python tries to automatically perform type conversions to make the comparison. There are no cross-type comparisons in this code that would cause the python program to generate errors.
- &#10004; Are there any mixed-mode comparisons or comparisons between variables of different lengths?
  - There are no obvious mixed-mode comparisons or comparisons of different lengths in the code.
- &#10004; Are the comparison operators correct?
  - The comparison operator used in the code is correct.
- &#10004; Does each Boolean expression state what it is supposed to state?
  - Boolean expressions clearly express their intent in the code.
- **Not Applicable** Are the operands of a Boolean operator Boolean?
  - In Python, it is usually not necessary to explicitly declare Boolean types, because Boolean operations usually produce Boolean values.
- **Not Applicable** Are there any comparisons between fractional or floating-point numbers that are represented in base-2 by the underlying machine?
  - There may be floating-point precision issues in Python, which uses a binary floating-point representation, but this is a common occurrence and not necessarily an error.
- &#10004; For expressions containing more than one Boolean operator, are the assumptions about the order of evaluation and the precedence of operators correct?
  - This code does not contain expressions with multiple Boolean operators.
- &#10004; Does the way in which the compiler evaluates Boolean expressions affect the program?
  - In Python, there are usually no situations where the compiler evaluates Boolean expressions in a way that would cause a programme error; Python short-circuits evaluation, i.e., it does not evaluate the right-hand side expression if the left-hand side expression is `False` in an and operation. Thus, `if(x==0&&(x/y)>z)` in the code will not result in a divide-by-zero error because the right-hand side expression will not be evaluated if the left-hand side condition `x==0` is False. Compound Boolean expressions do not exist in this code.

## Control-Flow

- &#10004; If the program contains a multipath branch such as a computed GOTO, can the index variable ever exceed the number of branch possibilities?
  - There are no multipath branches or calculated GOTO statements in this code.
- &#10004; Will every loop eventually terminate?
  - According to the code, all loops have explicit termination conditions. Gauss-Jordan elimination and file read and write operations have termination conditions.
- &#10004; Will the program, module, or subroutine eventually terminate?
  - According to the code, operations in the main programme `main` will terminate under appropriate conditions. If there are no problems with file reading and writing, the programme will terminate normally.
- &#10004; Is it possible that, because of the conditions upon entry, a loop will never execute?
  - There is no situation in the code where the loop entry condition may never be satisfied. The format of the input file may affect whether or not the loop will be entered.
- &#10004; For a loop controlled by both iteration and a Boolean condition (e.g., a searching loop) what are the consequences of loop fall-through?
  - Explicit Boolean conditions are used in the code to control loops, such as the determinant non-zero check in the `is_invertible()` function.
- &#10004; Are there any off-by-one errors, such as one too many or too few iterations?
  - There are no obvious cases in the code where loop control depends on both the number of iterations and Boolean conditions.
- &#10004; If the language contains a concept of statement groups or code blocks (e.g., do-while or {...}), is there an explicit while for each group, and do the instances of do correspond to their appropriate groups?
  - There are no obvious looping logic flaws in the code, such as loops that never terminate or terminate early.
- &#10004; Are there any nonexhaustive decisions?
  - There are no obvious "one less" or "one more" errors in the code, and the loop boundaries are correct.

## Interface

- &#10004; Does the number of parameters received by this module equal the number of arguments sent by each of the calling modules?
  - According to the code, the number and order of arguments for each method and function is correct. For example, the `invert_matrix()` method takes an implicit argument called self, and the filename argument.
- &#10004; Do the attributes (e.g., data type and size) of each parameter match the attributes of each corresponding argument?
  - In the code, the parameters and the attributes (data type, size, etc.) of the arguments passed to methods and functions match. For example, the `read_matrix_from_file()` method expects a string parameter (filename) and reads matrix data of integer type.
- &#10004; Does the units system of each parameter match the units system of each corresponding argument?
  - There is no unit involved in the code.
- &#10004; Does the number of arguments passed by this module to another module equal the number of parameters expected by that module?
  - There is no mismatch in the code between the number of arguments received by modules or methods and the number of arguments passed to them. For example, the `write_matrix_to_file()` method expects two arguments, a matrix and a filename, and passes both when called.
- &#10004; Do the attributes of each argument passed to another module match the attributes of the corresponding parameter in that module?
  - According to the code, the parameters and the attributes (data types, sizes, etc.) of the parameters passed to the methods and functions match and there are no mismatches.
- &#10004; Does the units system of each argument passed to another module match the units system of the corresponding parameter in that module?
  - The system of units is not explicitly addressed in this code.
- &#10004; If built-in functions are invoked, are the number, attributes, and order of the arguments correct?
  - There are no built-in functions explicitly involved in this code.
- &#10004; If a module or class has multiple entry points, is a parameter ever referenced that is not associated with the current point of entry?
  - There is no explicit involvement of multiple entry points in this code.
- &#10004; Does a subroutine alter a parameter that is intended to be only an input value?
  - In this code parameter passing is correct.
- &#10004; If global variables are present, do they have the same definition and attributes in all modules that reference them?
  - There are no global variables involved in this code.
- &#10004; Are constants ever passed as arguments?
  - Passing constants as parameters is not addressed in this code.

## Input/Output

- &#10004; If files are explicitly declared, are their attributes correct?
  - Using with `open(filename, 'r')` as file to open a file in your code ensures that the file is automatically closed after use, which is good practice and avoids resource leakage issues.
- &#10004; Are the attributes on the file’s OPEN statement correct?
  - There is no explicit OPEN statement in the code because Python's `with open` statement already includes the operation of opening the file.
- &#10004; Does the format specification agree with the information in the I/O statement?
  - The code does not address the issue of format specification as it is primarily used to read and write matrix data and does not involve complex formatting.
- &#10004; Is sufficient memory available to hold the file your program will read?
  - The code doesn't explicitly check memory usage, but it uses sensible memory management practices when reading files and processing matrix data, and usually doesn't cause problems due to out-of-memory.
- &#10004; Have all files been opened before use?
  - In the file read and write operations, the code uses the `with open` statement, which means that the file is automatically closed after use, thus following the principle that you must close the file after opening it.
- &#10004; Have all files been closed after use?
  - In the file read and write operations, the code uses the `with open` statement, which means that the file is automatically closed after use, thus following the principle that you must close the file after opening it.
- &#10008; Are end-of-file conditions detected and handled correctly?
  - The code doesn't explicitly handle the logic of the EOF condition, but in Python, the `EOFError` exception is automatically raised when the file is read to the end, which can be caught and handled if needed.
- &#10008; Are I/O error conditions handled correctly?
  - The code has no logic to explicitly handle I/O error conditions, but if an I/O error occurs during a file read or write, Python raises the appropriate exception (e.g., `IOError`), which can be caught and handled when needed.
- &#10004; Are there spelling or grammatical errors in any text that is printed or displayed by the program?
  - There are no obvious spelling or grammatical errors in the code.
- &#10008; Does the program properly handle "File not Found" errors?
  - The code does not handle file not found errors.

## Other Checks

- &#10004; If the compiler produces a cross-reference listing of identifiers, examine it for variables that are never referenced or are referenced only once.
  - In this code, there are no obvious unreferenced variables, most of them are used, and every function and method is called.
- &#10004; If the compiler produces an attribute listing, check the attributes of each variable to ensure that no unexpected default attributes have been assigned.
  - In this code, there is no obvious assignment of incorrect attributes.
- **Not Applicable** If the program compiled successfully, but the computer produced one or more "warning" or "informational" messages, check each one carefully.
  - Python does not normally generate compilation warnings or messages. Errors and warning messages are generated at runtime. If there is a potential problem in the code, such as a file that does not exist or a matrix that is not reversible, Python raises the relevant exception at runtime instead of generating a warning at compile time.
- &#10004; Is the program or module sufficiently robust? That is, does it check its input for validity?
  - The code does do some robustness checks when reading the file and processing the matrix data, such as checking that the matrix is square and checking that the matrix is invertible. 
- &#10004; Is a function missing from the program?
  - There are no obvious missing functions in this code, as all operations are defined in the MatrixInverter class.

## Testing program

```python
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

```
