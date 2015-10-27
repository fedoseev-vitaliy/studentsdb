import collections

class InvalidPage(Exception):
    pass

class EmptyPage(InvalidPage):
    pass

class PageNotAnInteger(InvalidPage):
    pass


# paginator class
class MyPaginator(object):
    
        
    def __init__(self, query_set, items_on_page, allow_empty_first_page=True):        
        self.items_on_page = int(items_on_page)        
        self.allow_empty_first_page = allow_empty_first_page
        
        self.query_set = []        
        while query_set.count() > items_on_page:
            pice = query_set[:items_on_page]
            self.query_set.append(pice)
            query_set = query_set[items_on_page:]    
        self.query_set.append(query_set)          
        
        self._count = 0
    
    def validate_number(self, number):
        """
        Validates the given 1-based page number.
        """
        try:
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger('That page number is not an integer')
        if number < 1:
            raise EmptyPage('That page number is less than 1')
        if number > self.page_count:
            if number == 1 and self.allow_empty_first_page:
                pass
            else:
                raise EmptyPage('That page contains no results')
        return number
    
    
    @property
    def count(self):
        """
        Returns the total number of objects, across all pages.
        """        
        try:
            for q_set in self.query_set:
                self._count = self._count + q_set.count()
        except (AttributeError, TypeError):
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            for q_set in self.query_set:
                self._count = self._count + len(q_set)
        return self._count
    
    
    
    @property
    def page_count(self):
        """
        Returns the total number of pages.
        """        
        if self.count == 0 and not self.allow_empty_first_page:
            self._page_count = 0
        else:
            hits = max(1, self.count)
            self._page_count = int(hits / float(self.items_on_page))
        return self._page_count
                             
    
    def page(self, page_num):
        number = self.validate_number(page_num)
        return Page(self.query_set[number - 1], number, self)
    
    
    
class Page(collections.Sequence):
    
    def __init__(self, query_set, number, paginator):
        self.paginator = paginator
        self.number = number
        self.query_set = query_set
        
    def __len__(self): 
        return len(self.query_set)
    
    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.paginator.page_num)

    def __getitem__(self, index):        
        return self.query_set[index]
    
    
    
    