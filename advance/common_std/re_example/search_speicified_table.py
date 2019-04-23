import re
import codecs
import sys


def search_table(src_file, dst_file, pattern):
    with codecs.open(src_file, 'r', encoding='utf-8') as fo, \
            codecs.open(dst_file, 'w', encoding='utf-8') as fw:
        new_list = []
        for line in fo:
            temp_list = re.findall(pattern, line)
            if temp_list:
                new_line = temp_list[0].split(' ')[1] + "\n"
                new_list.append(new_line)
        drop_repeater = set(new_list)
        for item in drop_repeater:
            fw.write(item)


if __name__ == '__main__':
    src_file = r"D:\Git\genejiang2012\py_basic_intermediate_advanced\advance\common_std\re_example\dw_das.tag_rv_app_action.txt"
    dst_file = r"D:\Git\genejiang2012\py_basic_intermediate_advanced\advance\common_std\re_example\test.txt"
    pattern = re.compile("from \s*\w*\.\w*")

    search_table(src_file, dst_file, pattern)

    print("done")
