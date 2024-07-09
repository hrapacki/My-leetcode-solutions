class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        n = len(customers)
        sum = 0
        wait_time = 0
        for x in range (len(customers)):
            if sum<=customers[x][0]:
                wait_time+=customers[x][1]
                sum = customers[x][0]+customers[x][1]
            else:
                wait_time += sum + customers[x][1] - customers[x][0]
                sum += customers[x][1]
            print(sum, wait_time)
        return wait_time/n