create or replace function return_rate (a varchar(2))
returns table (
country varchar(50),
confirm int) AS $$
BEGIN 
if a = '2' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-1-31' or date ='2020-2-29';
end if;
if a = '3' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-2-29' or date ='2020-3-31';
end if;
if a = '4' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-3-31' or date ='2020-4-30';
end if;
if a = '5' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-4-30' or date ='2020-5-31';
end if;
if a = '6' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-5-31' or date ='2020-6-30';
end if;
if a = '7' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-6-30' or date ='2020-7-31';
end if;
if a = '8' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-7-31' or date ='2020-8-31';
end if;
if a = '9' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-8-31' or date ='2020-9-30';
end if;
if a = '10' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-9-30' or date ='2020-10-31';
end if;
if a = '11' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-10-31' or date ='2020-11-30';
end if;
if a = '12' then
return query select country_name,confirmed 
from country_confirmed_cases 
where date = '2020-11-30' or date ='2020-12-29';
end if;
END;$$
Language plpgsql;