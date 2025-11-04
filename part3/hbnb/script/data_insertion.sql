INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `password`, `is_admin`) 
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$VHvQlCJp4u6r24DoZYk4EupWELP5kgVxSPr02D5oscNon7xxRA7/m',
    1
);

INSERT INTO `amenities` (`id`, `name`) 
VALUES
    ('4104a0cc-3128-4639-8cbf-ebe56a32b84a', 'Wifi'),
    ('910da42e-cf77-44d6-8383-18bcb192961c', 'Swimming Pool'),
    ('a0de5556-c903-49ee-8104-e9a77303c7fc', 'Air Conditioning'),
    ('1fcee8b6-64bc-461d-bb88-0f7697f3a920', 'Garden'),
    ('fd12747f-d73f-4f51-88f6-aff377faec9e', 'Terrace'),
    ('15650aed-dc4a-434e-af46-2771c5a4bf0a', 'Parking'),
    ('5fd71d38-851d-41c5-a530-34d2e44a2967', 'Washing Machine'),
    ('445bc912-6914-4802-b196-8815d4ded273', 'Coffee Machine'),
    ('ac97ecf8-d04a-4958-a31e-219f1729f3f6', 'Oven'),
    ('ffa60235-d7e4-40cb-910e-a00fe9cc22d4', 'TV');