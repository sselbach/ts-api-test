from common import api_request, response_json


def test_modules():
    res = api_request("/modules")

    assert res.status_code in (200, 206)
    assert (content := response_json(res))
    assert type(content) is list
    
    for m in content:
        assert type(m) is dict
        assert "_id" in m
        assert "name" in m


def test_moduleid():
    res = api_request("/modules/efcbGcXGbnrGKzbKo")

    assert res.status_code == 200
    assert (content := response_json(res))
    assert type(content) is dict

    assert "_id" in content
    assert "name" in content


def test_partslist():
    res = api_request("/modules/efcbGcXGbnrGKzbKo/partsList")

    assert res.status_code == 200
    assert (content := response_json(res))
    assert type(content) is dict

    assert "_id" in content
    assert "name" in content
    assert "lastAnalysis" in content
    assert "components" in content

    assert type(content["components"]) is list

    for comp in content["components"]:
        assert "name" in comp
        assert "versions" in comp
        assert "status" in comp

        for ver in comp["versions"]:
            assert "version" in ver
            
            license_list = ver["licenses"] if "licenses" in ver else []

            for l in license_list:
                assert "name" in l
                assert "spdxKey" in l