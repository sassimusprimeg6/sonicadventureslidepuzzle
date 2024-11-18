import random

class SlidePuzzle:
    def __init__(self, size):
        self.size = size
        self.board = self.create_board()
        self.empty = (size - 1, size - 1)
        self.shuffle_board()

    def create_board(self):
        return [[self.size * r + c + 1 for c in range(self.size)] for r in range(self.size)]

    def shuffle_board(self):
        n = self.size * self.size
        tiles = list(range(1, n)) + [0]
        random.shuffle(tiles)
        for r in range(self.size):
            for c in range(self.size):
                self.board[r][c] = tiles.pop(0)
        self.find_empty_tile()

    def find_empty_tile(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    self.empty = (r, c)

    def display_board(self):
        for row in self.board:
            print(' '.join(f"{tile:2}" if tile != 0 else "  " for tile in row))

    def move(self, tile):
        r, c = [(r, c) for r, row in enumerate(self.board) for c, val in enumerate(row) if val == tile][0]
        er, ec = self.empty

        if abs(r - er) + abs(c - ec) == 1:
            self.board[er][ec], self.board[r][c] = self.board[r][c], self.board[er][ec]
            self.empty = (r, c)

    def is_solved(self):
        count = 1
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] != count % (self.size * self.size):
                    return False
                count += 1
        return True

def main():
    size = 4
    puzzle = SlidePuzzle(size)
    while True:
        puzzle.display_board()
        if puzzle.is_solved():
            print("Congratulations! You solved the puzzle.")
            break
        move = int(input("Enter tile to move (0 to exit): "))
        if move == 0:
            break
        puzzle.move(move)

if __name__ == "__main__":
    main()
