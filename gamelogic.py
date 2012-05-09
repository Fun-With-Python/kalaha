import outputgametable as out
def next(now):
	flag = 0
	for k, v in out.score.items():
		if flag:
			return k
		flag = k == now

out.score["U0"] = 5
out.output()
