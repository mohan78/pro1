$(document).ready(function () {
    var today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate());

    $('#datepicker1').datetimepicker({
        footer: true,
        header: true,
        format: 'yyyy-mm-dd HH:MM'
    });

    $('#datepicker2').datetimepicker({
        footer: true,
        header: true,
        format: 'yyyy-mm-dd HH:MM'
    });
})