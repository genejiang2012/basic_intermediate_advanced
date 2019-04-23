import sys
import codecs

src_file = r"D:\Git\genejiang2012\py_basic_intermediate_advanced\first_party_tag_tablerule.txt"
dst_file = r"D:\Git\genejiang2012\py_basic_intermediate_advanced\after.txt"


def analyze_txt():
    with codecs.open(src_file, 'r', encoding='utf-8') as fr, \
            codecs.open(dst_file, 'w', encoding='utf-8') as fw:
        while True:
            line = fr.readline()
            if not line:
                break
            every_col = line.split('\t')
            # 处理最后一行的col
            col_end = eval(every_col[-1])
            for i in range(len(col_end)):
                col_env_value = col_end[i].values()
                # 拼接前面三个字段
                prev_col = "\t".join(
                    [every_col[i] for i in range(len(every_col) - 1)])
                # 拼接最后两个字段
                end_new_col = "\t".join([str(x) for x in col_env_value])
                new_line = prev_col + "\t" + end_new_col + "\n"
                fw.write(new_line)


if __name__ == '__main__':
    analyze_txt()
