from db import cursor, db
from datetime import date

# It will detch applications for a specific user
def fetch_user_applications(user_id, company=None, status=None, sort=None):
    query = """
    SELECT * FROM applications WHERE user_id = %s
    """
    params = [user_id]

    # Search
    if company:
        query += " AND (company LIKE %s OR position LIKE %s)"
        params.append(f"%{company}%")
        params.append(f"%{company}%")

    # Filter
    if status:
        query += " AND status = %s"
        params.append(status)

    # Sort
    if sort == "date_desc":
        query += " ORDER BY date DESC"
    elif sort == "date_asc":
        query += " ORDER BY date ASC"
    elif sort == "company_az":
        query += " ORDER BY company ASC"
    elif sort == "company_za":
        query += " ORDER BY company DESC"
    else:
        query += " ORDER BY date DESC"


    cursor.execute(query, tuple(params))
    applications = cursor.fetchall()
    return applications

# For dashboard stats
def get_dashboard_stats(user_id):
    # Total applications
    total_query = """
    SELECT COUNT(*) FROM applications WHERE user_id = %s
    """
    cursor.execute(total_query, (user_id,))
    total_applications = cursor.fetchone()[0]   

    # Status count query
    status_query = """
    SELECT COUNT(*) FROM applications WHERE status = %s AND user_id = %s
    """

    # Applied count
    cursor.execute(status_query, ("applied", user_id))
    applied = cursor.fetchone()[0]

    # Interview scheduled count
    cursor.execute(status_query, ("interview_scheduled", user_id))
    interview_scheduled = cursor.fetchone()[0]

    # Selected count
    cursor.execute(status_query, ("selected", user_id))
    selected = cursor.fetchone()[0]

    # Rejected count
    cursor.execute(status_query, ("rejected", user_id))
    rejected = cursor.fetchone()[0]

    stats = {
        "total_applications" : total_applications,
        "applied" : applied,
        "interview_scheduled" : interview_scheduled,
        "selected" : selected,
        "rejected" : rejected
    }
    return stats

# for application addition
def add_new_application(company, position, date, deadline, status, job_link, user_id):
    query = """
        INSERT INTO applications (company, position, date, deadline, status, job_link, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s)
        """

    values = (company, position, date, deadline, status, job_link, user_id)
    cursor.execute(query, values)
    db.commit()

# for deleting user application
def delete_user_application(application_id, user_id):
    query = """
    DELETE FROM applications WHERE user_id = %s AND id = %s
    """
    values = (user_id, application_id)
    cursor.execute(query, values)
    db.commit()

# fetch single application for editing
def fetch_single_application(application_id, user_id):
    # fetch current application date 
    query = """
    SELECT * FROM applications WHERE user_id = %s AND id = %s
    """
    values = (user_id, application_id)
    cursor.execute(query, values)
    application = cursor.fetchone()
    return application

# for editing user application
def update_user_application(company, position, date, deadline, status, job_link, application_id, user_id):
    update_query = """
        UPDATE applications SET
        company = %s,
        position = %s,
        date = %s,
        deadline = %s,
        status = %s,
        job_link = %s
        WHERE id = %s AND user_id = %s
        """

    update_values = (
            company,
            position,
            date,
            deadline,
            status,
            job_link,
            application_id,
            user_id
    )

    cursor.execute(update_query, update_values)
    db.commit()

# upcoming deadline
def get_upcoming_deadlines(user_id):

    query = """
    SELECT * FROM applications WHERE user_id = %s AND deadline >= CURDATE() AND status IN ('applied', 'interview_scheduled') ORDER BY deadline ASC LIMIT 3
    """
    cursor.execute(query, (user_id,))
    reminders = cursor.fetchall()

    today = date.today()

    updated_reminders = [app + ((app[4]-today).days,) for app in reminders]
    return updated_reminders