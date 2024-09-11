from app import database, Course

course1 = Course(
    title = 'Python for Everybody',
    course_provider = 'Coursera',
    description = 'This specialization introduces fundamental programming concepts including data structures, networked application program interfaces, and databases, using the Python programming language.',
    time_to_complete = 'Approximately 8 months (at 3 hours per week)',
    link = 'www.coursera.org/specializations/python'
)
course2 = Course(
    title = 'CS50\'s Introduction to Computer Science',
    course_provider = 'edX (Harvard University)',
    description = 'This is an entry-level course taught by Harvard University that covers fundamental concepts in computer science and programming. It uses languages like C, Python, SQL, and more.',
    time_to_complete = '11 weeks (at 10-20 hours per week).',
    link = 'https://cs50.harvard.edu/x/2024/'
)
course3 = Course(
    title = 'Introduction to Data Science',
    course_provider = 'Udacity',
    description = 'This course introduces you to data science and covers the basics of data wrangling, data analysis, and machine learning with Python.',
    time_to_complete = 'Approximately 2 months (at 5-10 hours per week).',
    link = 'https://udacity.com'
)
course4 = Course(
    title = 'Front-End Web Development with React',
    course_provider = 'Coursera',
    description = 'This course covers front-end development using the React library. It teaches how to build powerful, scalable web applications.',
    time_to_complete = 'Approximately 4 weeks (at 6-8 hours per week).',
    link = 'https://coursera.org'
)

course5 = Course(
    title = 'Machine Learning',
    course_provider = 'Coursera',
    description = 'This course provides a broad introduction to machine learning, data mining, and statistical pattern recognition.',
    time_to_complete = 'Approximately 11 weeks (at 5-7 hours per week)',
    link = 'https://www.coursera.org/learn/machine-learning'
)
course6 = Course(
    title = 'Full Stack Web Development',
    course_provider = 'Udemy',
    description = 'This course covers HTML, CSS, JavaScript, Node.js, and Express.js, offering a beginner-level introduction to full-stack web development.',
    time_to_complete = ' 27 hours (self-paced)',
    link = 'https://udemy.com'
)
course7 = Course(
    title = 'Digital Marketing Fundamentals',
    course_provider = 'Google Digital Garage',
    description = 'This course covers the basics of digital marketing, including SEO, SEM, social media marketing, and web analytics.',
    time_to_complete = 'Approximately 40 hours',
    link = 'https://'
)
course8 = Course(
    title = 'Introduction to HTML and CSS',
    course_provider = 'Udacity',
    description = 'This course introduces you to HTML and CSS, the core technologies for building web pages.',
    time_to_complete = '3 weeks (self-paced).',
    link = 'https://udacity.com'
)
course9 = Course(
    title = 'The Science of Well-Being',
    course_provider = 'Cousera',
    description = 'This course teaches how to increase your own happiness and build more productive habits.',
    time_to_complete = 'Approximately 10 weeks (at 1-2 hours per week).',
    link = 'https://www.coursera.org/learn/the-science-of-well-being'
)
course10 = Course(
    title = 'Introduction to Artificial Intelligence (AI)',
    course_provider = 'University of Helsinki and Reaktor',
    description = 'This course introduces the basics of artificial intelligence, exploring what AI is and how it impacts our daily lives.',
    time_to_complete = '6 weeks (self-paced).',
    link = 'https://www.elementsofai.com/'
)
course11 = Course(
    title = 'Responsive Web Design',
    course_provider = 'freeCodeCamp',
    description = 'This course covers the fundamentals of web design, including how to make responsive, mobile-friendly websites.',
    time_to_complete = 'Approximately 300 hours (self-paced).',
    link = 'https://freeCodeCamp.com'
)
course12 = Course(
    title = 'Financial Markets',
    course_provider = 'Cousera',
    description = 'This course covers the basics of financial markets and is taught by Nobel laureate Robert Shiller.',
    time_to_complete = 'Approximately 7 weeks (at 8-10 hours per week).',
    link = ''
)
course13 = Course(
    title = 'Introduction to Cyber Security',
    course_provider = 'Udacity',
    description = 'Learn the basics of cybersecurity and how to protect networks and data from threats.',
    time_to_complete = 'Approximately 8 weeks (self-paced).',
    link = 'https://udacity'
)
course14 = Course(
    title = 'Learning How to Learn',
    course_provider = 'Cousera',
    description = 'Learn the techniques used by experts in various disciplines to master tough subjects and gain knowledge efficiently.',
    time_to_complete = 'Approximately 4 weeks (at 2-3 hours per week).',
    link = 'https://www.coursera.org/learn/learning-how-to-learn'
)

database.session.add_all([course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14,])
database.session.commit()