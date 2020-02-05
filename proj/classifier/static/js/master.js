function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            $('#img-preview')
                .attr('src', e.target.result)
                .width(250)
                .height(250);

            document.getElementById("btn-analysis").style.visibility = 'visible';
            document.getElementById("results-block").style.visibility = 'hidden';
        };

        reader.readAsDataURL(input.files[0]);
    }
}
