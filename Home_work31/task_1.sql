-- 1. Вывести имя, фамилию, номер и название отдела для каждого сотрудника
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name
FROM
    employees e
JOIN
    department d ON e.department_id = d.department_id;

-- 2. Вывести имя, фамилию, отдел, город и штат/провинцию для каждого сотрудника
SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    l.state_province
FROM
    employees e
JOIN
    department d ON e.department_id = d.department_id
JOIN
    locations l ON d.location_id = l.location_id;

-- 3. Вывести имя, фамилию, номер и название отдела для всех сотрудников отделов 80 или 40
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name
FROM
    employees e
JOIN
    department d ON e.department_id = d.department_id
WHERE
    e.department_id IN (80, 40);

-- 4. Вывести все отделы, включая те, где нет сотрудников
SELECT
    d.department_id,
    d.department_name
FROM
    department d
LEFT JOIN
    employees e ON d.department_id = e.department_id;

-- 5. Вывести имя всех сотрудников, включая имя их менеджера
SELECT
    e.first_name AS "Имя сотрудника",
    m.first_name AS "Имя менеджера"
FROM
    employees e
LEFT JOIN
    employees m ON e.manager_id = m.employee_id;

-- 6. Вывести должность, полное имя (имя и фамилия) сотрудника и разницу между максимальной зарплатой для должности и зарплатой сотрудника
SELECT
    j.job_title,
    e.first_name || ' ' || e.last_name AS "Полное имя",
    (MAX(j.max_salary) OVER (PARTITION BY j.job_id) - e.salary) AS "Разница в зарплате"
FROM
    employees e
JOIN
    jobs j ON e.job_id = j.job_id;

-- 7. Вывести должность и среднюю зарплату сотрудников
SELECT
    j.job_title,
    AVG(e.salary) AS "Средняя зарплата"
FROM
    employees e
JOIN
    jobs j ON e.job_id = j.job_id
GROUP BY
    j.job_title;

-- 8. Вывести полное имя (имя и фамилия) и зарплату тех сотрудников, которые работают в любом отделе, расположенном в Лондоне
SELECT
    e.first_name || ' ' || e.last_name AS "Полное имя",
    e.salary
FROM
    employees e
JOIN
    departments d ON e.department_id = d.department_id
JOIN
    locations l ON d.location_id = l.location_id
WHERE
    l.city = 'London';

-- 9. Вывести название отдела и количество сотрудников в каждом отделе
SELECT
    d.department_name,
    COUNT(e.employee_id) AS "Количество сотрудников"
FROM
    department d
LEFT JOIN
    employees e ON d.department_id = e.department_id
GROUP BY
    d.department_name;

-- ОБЪЯСНЕНИЕ ЗАПРОСОВ В БАЗУ SQLITE -> G:\Мой диск\Обучение\Beetroot Academy\Информация