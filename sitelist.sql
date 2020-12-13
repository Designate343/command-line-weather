CREATE TABLE site (
    site_id INT(11) NOT NULL PRIMARY KEY,
    site_name VARCHAR(63) NOT NULL,
    site_region VARCHAR(2) NOT NULL,
    site_unitary_auth_area VARCHAR(31) NOT NULL,
    site_longitude DECIMAL(11) NOT NULL,
    site_latitude DECIMAL(11) NOT NULL,
    INDEX site_name_index(site_name)
);