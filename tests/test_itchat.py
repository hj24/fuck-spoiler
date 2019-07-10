import pytest
import itchat
from manage import check_msg

WARNING_KEYWORDS = ['蜘蛛侠', '英雄远征', '漫威', '彼得帕克']

#@pytest.mark.finished
@pytest.mark.parametrize('received_text',
                         ['蜘蛛侠，小蜘蛛，英雄远征，铁人',
                          '彼得帕克, 漫威'])
def test_check_msg_success(received_text):
    assert check_msg(received_text, WARNING_KEYWORDS) == True

@pytest.mark.parametrize('received_text', ['.,。，|@&……'])
def test_check_msg_fail(received_text):
    assert check_msg(received_text, WARNING_KEYWORDS) == False