import collections

class InvalidPage(Exception):
    pass

class EmptyPage(InvalidPage):
    pass

class PageNotAnInteger(InvalidPage):
    pass


# paginator class
class MyPaginator(object):
        
    def __init__(self, query_set, items_on_page, allow_empty_first_page = True):        
        self.items_on_page = int(items_on_page)        
        self.initial_query_set = query_set
        
        self.query_set = []        
        while query_set.count() > items_on_page:
            pice = query_set[:items_on_page]
            self.query_set.append(pice)
            query_set = query_set[items_on_page:]    
        self.query_set.append(pice)
        
        self._page_count = None 
        
    
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
    def has_pages(self):
        """
        Returns True/False if query set contains any objects.
        """
        return self.query_set
    
    
    @property
    def page_num(self):
        """
        Returns the total number of pages.
        """
        return int(self.page_count/float(self.items_on_page))
    
          
    @property
    def page_count(self):
        """
        Returns the total number of objects.
        """
        if self._page_count == None:
            try:
                self._page_count = self.initial_query_set.count()
            except (AttributeError, TypeError):
                # AttributeError if object_list has no count() method.
                # TypeError if object_list.count() requires arguments
                # (i.e. is of type list).
                self._page_count = len(self.initial_query_set)
        return self._page_count
    
    
    @property
    def page_range(self):
        """
        Returns iterable list pages.
        """
        return list(range(1, self.page_num + 1))
    
    
    def page(self, page_num):
        number = self.validate_number(page_num)
        return Page(self.query_set, number, self)
    
    
    
class Page(collections.Sequence):
    
    def __init__(self, query_set, number, paginator):
        self.paginator = paginator
        self.number = number
        self.query_set = query_set[self.number - 1]
        
    def __len__(self): 
        return len(self.query_set)
    
    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.paginator.page_num)

    def __getitem__(self, index):        
        return self.query_set[index]
    
    
    
    