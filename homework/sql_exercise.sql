/**********************************************************
*	SQL Query & Function Example1
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

--�μ���ȣ�� 10���� �μ��� ��� �� �����ȣ, �̸�, ������ ����϶�
select employee_id, first_name, last_name, salary
from employees
where department_id = 10;




--�����ȣ�� 7369�� ��� �� �̸�, �Ի���, �μ� ��ȣ�� ����϶�.
select first_name, last_name, hire_date, department_id
from employees
where employee_id = 7369;



--�̸��� Ellen�� ����� ��� ������ ����϶�.
select * from employees
where first_name = 'Ellen';




--�Ի����� 08/04/21�� ����� �̸�, �μ���ȣ, ������ ����϶�.
select first_name, last_name, department_id, salary
from employees
where hire_date = '08/04/21';





--������ SA_MAN �ƴ� ����� ��� ������ ����϶�.
select * from jobs
where JOB_ID != 'SA_MAN';



--�Ի����� 08/04/21 ���Ŀ� �Ի��� ����� ������ ����϶�.
select e.* from employees e, job_history j
where TO_DATE(j.start_date, 'YYYY/MM/DD') > TO_DATE('08/04/21', 'YYYY/MM/DD') and j.employee_id = e.employee_id;


--�μ���ȣ�� 20,30���� ������ ��� ����� �̸�, �����ȣ, �μ���ȣ�� ����϶�.
select first_name, last_name, employee_id, department_id
from employees
where department_id not in (20, 30);




--�̸��� S�� �����ϴ� ����� �����ȣ, �̸�, �Ի���, �μ���ȣ�� ����϶�.
select employee_id, first_name, last_name, department_id from employees
where first_name like 'S%';


--�̸��� s�� �����ϰ� ������ ���ڰ� t�� ����� ������ ����϶�.
select * from employees
where first_name like 's%' and last_name like '%t';



/**
employees ���̺��� �̸�, �޿�, ��, �Ѿ��� ���Ͽ� �Ѿ� ���� ������ ����϶� �� �󿩱��� NULL�� ����� ����

*/
select employee_id, salary + commission_pct as total from employees
where commission_pct is not null
order by total desc;



/**
10�� �μ��� ��� ����鿡�� �޿��� 13%�� ���ʽ��� �����ϱ�� �Ͽ���. �̸�, �޿�, ���ʽ��ݾ�, �μ���ȣ�� ����϶�.
**/
select first_name, last_name, salary*0.13 as bonus, department_id from employees
where department_id = 10;


/**
30�� �μ��� ������ ����Ͽ� �̸�, �μ���ȣ, �޿�, ������ ����϶�. �� ������ �޿��� 150%�� ���ʽ��� �����Ѵ�.
   -- ���� = sal*12+(sal*1.5)
**/
select first_name, last_name, department_id, salary, salary*12 + (salary*1.5) as total from employees
where department_id = 30;



/**
�μ���ȣ�� 20�� �μ��� �ð��� �ӱ��� ����Ͽ� ����϶�. �� 1���� �ٹ��ϼ��� 12���̰� 1�� �ٹ��ð��� 5�ð��̴�.
��¾���� �̸�, �޿�, �ð��� �ӱ�(�Ҽ����� 1��° �ڸ����� �ݿø�)�� ����϶�.
   -- �ñ� = sal/�ϼ�/�ð�  -> sal/ 12/5 
   -- round(m, n) m�� �Ҽ��� n�ڸ����� �ݿø� 
**/
select first_name, last_name, salary, round(salary/60, 1)
from employees
where department_id = 20;



/**
�޿��� 1500���� 3000������ ����� �޿��� 5%�� ȸ��� �����ϱ�� �Ͽ���. �̸� �̸�, �޿�, ȸ��(-2�ڸ����� �ݿø�)�� ����϶�.
	-- ȸ��  = sal * 0.05	
	-- -2�ڸ����� �ݿø� : ���� 2��° �ڸ����� �ݿø�.. 100������  
**/
select first_name, last_name, salary, round(salary*0.05, 2) as monthly_cost
from employees
where salary between 1500 and 3000;  




/**
�Ի��Ϻ��� ���ݱ����� ��¥���� ����϶�. �μ���ȣ, �̸�, �Ի���, ������, �ٹ��ϼ�(�Ҽ�����������), �ٹ����,
 �ٹ�����(30�� ����)�� ����϶�.
	-- ���� ��¥ : sysdate 
	-- �ٹ� �ϼ� : ���糯¥ - �Ի��� = sysdate - hire_date  -> ��¥ - ��¥ : �ϼ� ����
	-- �ٹ� ��� : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
	-- �ٹ� ���� : �ٹ��ϼ� / 1��(30��)
**/
select department_id, first_name, last_name, hire_date, sysdate as now, round(sysdate - hire_date, 0) as work_date, to_char(sysdate, 'YYYY') - to_char(hire_date, 'YYYY') as work_year,
round(round(sysdate - hire_date, 0)/ 30, 0) as work_month
from employees;






/**
�Ի��Ϸκ��� ���ñ����� �ϼ��� ���Ͽ� �̸�, �Ի���, �ٹ��ϼ��� ����϶�.
--round(sysdate-hiredate,0) �ٹ��ϼ�
**/
select first_name, last_name, hire_date, round(sysdate - hire_date, 0) as work_date
from employees;


/**
�Ի����� 2012�� 7�� 5���� ���·� �̸�, �Ի����� ����϶�.
	-- ��¥ ���� �տ� fm �� ���� '0'�� ǥ������ �ʴ´ٴ� ��.. 
	-- 'fmYYYY"��" MM"��" DD"��' 
**/

select first_name, last_name, to_char(hire_date, 'fmYYYY"��" MM"��" DD"��"') as hire_date
from employees;


/**
�̸�(first_name)�� ���ڼ��� 6���̻��� ����� �̸��� �տ��� 3�ڸ� ���Ͽ� �ҹ��ڷ� �̸����� ����϶�.
	-- substr(str, position, length) : str ���ڸ� positin ���� length���� ��ŭ ǥ��
	-- lower(str)  �ҹ��� ��ȯ
	-- length(str)  str�� ����
**/

select lower(substr(first_name, 0, 3)) as name
from employees
where length(first_name) >= 6;




/**
10�� �μ� ������ ��դ� �ְ�, ����, �ο����� ���Ͽ� ����϶�
**/

select avg(salary) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id) as cnt
from employees
where department_id = 10
group by department_id;



/**
�� �μ��� �޿��� ���, �ְ�, ����, �ο����� ���Ͽ� ����϶�.
**/

select department_id, round(avg(salary),0) as avg_salary, max(salary) as max_salary, min(salary) as min_salary, count(employee_id) as cnt
from employees
where department_id is not null
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

select d.department_id, d.department_name, count(e.employee_id) as cnt
from employees e, departments d
where e.department_id = d.department_id
group by d.department_id, d.department_name
having count(e.employee_id) >= 4;



/**
�� �μ��� ��տ���, ��ü����, �ְ����, ��������,�� ���Ͽ� ��տ����� ���������� ����϶�.
**/

select round(avg(salary),0) as avg_salary, sum(salary) as sum_salary, max(salary) as max_salary, min(salary) as min_salary
from employees
group by department_id
order by round(avg(salary),0) desc;


