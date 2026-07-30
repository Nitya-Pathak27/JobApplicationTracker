from __init__ import app
from utils import login_required
from database.application_queries import (
    fetch_user_applications, get_dashboard_stats, add_new_application, delete_user_application, fetch_single_application, update_user_application, get_upcoming_deadlines
)
from flask import render_template, flash, session, request, redirect, url_for

# home route
@app.route('/')
def home_page():
    return render_template("home.html")

# dashboard route
@app.route('/dashboard')
@login_required
def dashboard_page():
    user_id = session['user_id']

    company = request.args.get('company')
    status = request.args.get('status')
    sort = request.args.get('sort')

    stats = get_dashboard_stats(user_id)

    # Fetch all applications for the user
    applications = fetch_user_applications(user_id, company, status, sort)
    
    # user data dictionary
    user = {
        "name" : session['user_name'],
        "total_applications" : stats['total_applications'],
        "applied" : stats['applied'],
        "interview_scheduled" : stats['interview_scheduled'],
        "selected" : stats['selected'],
        "rejected" : stats['rejected']
    }
    reminders = get_upcoming_deadlines(session['user_id'])
    
    return render_template("dashboard.html", user=user, applications=applications, reminders=reminders)

# add application route
@app.route('/add-application', methods = ['GET', 'POST'])
@login_required
def add_application():
    
    if request.method == 'POST':
        company = request.form.get('company')
        position = request.form.get('position')
        date = request.form.get('date')
        deadline = request.form.get('deadline')
        status = request.form.get('status')
        job_link = request.form.get('job_link')

        add_new_application(company, position, date, deadline, status, job_link, session['user_id'])
        

        flash("Application added successfully!", "success")
        return redirect(url_for('dashboard_page'))

    return render_template("add_application.html")

# view application route
@app.route('/view-applications')
@login_required
def view_applications():
    company = request.args.get('company')
    status = request.args.get('status')
    sort = request.args.get('sort')
    
    applications = fetch_user_applications(session['user_id'], company, status, sort)
    
    return render_template("view_applications.html", applications=applications)
 
# Delete route
@app.route('/delete-application/<int:application_id>')
@login_required
def delete_application(application_id):
    
    delete_user_application(application_id, session['user_id'])

    flash("Application deleted successfully!", "success")
    return redirect(url_for('dashboard_page'))

# Edit route
@app.route('/edit-application/<int:application_id>', methods = ['GET', 'POST'])
@login_required
def edit_application(application_id):
    application = fetch_single_application(application_id, session['user_id'])
    
    # If form submitted
    if request.method == 'POST':
        company = request.form.get('company')
        position = request.form.get('position')
        date = request.form.get('date')
        deadline = request.form.get('deadline')
        status = request.form.get('status')
        job_link = request.form.get('job_link')

        update_user_application(company, position, date, deadline, status, job_link, application_id, session['user_id'])
        

        flash("Application updated successfully!", "success")
        return redirect(url_for('dashboard_page'))
    
    return render_template("edit_application.html", application=application)