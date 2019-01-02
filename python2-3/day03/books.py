class Book:
    def __init__(self, title, author):
        '实例化时自动调用'
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》is written by %s.' % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('Core Python', 'Wesley')
    print(core_py)   # 调用__str__方法
    core_py()   # 调用__call__方法
