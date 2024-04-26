src=input()
dst=input()
def func():
    if dst not in src:
        print(-1)
        return
    else:
        for idx in range(len(src)-len(dst)+1):
            cnt=0
            for dst_idx in range(len(dst)):
                if dst[dst_idx]==src[idx+dst_idx]:
                    cnt+=1
            if cnt==len(dst):
                print(idx)
                return

func()