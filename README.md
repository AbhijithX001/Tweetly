# Tweetly

A Django-based social networking application where users can share posts, upload images, interact through likes and comments, and manage personalized profiles.

![Django](https://img.shields.io/badge/Django-5.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Cloudinary](https://img.shields.io/badge/Cloudinary-Media-orange)

---

## About

Tweetly is a Twitter-inspired social media platform that demonstrates core social networking features. Users can create accounts, publish posts with text and images, engage through likes and comments, and customize their profiles. The application is deployed on Railway using PostgreSQL and Cloudinary for media storage.

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
- Responsive design using Django templates
- Home feed displaying recent tweets
- Individual profile and tweet detail pages

---

## Tech Stack

**Backend**
- Django 5.x with Python 3.x
- PostgreSQL (Production) / SQLite (Development)
- Django ORM for database operations

**Media Storage**
- Cloudinary for image hosting

**Deployment**
- Railway platform
- Gunicorn WSGI server
- WhiteNoise for static files

**Frontend**
- Django Templates with HTML5 and CSS3

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git
- Cloudinary account

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
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
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
3. Add to `.env` file

### Database Configuration

**Development:**
Uses SQLite by default

**Production:**
Configure PostgreSQL connection string in `DATABASE_URL` environment variable

---

## How It Works

### Tweet Creation Flow
1. User logs in and accesses home page
2. User writes text and optionally selects an image
3. Form sends data to Django backend
4. Django validates authentication and saves tweet
5. Image uploads to Cloudinary, URL stored in database
6. Tweet appears in feed immediately

### Like System
- Many-to-Many relationship between Users and Tweets
- Toggle functionality: add or remove like on click
- Real-time count updates

### Comment System
- Comments belong to tweets via foreign key
- Replies use self-referential foreign key (parent comment)
- Templates render threaded discussions

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

### Railway Deployment

**Prepare for production**
```bash
pip install gunicorn dj-database-url psycopg2-binary whitenoise
pip freeze > requirements.txt
```

**Create Procfile**
```
web: gunicorn tweetly.wsgi --log-file -
```

**Configure production settings**
- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS`
- Set up PostgreSQL database URL
- Add Cloudinary credentials as environment variables

**Deploy**
1. Push code to GitHub
2. Connect repository to Railway
3. Add PostgreSQL database service
4. Set environment variables in Railway dashboard
5. Railway automatically deploys the application

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
- Railway for deployment platform
- PostgreSQL database
- Open-source community

---

**If you find this project useful, please give it a star on GitHub!**