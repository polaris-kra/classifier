function classify() {
    $('#btn-analysis-id').hide();
    $('#wait-block-id').show();

    var fd = new FormData();
    var files = $('#img-file-id')[0].files[0];
    fd.append('img', files);

    $.ajax({
        url: '/classify_ajax',
        type: 'post',
        data: fd,
        contentType: false,
        processData: false,
        success: function(response){
            result = response['result'];
            createDiseaseResult(result);
        },
        error: function(response){
        },
        complete: function(response){
            $('#wait-block-id').hide();
        }
    });
}

function createDiseaseResult(result){
    var resultsDiv = $('#results-block-id');
    var diseases = result['diseases'];
    var details = result['details'];

    var innerHtml = '<div id="diseases-result-id">';
    if (diseases.length == 0) {
        innerHtml += '<p class="polaris-welcome-text"><b>Болезни не выявлены</b></p>';
    }
    else {
        innerHtml += '<p class="polaris-diseases-detected">Выявлены болезни:';
        for (var i in diseases) {
            var disease = diseases[i];
            innerHtml += '<br><span class="text-danger"><b>' + disease + '</b></span>';
        }
        innerHtml += '</p>';
        innerHtml += '<a href="javascript:displayDetails(true);">подробнее</a>';
    }
    innerHtml += '</div>';

    innerHtml += '<div id="diseases-details-id">';
    innerHtml += '<table class="polaris-details-table">';
    for (var class_name in details) {
        var pct = Math.round(100*details[class_name]);
        var disease_class = ((pct >= 80) ? 'text-danger' : '');
        innerHtml += '<tr class="' + disease_class + '">';
        innerHtml += '<td class="polaris-disease-td">' + class_name + '</td>';
        innerHtml += '<td class="polaris-disease-pct-td">' + pct + '%</td>';
        innerHtml += '</tr>';
    }
    innerHtml += '</table>';

    innerHtml += '<a href="javascript:displayDetails(false);">скрыть</a>';
    innerHtml += '</div>';

    resultsDiv.html(innerHtml);
    resultsDiv.show();
}