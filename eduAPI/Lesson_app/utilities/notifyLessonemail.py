from django.core.mail import send_mass_mail

def lesson_Notification(student_data):
    subject = 'New Lesson Added in Your Course!'
    email_messages = [
                    (
                    subject, 
                    f'''Hi {first_name}, 
                     We’re excited to let you know that a new lesson has just been added to your course, {course_name}! \n

                    To access the latest content, simply log in to your account and navigate to the course dashboard. \n

                    Happy learning!

                    Best Regards,
                    Prasad M.
                     ''' ,
                    None, 
                     [email]) 
                     for email, first_name,course_name in student_data]
    send_mass_mail(email_messages)