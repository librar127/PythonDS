"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employees.sort(key = lambda emp: emp.id)
        
        dict_emp = {}
        led_sub = {} 
        sub_list = [id]
        
        
        for emp in employees:
            
            dict_emp[emp.id] = emp.importance
            
            for each_sub in emp.subordinates:
                led_sub[each_sub] = emp.id
            
            if emp.id == id or emp.id in sub_list:
                if len(emp.subordinates) > 0:
                    sub_list.extend(emp.subordinates)
                
        sum_imp = 0
        for each in sub_list:
            sum_imp += dict_emp[each]
            
        return sum_imp