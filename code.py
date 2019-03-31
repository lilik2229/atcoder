from functools import reduce

class Group():
    def __init__(self,num_of_person,start_sheet):
        self.num_of_person = num_of_person
        self.start_sheet = start_sheet
        
class Sheet():
    def __init__(self,num_of_sheets):
        self.num_of_sheets = num_of_sheets
        self.is_sheets_available = [0 for i in range(self.num_of_sheets)]
        
    def take_sheets(self,num_of_person,start_sheet):
        sheets = start_sheet        
        target_sheets = [0 for i in range(self.num_of_sheets)]
        
        # 欲しい席の一覧を作成
        for i in range(num_of_person):       
            target_sheets[sheets] = 1;            
            sheets = self.next_sheets(sheets)

        # 席に人がいるか確認 既に人が座っている場合はfalse
        if(not self.can_take_sheets(target_sheets)):
            return False
        
        self.update_sheets(target_sheets)
        
        return True
    
    def next_sheets(self,sheets):        
        return (sheets + 1) % self.num_of_sheets

    def can_take_sheets(self,target_sheets):
        for i in range(self.num_of_sheets):
            if(target_sheets[i]==1 and self.is_sheets_available[i] ==1):
                return False
        return True

    def update_sheets(self,target_sheets):
        for i in range(self.num_of_sheets):
            if(target_sheets[i]==1):
                self.is_sheets_available[i] = 1        
    
def main():
    group = []
    s = input().rstrip().split(' ')
    sheet = Sheet(int(s[0]))
    group_num = int(s[1])

    for i in range(group_num):
        s = input().rstrip().split(' ')
        group.append(Group(int(s[0]),int(s[1])-1))        
        sheet.take_sheets(group[i].num_of_person,group[i].start_sheet)
    print(reduce(lambda a,b:a+b,sheet.is_sheets_available))
    
if __name__ == '__main__':
    main()
                
