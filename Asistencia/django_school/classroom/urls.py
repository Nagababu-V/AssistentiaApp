from django.urls import include, path
from classroom.views import *
from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),
    path('index1/', classroom.index1, name='index1'),
    path('tpost_form_upload/', classroom.Tpost_form_upload, name='Tpost_form_upload'),

    path('OSpost_form_upload/', classroom.PrintOneStudent, name='PrintOneStudent'),

    path('gpost_form_upload/', classroom.Gpost_form_upload, name='Gpost_form_upload'),
    path('display/', classroom.index, name='index'),
    path('GGetClassDetails/', classroom.GClassDetails),
    path('GetAttendanceDetails/', classroom.Details),
    path('MarkAttendance/', classroom.MarkAttendance),
    path('ClassDetailsToMark/', classroom.GetClassDetailsToMark),
    path('allStudents/', classroom.AllStudents),
    path('individualStudent/', classroom.IndividualStudent),
    path('GetStudentDetails/', classroom.AllStudents),

    path('getDetails/oneStudent/', classroom.OneStudent),
    path('getDetails/allStudents/', classroom.AllStudents),

    path('takeAttendance/tpost_form_upload/', classroom.TClassDetails),

    #path('getDetails/oneStudent/', classroom.TClassDetails),

    path('getDetails/gpost_form_upload/', classroom.GClassDetails),


#/takeAttendance/tpost_form_upload/Tprint/

    path('takeAttendance/tpost_form_upload/Tprint/', classroom.TPrint),
    path('getDetails/gpost_form_upload/Gprint/', classroom.GPrint),
    #path('display/', classroom.index, name='index'),

    path('students/', include(([
        path('', students.StudentLogin.as_view()),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.TeachersLogin.as_view(), name='quiz_change_list'),
    ], 'classroom'), namespace='teachers')),
]
