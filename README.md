# Tweetly

A Django-based social networking application where users can share posts, upload images, interact through likes and comments, and manage personalized profiles.

![Django](https://img.shields.io/badge/Django-5.2-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-blue)
![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-orange)

---

## About

Tweetly is a Twitter-inspired social media platform that demonstrates core social networking features. Users can create accounts, publish posts with text and images, engage through likes and comments, and customize their profiles. The application is deployed on Render using Supabase PostgreSQL and Cloudinary for media storage.

---

## Features

**User Management**
- Secure registration and authentication system
- Automatic profile creation with bio and profile picture support
- User-specific tweet timelines

**Content Creation**
- Create, edit, and delete tweets with text and images
- Image upload and hosting via Cloudinary
- Ownership-based permissions for content management

**Social Interactions**
- Like and unlike tweets with real-time count updates
- Comment on tweets with nested reply support
- Threaded discussion system

**User Interface**
- Responsive design using Bootstrap 5
- Home feed displaying recent tweets
- Individual profile and tweet detail pages

---

## Tech Stack

**Backend**
- Django 5.2 with Python 3.x
- PostgreSQL (Supabase) for production
- SQLite for local development
- Django ORM for database operations

**Media Storage**
- Cloudinary for image hosting

**Deployment**
- Render platform
- Gunicorn WSGI server
- WhiteNoise for static files

**Frontend**
- Django Templates with Bootstrap 5
- Custom CSS

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git
- Cloudinary account
- Supabase account (for production)

### Setup Steps

**Clone the repository**
```bash
git clone https://github.com/AbhijithX001/tweetly.git
cd tweetly
```

**Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Configure environment variables**

Create a `.env` file:
```env
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

**Run migrations and create superuser**
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Start development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`

---

## Configuration

### Cloudinary Setup
1. Sign up at [Cloudinary](https://cloudinary.com/)
2. Get credentials from Dashboard
3. Add `CLOUDINARY_URL` to `.env` file

### Database Configuration

**Development:**
Uses SQLite by default

**Production:**
Configure PostgreSQL connection string in `DATABASE_URL` environment variable:
```env
DATABASE_URL=postgresql://user:password@host:port/database
```

---

## Database Models

**User Model**
- Django's built-in User model with authentication

**Profile Model**
- One-to-one with User
- Fields: bio, profile_image, created_at
- Auto-created on user registration

**Tweet Model**
- Fields: user, text, photo, created_at, updated_at, likes
- Many-to-Many relationship for likes

**Comment Model**
- Fields: user, tweet, text, parent, created_at
- Self-referential foreign key for nested replies

---

## Deployment

### Render Deployment

**Prepare for production**
```bash
pip install gunicorn dj-database-url psycopg2-binary whitenoise
pip freeze > requirements.txt
```

**Create Procfile**
```
web: gunicorn tweetly_project.wsgi:application
```

**Configure production settings**
- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS` to include `.onrender.com`
- Set up Supabase PostgreSQL database URL
- Add Cloudinary credentials as environment variables

**Deploy**
1. Create a Supabase PostgreSQL database (free tier: 500MB)
2. Push code to GitHub
3. Connect repository to Render
4. Set environment variables in Render dashboard:
   - `DJANGO_SECRET_KEY`
   - `DATABASE_URL` (from Supabase)
   - `CLOUDINARY_URL`
   - `DEBUG=False`
5. Render automatically deploys the application

---

## Security

**Implemented measures:**
- Password hashing using Django's authentication system
- CSRF protection on all forms
- Login required decorators for protected views
- Ownership validation for edit/delete operations
- Environment variables for sensitive data
- XSS and SQL injection protection via Django defaults

---

## Future Enhancements

- Real-time notifications for interactions
- Direct messaging system
- Follow/follower functionality
- Hashtag and trending topics
- User mentions with @ functionality
- Tweet bookmarks and retweets
- Email verification and password reset
- Advanced search and filtering
- Mobile application
- Content moderation tools

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, commit your changes, and open a Pull Request with a detailed description.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

**Author:** Abhijith P

**GitHub:** [https://github.com/AbhijithX001](https://github.com/AbhijithX001)

**Email:** abhijith26p@gmail.com

**LinkedIn:** [https://www.linkedin.com/in/abhijith-p11/](https://www.linkedin.com/in/abhijith-p11/)

---

## Acknowledgments

- Django Framework documentation
- Cloudinary for media storage
- Supabase for PostgreSQL database
- Render for deployment platform
- Bootstrap 5 for UI components
- Open-source community

---

**Live Demo:** [https://tweetly-adhi.onrender.com](https://tweetly-adhi.onrender.com)

**If you find this project useful, please give it a star on GitHub!**
