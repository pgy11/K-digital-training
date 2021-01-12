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
50번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
select round(avg(salary),0) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id) as number_of_employee
from employees
where department_id = 50;




/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
select round(avg(salary),0) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id)
from employees
group by department_id;





/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
select d.department_id, d.department_name, count(e.employee_id)
from employees e, departments d
where e.department_id = d.department_id
group by d.department_id, d.department_name;




/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
select d.department_name, count(e.employee_id)
from departments d, employees e
group by d.department_name
having count(e.employee_id) >= 4;




/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
select round(avg(salary),0) as avg_salary, sum(salary) as total_salary, max(salary) as max_salary, min(salary) as min_salary
from employees
group by department_id
order by avg(salary) desc;

/**
 부서번호, 부서명, 이름, 급여를 출력하라.
**/
select d.department_id, d.department_name, e.first_name, e.last_name, e.salary
from departments d, employees e
where d.department_id = e.department_id;

/**
이름이 adam인 사원의 부서명을 출력하라.
**/
select d.department_name
from departments d, employees e
where e.department_id = d.department_id and e.first_name = 'Adam';

/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하라
'smith'의 매니저는 'ford'이다.
**/
select e1.first_name || '의 매니저는 ' || e2.first_name || '이다.' as info
from employees e1, employees e2
where e1.manager_id = e2.employee_id;


/**
adam의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하라.
**/
select e.first_name, e.last_name, d.department_name, e.salary, j.job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id;

/**
전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
**/
select e.employee_id, e.first_name, e.last_name, d.department_name, e.hire_date, e.salary
from employees e, departments d
where d.department_id = e.department_id and e.salary >
(select avg(salary) from employees);

/**
50번 부서사람들 중에서 30번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하라.
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
급여가 30번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하라.
**/
select employee_id, first_name, last_name, salary
from employees
where salary >(
select max(salary) from employees
where department_id = 30
group by department_id
);