import jieba
import jieba.analyse
import pytest

@pytest.mark.parametrize('comment, keys',
                         [('中国特色社会主义是我们党领导的伟大事业', ['社会主义', '领导', '特色'])])
def test_cut_noun(comment, keys):

    cut = jieba.analyse.extract_tags(comment, topK=20, withWeight=False, allowPOS=('n'))

    assert set(cut) == set(keys)