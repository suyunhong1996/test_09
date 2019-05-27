import allure
import pytest


class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试加法步骤")
    def test_01(self):
        print("起风了")
        allure.attach("标题","具体内容")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试断言步骤")
    def test_02(self):
        print("今夜月色很美")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个测试步骤")
    def test_03(self):
        print("时间之中")
        allure.attach("标题","具体内容")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试断步骤")
    def test_04(self):
        print("IF")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试言步骤")
    def test_05(self):
        print("U")
        assert 1
