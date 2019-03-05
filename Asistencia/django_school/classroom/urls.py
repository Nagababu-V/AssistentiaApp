from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),

    path('display/', classroom.index, name='index'),
    path('GetClassDetails/', classroom.ClassDetails),
    path('GetAttendnaceDetails/', classroom.Details),
    path('MarkAttendance/', classroom.MarkAttendance),
    path('ClassDetailsToMark/', classroom.GetClassDetailsToMark),
    path('allStudents/', classroom.AllStudents),
    path('individualStudent/', classroom.IndividualStudent),
    path('GetStudentDetails/', classroom.IndividualStudent),
    #path('display/', classroom.index, name='index'),

    path('students/', include(([
        path('', students.StudentLogin.as_view()),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.TeachersLogin.as_view(), name='quiz_change_list'),
    ], 'classroom'), namespace='teachers')),
]
