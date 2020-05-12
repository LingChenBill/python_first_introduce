# 从标准库的string模块导入Template类，它支持简单的字符串替换模版
from string import Template


def start_response(resp="text/html"):
    """
    需要一个（可选的）字符串作为参数，用它来创建一个CGI"Content-type"行，参数缺省值是"text/html"
    :param resp:
    :return:
    """
    return 'Content-type: ' + resp + '\n\n'


def include_header(the_title):
    """
    打开header.html头部模版文件，读入模版，可以根据需要替换标题
    :param the_title:
    :return:
    """
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return header.substitute(title=the_title)


def include_footer(the_links):
    """
    打开底部文件，换入the_links中提供的HTML链接字典
    :param the_links:
    :return:
    """
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''

    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)

    return footer.substitute(links=link_string)


def start_form(the_url, form_type="POST"):
    """
    这个函数返回表单最前面的HTML，允许调用者指定URL，还可以指定所要使用的方法
    :param the_url:
    :param form_type:
    :return:
    """
    return '<form action="' + the_url + '" method="' + form_type + '">'


def end_form(submit_msg="Submit"):
    """
    返回表单末尾的HTML标记，同时还允许调用者定制表单submit按钮的文本
    :param submit_msg:
    :return:
    """
    return '<p></p><input type=submit value="' + submit_msg + '"></form>'


def radio_button(rb_name, rb_value):
    """
    给定一个单选按钮和值
    :param rb_name:
    :param rb_value:
    :return:
    """
    return '<input type="radio" name="' + rb_name + '" value="' + rb_value + '"> ' + rb_value + '<br />'


def u_list(items):
    """
    给定一个项列表
    :param items:
    :return:
    """
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'

    return u_string


def header(header_text, header_level=2):
    """
    创建并返回一个HTML标题标记，默认为2级标题
    :param header_text:
    :param header_level:
    :return:
    """
    return '<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>'


def para(para_text):
    """
    段落标记标注文本
    :param para_text:
    :return:
    """
    return '<p>' + para_text + '</p>'


# 测试yate模块
print('start_response: ', start_response())
print('start_response text/plain: ', start_response('text/plain'))
print('include_header: ', include_header('Welcome to my home on the web'))
print('include footer:')
print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
print('start-form: ')
print(start_form('/cgi-bin/process-athlete.py'))
print('end_form: ')
print(end_form())

for fab in ['John', 'Paul', 'George', 'Ringo']:
    print(radio_button(fab, fab))
