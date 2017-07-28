/**
 * Created by Administrator on 2017/7/28.
 */
$(document).ready(function () {
    $.getJSON('/today_on_history/', function(data){
        var his_data = jQuery.parseJSON(data);
        console.log(his_data);
        $('#history_des').html(
            his_data.des
        );
        $('#history_pic').html(
            '<img src="'+his_data.pic+'" width="280" height="215">'
        );
    });
});