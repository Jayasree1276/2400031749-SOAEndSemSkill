CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO items (name, description) VALUES
    ('Item One',   'First record from app-db'),
    ('Item Two',   'Second record from app-db'),
    ('Item Three', 'Third record from app-db');
