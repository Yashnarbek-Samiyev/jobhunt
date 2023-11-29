# Job Hunt App

## Overview

The Job Hunt app is a [Django](https://www.djangoproject.com/) project designed to streamline the job application process. It provides features for managing job listings, user profiles, news updates, comments, and applicant details.

## Features

- **Job Listings:** Post and manage job opportunities.
- **User Profiles:** Create and customize user profiles.
- **Skills:** Define and list required skills for job listings.
- **Applicant Management:** Track and review job applications.
- **News and Comments:** Share updates and engage in discussions.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Yashnarbek-Samiyev/jobhunt.git
    ```

2. Navigate to the project directory:

    ```bash
    cd jobhunt
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to populate the database.

8. Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and log in with the superuser account.

## Usage

1. **Job Listings:**
   - Navigate to the "Job Listings" section to view and manage job opportunities.
   - Create new job listings, specifying the title, description, company, skills, and deadline.

2. **User Profiles:**
   - Customize your user profile by navigating to the "User Profile" section.
   - Add a bio and upload a profile picture.

3. **Skills:**
   - Define and manage required skills in the "Skills" section.

4. **Applicant Management:**
   - Track job applications in the "Applicants" section.
   - View details of applicants, including their cover letter and resume.

5. **News and Comments:**
   - Share updates and news in the "News" section.
   - Engage in discussions by adding comments.

## Contributing

Contributions are welcome! If you'd like to contribute to the development of the Job Hunt app, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the [UIC Group].

---

Happy job hunting! 🚀
