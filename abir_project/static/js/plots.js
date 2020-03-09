$('#month_selection').on('change',function(){

    $.ajax({
        url: "/scatter_polar",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'selected': document.getElementById('month_selection').value

        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('scatter_polar', data );
        }
    });
})
