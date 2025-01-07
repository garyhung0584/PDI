from collections import defaultdict
import math


def get_input():
    M = int(input("Enter number of courses: "))

    data = defaultdict(lambda: defaultdict(list))
    for _ in range(M):
        course_code, semester_code, student_count = input().split()
        student_count = int(student_count)
        students = []
        for _ in range(student_count):
            student_info = input().split()
            student_id = student_info[0]
            if student_info[1] == "w":
                semester_score = "w"
                exam_score = "w"
            else:
                semester_score = int(student_info[1])
                exam_score = int(student_info[2]) if len(student_info) > 2 else None
            students.append((student_id, semester_score, exam_score))
        data[course_code][semester_code].extend(students)

    search_course = input("Enter course code to search: ")
    return data, search_course


def calculate_course_scores(data):
    course_scores = defaultdict(lambda: defaultdict(list))
    for course_code, semesters in data.items():
        for semester_code, students in semesters.items():
            for student_id, semester_score, exam_score in students:
                if semester_score == "w":
                    continue
                if exam_score is not None:
                    final_score = math.ceil(semester_score * 0.7 + exam_score * 0.3)
                else:
                    final_score = semester_score
                course_scores[course_code][semester_code].append(
                    (student_id, final_score)
                )
    return course_scores


def calculate_student_annual_scores(data):
    student_scores = defaultdict(lambda: defaultdict(list))
    for course_code, semesters in data.items():
        for semester_code, students in semesters.items():
            year = semester_code[:3]
            for student_id, semester_score, exam_score in students:
                if semester_score == "w":
                    continue
                if exam_score is not None:
                    final_score = math.ceil(semester_score * 0.7 + exam_score * 0.3)
                else:
                    final_score = semester_score
                student_scores[student_id][year].append(final_score)
    return student_scores


def calculate_rank_percentage(total_students, rank):
    percentage = math.ceil((rank / total_students) * 100)
    return percentage


def calculate_drop_percentage(total_courses, dropped_courses):
    percentage = math.floor((dropped_courses / total_courses) * 100)
    return percentage


def process_data(data, search_course):
    course_scores = calculate_course_scores(data)
    student_scores = calculate_student_annual_scores(data)

    # Part 1: Output top 3 students for each department, year, and course year
    department_year_scores = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for student_id, years in student_scores.items():
        department = student_id[3:6]
        for year, scores in years.items():
            total_score = sum(scores) // len(scores)
            department_year_scores[department][student_id[:3]][year].append(
                (student_id, total_score)
            )

    for department, years in department_year_scores.items():
        for entry_year, courses in years.items():
            for course_year, students in courses.items():
                students.sort(key=lambda x: (-x[1], x[0]))
                print(f"{department} {entry_year} {course_year}")
                for rank, (student_id, score) in enumerate(students[:3], start=1):
                    rank_percentage = calculate_rank_percentage(len(students), rank)
                    drop_percentage = calculate_drop_percentage(
                        len(students), 0
                    )  # Assuming no drops for simplicity
                    print(f"{student_id} {score} {rank_percentage}% {drop_percentage}%")

    # Part 2: Output course statistics
    for course_code, semesters in course_scores.items():
        for semester_code, students in semesters.items():
            students.sort(key=lambda x: (-x[1], x[0]))
            highest_score = students[0][1]
            lowest_score = students[-1][1]
            average_score = sum(score for _, score in students) // len(students)
            drop_percentage = calculate_drop_percentage(
                len(students), 0
            )  # Assuming no drops for simplicity
            print(f"{course_code} {semester_code}")
            print(f"{highest_score} {average_score} {lowest_score} {drop_percentage}%")
            for rank, (student_id, score) in enumerate(students[:3], start=1):
                rank_percentage = calculate_rank_percentage(len(students), rank)
                print(f"{student_id} {score} {rank_percentage}%")

    # Part 3: Search for the course
    if search_course in course_scores:
        all_students = []
        for semester_code, students in course_scores[search_course].items():
            all_students.extend(students)
        all_students.sort(key=lambda x: (-x[1], x[0]))
        top_two_students = [student_id for student_id, _ in all_students[:2]]
        department_counts = defaultdict(int)
        for student_id, _ in all_students:
            department = student_id[3:6]
            department_counts[department] += 1
        most_common_department = max(department_counts.items(), key=lambda x: x[1])[0]
        print(f"{' '.join(top_two_students)} {most_common_department}")


def main():
    data, search_course = get_input()
    process_data(data, search_course)


if __name__ == "__main__":
    main()
