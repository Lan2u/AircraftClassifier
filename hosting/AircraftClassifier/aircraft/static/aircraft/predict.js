console.log("Predict JS loaded");

// The API endpoint used for prediction.
// Important to make sure that the API url starts with an allowed protocol (in this case http:) otherwise
// chrome won't allow the request.
const API_PREDICT_ENDPOINT = "http://localhost:8000/predict/aircraft/variant/";

// Timeout the prediction request after 3000 milliseconds.
const PREDICTION_TIMEOUT_MS = 3000;

function startWaitingForPredict() {
    console.log("Waiting for prediction...")
}

// Called if the file to upload for a prediction fails to upload / isn't found.
function fileUploadFailed() {
    console.log("Failed to upload file");
}

// Called on prediction failure (signalled by the API response).
function predictionFailed(error) {
    console.log("Failed to run prediction");
}

// Called if the prediction attempt times-out before receiving a response.
function predictionTimeout() {

}

// Called on prediction success.
function predictionSuccess(data) {
    clearTimeout();
}

// Called on progress updates when uploading a prediction request.
function predictionProgress(event) {
    // var percent = 0;
    // var position = event.loaded || event.position;
    // var total = event.total;
    // var progress_bar_id = "#progress-wrp";
    // if (event.lengthComputable) {
    //     percent = Math.ceil(position / total * 100);
    // }
    // // update progressbars classes so it fits your code
    // $(progress_bar_id + " .progress-bar").css("width", +percent + "%");
    // $(progress_bar_id + " .status").text(percent + "%");
}

function performPrediction(file, name) {
    let formData = new FormData();
    formData.append("file", file, name)
    formData.append("upload_file", true)

    let headers = new Headers();

    $.ajax({
        type: "POST",
        url: API_PREDICT_ENDPOINT,
        xhr: function () {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                myXhr.upload.addEventListener('progress', predictionProgress, false);
            }
            return myXhr;
        },
        success: predictionSuccess,
        error: predictionFailed,
        async: true,
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        timeout: 60000,
        // headers: headers,
        credentials: 'include'
    });
}

$(function() {
    $("#predict_image_form").submit(function(e) {
        e.preventDefault();

        console.log("Image submitted");
        let file = $('#aircraft_img').prop('files')[0];

        if (file === undefined || file === null) {
            fileUploadFailed();
        } else {
            startWaitingForPredict();
            performPrediction(file, file.name); // Now wait for callback.
            setTimeout(predictionTimeout, PREDICTION_TIMEOUT_MS);
        }
        return false; // Don't refresh
    });
})

