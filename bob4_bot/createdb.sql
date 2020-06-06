create table answers(
    id integer primary key,
    question_id integer,
    ans_text varchar(255)
);

create table users(
    id integer primary key,
    user_selfie_path varchar(255),
    user_id integer,
);


