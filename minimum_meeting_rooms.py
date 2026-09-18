def minMeetingRooms(meetingTimings: list[list[int]]) -> int:

    current_rooms = 0
    max_rooms = 0

    starts = []
    ends = []

    for meeting in meetingTimings:
        start_time = meeting[0] 
        end_time = meeting[1]

        starts.append(start_time)
        ends.append(end_time) 

    starts.sort()
    ends.sort()

    # At this point, we have 2 sorted lists of start and end times

    start_ptr = 0
    end_ptr = 0

    while start_ptr < len(starts):
        if starts[start_ptr] < ends[end_ptr]:
            current_rooms += 1
            start_ptr += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -=1
            end_ptr += 1

    return max_rooms

print(minMeetingRooms([
    [1, 4],
    [2, 5],
    [7, 9]
]))  # expected: 2

print(minMeetingRooms([
    [1, 4],
    [2, 3],
    [3, 5]
]))  # expected: 2

print(minMeetingRooms([
    [1, 10],
    [2, 3],
    [4, 5],
    [6, 7]
]))  # expected: 2

print(minMeetingRooms([
    [1, 2],
    [2, 3],
    [3, 4]
]))  # expected: 1

print(minMeetingRooms([
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 8]
]))  # expected: 4

print(minMeetingRooms([
    [5, 10],
    [1, 2],
    [3, 4]
]))  # expected: 1

print(minMeetingRooms([
    [1, 4],
    [1, 5],
    [5, 6],
    [6, 10],
    [7, 9]
]))  # expected: 2

print(minMeetingRooms([
    [1, 3]
]))  # expected: 1