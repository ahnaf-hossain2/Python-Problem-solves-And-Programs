try:
    with (
        open("Python-Problem-solves-And-Programs/Code With Harry/this.txt", "r") as f1,
        open("Python-Problem-solves-And-Programs/Code With Harry/that.txt", "r") as f2,
    ):
        content1 = f1.read()
        content2 = f2.read()
        print(content1)
        print(content2)
except Exception as e:
    print(e)
