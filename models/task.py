class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    # 標記成功
    def mark_done(self):
        self.done = True
    # 標記未完成

    def mark_not_done(self):
        self.done = False

    # 顯示狀態

    def __str__(self):
        if self.done:
            status = "✓"
        else:
            status = "❌"
        return f"{self.id} . {self.title} is {status}"
