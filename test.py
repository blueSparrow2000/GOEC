# import re
#
# def ascii_remover(txt):
#     ansi_escape_8bit = re.compile(
#         '\033\\[([0-9]+)(;[0-9]+)*m'
#     )
#     m_pre = ansi_escape_8bit.search(txt)
#     if m_pre:
#         txt = txt[m_pre.end():]
#     m_suf = ansi_escape_8bit.search(txt)
#     if m_suf:
#         txt = txt[:m_suf.start()]
#     return txt
#
# def back_ascii_remover(txt):
#     ansi_escape_8bit = re.compile(
#         '\033\\[([0-9]+)*m'
#     )
#     m_suf = ansi_escape_8bit.search(txt)
#     if m_suf:
#         txt = txt[:m_suf.start()]
#     return txt
#
# def title_refiner(title): # 모든 타이틀(title)은 ' \033[ddm{}\033[0m'이런 형식임. dd는 2자리 정수.
#     title = title.strip()
#     title_list = title.split('the')
#     title_list = title_list[1:]
#     fully_refined_title=''
#     for title in title_list:
#         refined_title = back_ascii_remover(title)
#         fully_refined_title = fully_refined_title + ' the' + refined_title
#     return [fully_refined_title]
#
# #print(title_refiner(' \033[92m{}\033[0m'.format('the Archer')))
#
# print(title_refiner(' \033[92m{}\033[0m'.format('the Archer') + ' \033[92m{}\033[0m'.format('the Rich') + ' \033[92m{}\033[0m'.format('the Mage')))
# print('=============')
# #print(ascii_remover('11 \033[92m111{1}111\033[0m11'))

title = ' the Mage the Rich the Archer'
print(title.split(' the'))