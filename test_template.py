from pytest import mark

@mark.anyname
def test_as_expected():
    assert False

@mark.ui
def test_fixture(chrome_browser):
    chrome_browser.get('https://www.facebook.com/')
    assert True


@mark.skip(reason="for prod hotfix")
def test_feature_want_to_skip():
    assert False


@mark.xfail(reason="expected to fail")
def test_expected_to_fail():
    assert False


@mark.skip(reason="Have better ways to do this")
@mark.param
@mark.parametrize('tv_brand', [
    ("Samsung"),
    ("Sony"),
    ("Vizio")
])
def test_run_multiple_time_based_on_number_of_param(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.allBrowser
def test_browser_can(browser):
    browser.get("https://www.youtube.com/")

@mark.tvBrand
def test_better_way_of_parma(tv_brand):
    print(f"{tv_brand} turns on as expected")
