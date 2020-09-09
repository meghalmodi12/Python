def NumToBinary(n):
    if n < 1:
        return
    
    NumToBinary(n/2)
    print(int(n%2))

if __name__ == "__main__":
    NumToBinary(8)