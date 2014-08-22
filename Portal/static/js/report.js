/**
 * Created by honglei.yu on 14-6-19.
 */

function report_product_changed(obj, callback_ok){

    var update_json = {
        ProductName: obj
    };

    var json_str = JSON.stringify(update_json);
    $.ajax({
        type: "post",
        url: "/ReportProductChanged/",
        dateType: "json",
        data: json_str,
        success: callback_ok
    });
}

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
    }
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

function report_module_changed(obj, callback_ok){

    var update_json = {
        ModuleName: obj
    };
    var json_str = JSON.stringify(update_json);
    $.ajax({
        type: "post",
        url: "/ReportModuleChanged/",
        dateType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    });
}

function report_job_changed(obj, callback_ok){

    var update_json = {
        JobName: obj
    };
    var json_str = JSON.stringify(update_json);
    $.ajax({
        type: "post",
        url: "/ReportJobChanged/",
        dateType: "json",
        async: false,
        data: json_str,
        success: callback_ok
    });
}

function run_job_result(obj, callback_ok)
{
    var jobname_json = {
        JobName: obj
    };
    var json_str = JSON.stringify(jobname_json);
    $.ajax({
        type:"post",
        url:"JobtoModuleandProduct/",
        dataType: "json",
        data: json_str,
        async: false,
        success: callback_ok
    });
}

function run_job_result(obj, callback_ok)
{
    var jobname_json = {
        JobName: obj
    };
    var json_str = JSON.stringify(jobname_json);
    $.ajax({
        type:"post",
        url:"JobtoModuleandProduct/",
        dataType: "json",
        data: json_str,
        async: false,
        success: callback_ok
    });
}