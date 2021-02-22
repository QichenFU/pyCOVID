create or replace function return_country (name varchar(50),a varchar(4))
returns table (
dates date,
confirm int) AS $$
BEGIN 
if a = '1' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-1-22' and date <='2020-1-31'
and Country_name=name;
end if;
if a = '2' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-2-1' and date <='2020-2-29'
and Country_name=name;
end if;
if a = '3' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-3-1' and date <='2020-3-31'
and Country_name=name;
end if;
if a = '4' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-4-1' and date <='2020-4-30'
and Country_name=name;
end if;
if a = '5' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-5-1' and date <='2020-5-31'
and Country_name=name;
end if;
if a = '6' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-6-1' and date <='2020-6-30'
and Country_name=name;
end if;
if a = '7' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-7-1' and date <='2020-7-31'
and Country_name=name;
end if;
if a = '8' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-8-1' and date <='2020-8-31'
and Country_name=name;
end if;
if a = '9' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-9-1' and date <='2020-9-30'
and Country_name=name;
end if;
if a = '10' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-10-1' and date <='2020-10-31'
and Country_name=name;
end if;
if a = '11' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-11-1' and date <='2020-11-30'
and Country_name=name;
end if;
if a = '12' then
return query select date,confirmed 
from country_confirmed_cases 
where date >= '2020-12-1' and date <='2020-12-29'
and Country_name=name;
end if;
if a = '2020' then
return query select date,confirmed 
from country_confirmed_cases 
where (date = '2020-01-31' or  date = '2020-02-29' or  date = '2020-03-31' or date =  '2020-04-30' or date =  '2020-05-31' or  date = '2020-06-30' or date =  '2020-07-31' 
or date =  '2020-8-31' or  date = '2020-9-30' or date =  '2020-10-31' or  date = '2020-11-30' or  date = '2020-12-29') 
and Country_name=name;
end if;
END;$$
Language plpgsql;