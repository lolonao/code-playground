import MeCab

t = MeCab.Tagger()
node = t.parseToNode('私はペンを持っています')

while node:
    # print(node.feature)
    print("---")

    f = node.feature
    p = f.split(',')[0]
    breakpoint()
    if p == '名詞':
        print(node.surface)
    node = node.next
    
    
