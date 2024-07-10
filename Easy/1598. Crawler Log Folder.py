class Solution:
    def minOperations(self, logs: List[str]) -> int:
        print (logs)
        depth = 0
        for x in range (len(logs)):
            match logs[x]:
                case "../":
                    if depth > 0:
                        depth -= 1
                case "./":
                    continue
                case _:
                    depth+=1
        return depth