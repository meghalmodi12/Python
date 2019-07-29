def PrintStars(n):
    if n > 1:
        PrintStars(n - 1)
    content = ""
    for i in range(n):
        content = content + "*"
    print(content)

if __name__ == "__main__":
    PrintStars(5)