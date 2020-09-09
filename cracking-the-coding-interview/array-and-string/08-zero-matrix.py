class ZeroMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def nullifyRow(self, row):
        self.matrix[row] = [0] * len(self.matrix[row])

    def nullifyColumn(self, col):
        for i in range(len(self.matrix)):
            self.matrix[i][col] = 0

    def apply(self):
        rows = []
        cols = []

        for m in range(len(self.matrix)):
            for n in range(len(self.matrix[m])):
                if self.matrix[m][n] == 0:
                    rows.append(m)
                    cols.append(n)

        for row in rows:
            self.nullifyRow(row)

        for col in cols:
            self.nullifyColumn(col)

        return self.matrix