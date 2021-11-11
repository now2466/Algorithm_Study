files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    from collections import deque
    new_files=[]
    
    for file in files:
        queue = deque(file)
        head=""
        while queue and not queue[0].isdigit():
            head+=queue.popleft()
        number = ""
        while queue[0].isdigit():
            number+=queue.popleft()
        tail=""
        while queue:
            tail+=queue.popleft()
        new_files.append([head,number,tail])
        


    new_files.sort(key = lambda x:[x[0][0].upper(),int(x[1])])
    
    answer = []
    for files in new_files:
        answer.append("".join(files))

    return answer


print(solution(files))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
