import json

def decode_value(base, value):
    return int(value, base)

def matrix_elimination(matrix, results):
    n = len(matrix)
    for i in range(n):
        matrix[i].append(results[i])
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            matrix[k][n] -= matrix[k][i] * solution[i]
    
    return solution

def process_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    n = data['keys']['n']
    k = data['keys']['k']

    points = []
    for key in data:
        if key != 'keys':
            x = int(key)
            base = int(data[key]['base'])
            y_encoded = data[key]['value']
            y = decode_value(base, y_encoded)
            points.append((x, y))

    points = points[:k]

    matrix = []
    results = []
    for x, y in points:
        row = [x ** i for i in range(k)]
        matrix.append(row)
        results.append(y)

    coefficients = matrix_elimination(matrix, results)
    
    c = coefficients[0]
    
    return int(c)

def main():
    c1 = process_file('input1.json')
    c2 = process_file('input2.json')

    print("The constant term (c) from input1.json is:", c1)
    print("The constant term (c) from input2.json is:", c2)

if __name__ == "__main__":
    main()
