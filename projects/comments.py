class Comment:
    def __init__(self, username, text, likes):
        self.username = username
        self.text = text
        self.likes = likes


comment1 = Comment('RingsKing',
                   'When you begin looking into abyss, abyss also begin looking to you',
                   10000000)

print('',comment1.username, '\n',comment1.text,'\n', comment1.likes)