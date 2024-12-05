CREATE TABLE Timetable (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255),
    day VARCHAR(50),
    time VARCHAR(50),
    room VARCHAR(50),
    level INT
);

INSERT INTO Timetable (course_name, day, time, room, level) VALUES
('Computer Architecture', 'Monday', '02:00 PM - 04:20 PM', '-', 1),
('Principles of Programming', 'Monday', '04:30 PM - 06:50 PM', '-', 1),
('IT Project Management', 'Tuesday', '04:30 PM - 06:50 PM', '-', 2),
('Computer and Information', 'Thursday', '04:30 PM - 06:50 PM', '-', 2),
('Media Literacy', 'Friday', '02:00 PM - 04:20 PM', '-', 3),
('Media Writing', 'Friday', '04:30 PM - 06:50 PM', '-', 3);
