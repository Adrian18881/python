from collections import deque

#創建一個空的隊列
snack_queue = deque()

#向隊列中加入 人
snack_queue.append("小名")
snack_queue.append("小華")
snack_queue.append("小強")

print(f"初始隊列:{snack_queue}")

#第一個人購買點心並離開隊列
first_student = snack_queue.popleft()
print(f"{first_student}已購買點心並離開隊列")
print(f"現在的隊列:{snack_queue}")

#新的人加入隊列
snack_queue.append("小美")
print(f"小美加入隊列。")

print(f"最終隊列:{snack_queue}")
