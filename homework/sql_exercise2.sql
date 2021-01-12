/**********************************************************
*	SQL Query & Function Example2
**********************************************************/
/**
-- Employees Table Columns
-- EMPLOYEE_ID
-- FIRST_NAME
-- LAST_NAME
-- EMAIL
-- PHONE_NUMBER
-- HIRE_DATE
-- JOB_ID
-- SALARY
-- COMMISSION_PCT
-- MANAGER_ID
-- DEPARTMENT_ID
**/

/**
--Departments Table Columns
--DEPARTMENT_ID
--DEPARTMENT_NAME
--MANAGER_ID
--LOCATION_ID
**/

/**
50�� �μ� ������ ��դ� �ְ�, ����, �ο����� ���Ͽ� ����϶�
**/
select round(avg(salary),0) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id) as number_of_employee
from employees
where department_id = 50;




/**
�� �μ��� �޿��� ���, �ְ�, ����, �ο����� ���Ͽ� ����϶�.
**/
select round(avg(salary),0) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id)
from employees
group by department_id;





/**
�� �μ��� ���� ������ �ϴ� ����� �ο����� ���Ͽ� �μ���ȣ, ������, �ο����� ����϶�.
**/
select d.department_id, d.department_name, count(e.employee_id)
from employees e, departments d
where e.department_id = d.department_id
group by d.department_id, d.department_name;




/**
���� ������ �ϴ� ����� ���� 4�� �̻��� ������ �ο����� ����϶�.
**/
select d.department_name, count(e.employee_id)
from departments d, employees e
group by d.department_name
having count(e.employee_id) >= 4;




/**
�� �μ��� ��տ���, ��ü����, �ְ����, ��������,�� ���Ͽ� ��տ����� ���������� ����϶�.
**/
select round(avg(salary),0) as avg_salary, sum(salary) as total_salary, max(salary) as max_salary, min(salary) as min_salary
from employees
group by department_id
order by avg(salary) desc;

/**
 �μ���ȣ, �μ���, �̸�, �޿��� ����϶�.
**/
select d.department_id, d.department_name, e.first_name, e.last_name, e.salary
from departments d, employees e
where d.department_id = e.department_id;

/**
�̸��� adam�� ����� �μ����� ����϶�.
**/
select d.department_name
from departments d, employees e
where e.department_id = d.department_id and e.first_name = 'Adam';

/**
employees���̺� �ִ� employee_id�� manager_id�� �̿��Ͽ� ������ ���踦 ������ ���� ����϶�
'smith'�� �Ŵ����� 'ford'�̴�.
**/
select e1.first_name || '�� �Ŵ����� ' || e2.first_name || '�̴�.' as info
from employees e1, employees e2
where e1.manager_id = e2.employee_id;


/**
adam�� ������ ���� ������ ���� ����� �̸�, �μ���, �޿�, ������ ����϶�.
**/
select e.first_name, e.last_name, d.department_name, e.salary, j.job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id;

/**
��ü ����� ��� �ӱݺ��� ���� ����� �����ȣ, �̸�, �μ���, �Ի���, ����, �޿��� ����϶�.
**/
select e.employee_id, e.first_name, e.last_name, d.department_name, e.hire_date, e.salary
from employees e, departments d
where d.department_id = e.department_id and e.salary >
(select avg(salary) from employees);

/**
50�� �μ������ �߿��� 30�� �μ��� ����� ���� ������ �ϴ� ����� �����ȣ, �̸�, �μ���, �Ի����� ����϶�.
**/
select e.employee_id, e.first_name, e.last_name, d.department_name, e.hire_date
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.department_id = 50 and j.job_id = e.job_id and j.job_title in
(
select j.job_title
from jobs j, employees e, departments d
where e.department_id = d.department_id and j.job_id = e.job_id and e.department_id = 30
);

/**
�޿��� 30�� �μ��� �ְ� �޿����� ���� ����� �����ȣ, �̸�, �޿��� ����϶�.
**/
select employee_id, first_name, last_name, salary
from employees
where salary >(
select max(salary) from employees
where department_id = 30
group by department_id
);