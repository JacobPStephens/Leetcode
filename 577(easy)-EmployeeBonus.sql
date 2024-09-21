-- Jacob Stephens / September 21, 2024
-- https://leetcode.com/problems/employee-bonus/description/
Select name, bonus
from Employee left join Bonus on Employee.empId = Bonus.empId
where bonus < 1000 or bonus is null;
