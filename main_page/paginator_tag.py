from django import template

register = template.Library()

@register.simple_tag
def PAGINATION(curr_page,paginator,num_of_pages=10,pages_back=4):
    pages_front = num_of_pages - pages_back - 3
    html=''

    if paginator.num_pages <= num_of_pages:
        for i in range(1,paginator.num_pages+1):
            html+= '<li><a href="?page=%s">%s</a></li>'%(i,i)
        return html
    elif curr_page.number <= num_of_pages-pages_back:
        for i in range(1,num_of_pages+1):
            html+= '<li><a href="?page=%s">%s</a></li>'%(i,i)
        return html
    elif num_of_pages-pages_front <= curr_page.number <= paginator.num_of_pages - pages_back:
        html = '''
            <li><a href="?page=1">1</a></li>
            <li class="disabled"><a href="?page=1">...</a></li>
        '''
        for i in range(curr_page.number - pages_front,curr_page.number + pages_back+1):
            html+='<li><a href="?page=%s">%s</a></la>'%(i,i)
        return html
    else:
        html = '''
            <li><a href="?page=1">1</a></li>
            <li class="disabled"><a href="?page=1">...</a></li>
        '''
        for i in range(paginator.num_pages-pages_back-pages_front,paginator.num_pages+1):
            html+='<li><a href="?page=%s">%s</a></la>'%(i,i)
        return html
        