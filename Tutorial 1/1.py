seconds = int(input())
hh = seconds // 3600
mm = (seconds % 3600) // 60
ss = seconds % 60
print(f"{hh:02}:{mm:02}:{ss:02}")
