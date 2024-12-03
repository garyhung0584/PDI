def parse_input():
    n = int(input())
    m = int(input())
    matrix_a = list(map(int, input().split()))
    matrix_b = list(map(int, input().split()))
    selected_numbers = list(map(int, input().split()))
    return n, m, matrix_a, matrix_b, selected_numbers


def build_matrix(n, flat_matrix):
    return [flat_matrix[i * n : (i + 1) * n] for i in range(n)]


def count_lines(matrix, selected_numbers):
    n = len(matrix)
    marked = [[num in selected_numbers for num in row] for row in matrix]

    lines = 0

    # Check rows
    for row in marked:
        if all(row):
            lines += 1

    # Check columns
    for col in range(n):
        if all(marked[row][col] for row in range(n)):
            lines += 1

    # Check diagonals
    if all(marked[i][i] for i in range(n)):
        lines += 1
    if all(marked[i][n - i - 1] for i in range(n)):
        lines += 1

    return lines


def main():
    n, m, matrix_a_flat, matrix_b_flat, selected_numbers = parse_input()

    matrix_a = build_matrix(n, matrix_a_flat)
    matrix_b = build_matrix(n, matrix_b_flat)

    lines_a = count_lines(matrix_a, selected_numbers)
    lines_b = count_lines(matrix_b, selected_numbers)

    if lines_a > lines_b:
        print("A Win")
    elif lines_b > lines_a:
        print("B Win")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
