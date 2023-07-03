def schedule_seminars(T, a):
    n = len(a)  # 세미나 개수

    # 가능한 모든 세미나 일정 탐색
    best_day = None  # 세미나 수가 가장 많은 날의 세미나 수
    best_schedule = None  # 최적의 세미나 일정

    for start_day in range(1, T + 1):
        schedule = []  # 세미나 일정
        seminar_count = 0  # 세미나 수가 가장 많은 날의 세미나 수

        for i in range(n):
            # 세미나 일정 계산
            seminar_day = (start_day + i - 1) % T + 1
            if seminar_day == a[i]:
                seminar_count += 1
            schedule.append(seminar_day)

        if best_day is None or seminar_count < best_day:
            best_day = seminar_count
            best_schedule = schedule

    return best_schedule

# 입력 예시
T = 3
a = [4, 6, 3, 5, 7]
#a = [5, 5, 5]
# 세미나 일정 계산
seminar_schedule = schedule_seminars(T, a)

# 결과 출력
print("각 세미나의 일정:", seminar_schedule)
print("세미나 수가 가장 많은 날의 세미나 수:", max(seminar_schedule.count(day) for day in seminar_schedule))
