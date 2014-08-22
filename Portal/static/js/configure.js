/**
 * Created by honglei.yu on 14-8-5.
 */
function add_product(obj, callback_ok)
{
    var add_json = {
        AddProduct: obj
    };

    var json_str = JSON.stringify(add_json);
    $.ajax({
        type:"post",
        url:"/AddProduct/",
        dataType:"json",
        data:json_str,
        async: false,
        success:callback_ok
    });
}

function updateproduct(obj, callback_ok)
{
    var update_json = {
        ProductName: obj
    };
    var json_str = JSON.stringify(update_json);

    $.ajax({
        type: "post",
        url:"/UpdateProduct/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function updatemodule(obj, callback_ok)
{
    var update_json = {
        ModuleName: obj
    };
    var json_str = JSON.stringify(update_json);

    $.ajax({
        type: "post",
        url: "/UpdateModule/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function updateversion(obj1, obj2, callback_ok)
{
    var update_json = {
        VersionName: obj1,
        ModuleName: obj2
    };
    var json_str = JSON.stringify(update_json);

    $.ajax({
        type: "post",
        url: "/ConfigUpdateVersion/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function updatesuite(obj, callback_ok)
{
    var update_json = {
        SuiteName: obj
    };
    var json_str = JSON.stringify(update_json);

    $.ajax({
        type: "post",
        url: "/ConfigUpdateSuite/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function addtestsuite(obj1, obj2, callback_ok)
{
    var update_json = {
        VersionName: obj1,
        ModuleName: obj2
    };
    var json_str = JSON.stringify(update_json);

    $.ajax({
        type: "post",
        url: "/ConfigUpdateVersion/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function addrunsuite(obj1, obj2, obj3, obj4, callback_ok)
{
    var update_json = {
        RunSuiteName: obj1,
        ModuleName: obj3,
        VersionName: obj2,
        SuiteList: obj4
    };
    var json_str = JSON.stringify(update_json);
    $.ajax({
        type: "post",
        url: "/AddRunSuite/",
        dataType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    })
}

function check_suite_name(obj, callback_ok)
{
    var check_json = {
        CheckSuiteName: obj
    };
    var json_str = JSON.stringify(check_json);
    $.ajax({
        type: "post",
        url: "/CheckSuiteName/",
        dataType: "json",
        data: json_str,
        success: callback_ok
    });
}
