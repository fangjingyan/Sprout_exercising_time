class CountTime:
    def exercise_time(self, ts, hr, min_hr, interval=120):
        '''
        :param ts: time step after midnight
        :param hr: corresponding heart rate
        :param min_hr: the minial heart rate for exercising
        :param interval: the maximum interval allowing the user to take off the watch
        :return: total exercising time
        '''
        # the length of the array
        n = len(ts)
        res = 0
        i = 0
        while i < n:
            # find the start index of potential exercising time in ts array
            while i < n and hr[i] < min_hr:
                i += 1
            j = i + 1
            while j < n:
                if hr[j] >= min_hr and ts[j] - ts[j - 1] <= interval:
                    res += ts[j] - ts[j - 1]
                    j += 1
                else:
                    break
            i = j
        return res

    def exercise_time_simplified(self, ts, hr, min_hr, interval=120):
        '''
        :param ts: time step after midnight
        :param hr: corresponding heart rate
        :param min_hr: the minial heart rate for exercising
        :param interval: the maximum interval allowing the user to take off the watch
        :return: total exercising time
        '''
        # the length of the array
        n = len(ts)
        res = 0
        in_interval = False
        for i in range(n):
            if hr[i] < min_hr:
                in_interval = False
            else:
                if not in_interval:
                    in_interval = True
                else:
                    if ts[i] - ts[i - 1] <= interval:
                        res += ts[i] - ts[i - 1]

        return res