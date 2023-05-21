import math
class Pagination():
    def __init__(self, items = None, pageSize =10):
        self.items =list(items)
        self.pageSize =pageSize
        self.totalPages =  math.ceil(len(self.items)/self.pageSize)
        self.currentPage = 1
        
        
    def getVisibleItems(self):
        start_index = (self.currentPage-1)*self.pageSize
        end_index = start_index+self.pageSize
        print(self.items[start_index:end_index])
        return self.items[start_index:end_index]
        
    def nextPage(self):
        self.currentPage = min(self.currentPage+1, self.totalPages)
        return self
    
    def prevPage(self, page_number =1):
        self.currentPage = max(self.currentPage-1, 1)
        return self
    
    def firstPage(self):
        self.currentPage =1
        return self

    
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    
    def goToPage(self, pageNum):
        page = pageNum
        if page > self.totalPages:
            page==self.totalPages
        self.currentPage = page
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

page = Pagination(alphabetList, 4)
print('******************')
print('Start')
page.getVisibleItems()
print('******************')
print('Next page')
page.nextPage()
page.getVisibleItems()
print('******************')
print('Next page')
page.nextPage()
page.getVisibleItems()
print('******************')
print('Next page')
page.nextPage()
page.getVisibleItems()
print('******************')
print('Previous page')
page.prevPage()
page.getVisibleItems()
print('******************')
print('First page')
page.firstPage()
page.getVisibleItems()
print('******************')
print('Last page')
page.lastPage()
page.getVisibleItems()
print('******************')
print('To page')
page.goToPage(4)
page.getVisibleItems()
