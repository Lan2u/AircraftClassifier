console.log("Predict JS loaded");

// The API endpoint used for prediction.
// Important to make sure that the API url starts with an allowed protocol (in this case http:) otherwise
// chrome won't allow the request (reported as CORS error).
const API_PREDICT_ENDPOINT = "http://localhost:8000/predict/aircraft/variant/";

// Timeout the prediction request after 3000 milliseconds.
const PREDICTION_TIMEOUT_MS = 3000;

// Only display predictions which have above a 5% probability
const DISPLAY_PREDICT_THRESHOLD = 0.05;

function startWaitingForPredict() {
    console.log("Waiting for prediction...")
}

// Called if the file to upload for a prediction fails to upload / isn't found.
function fileUploadFailed() {
    console.log("Failed to upload file");
}

// Called on prediction failure (signalled by the API response).
function predictionFailed(error) {
    console.log("Failed to run prediction: " + error.toString());
}

// Generates a colour value used as part of the charts.
function genColor(seed) {
    const CHART_COLOURS = [
        'rgba(255,0,0,0.66)',
        'rgba(255,128,0,0.66)',
        'rgba(255,255,0,0.62)',
        'rgba(128,255,0,0.6)',
        'rgba(0,255,255,0.47)',
        'rgba(0,64,255,0.5)',
        'rgba(191,0,255,0.53)'];
    if (seed < CHART_COLOURS.length) {
        return CHART_COLOURS[seed];
    } else {
        return '#000000';
    }
}

// Called on prediction success.
function predictionSuccess(rawData) {
    console.log("Successfully run prediction")
    console.log(rawData);

    let predictions = rawData['predictions'];

    let data = [];
    let labels = [];
    let colors = [];

    console.log(predictions);

    for (x in predictions) {
        // console.log(x);
        let prob = predictions[x]['probability'];
        console.log(prob);
        if (prob > DISPLAY_PREDICT_THRESHOLD) {
            labels.push(predictions[x].variant_name);
            data.push(predictions[x].probability);
            colors.push(genColor(x))
        }
    }

    console.log(colors);

    let predictionCtx = document.getElementById('prediction_percentage_canvas').getContext('2d');
    let predictionChart = new Chart(predictionCtx, {
        type: 'pie',
        data: {
            datasets: [{
                data: data,
                label: 'Predicted Variant Probabilities',
                backgroundColor: colors,
            }],
            labels: labels
        },
        options: {
            responsive: true
        }
    });
    console.log(data);
    console.log(labels);
    console.log(predictionChart);
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

function performPrediction(file) {
    let formData = new FormData();
    formData.append("predictFile", file);

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
        timeout: PREDICTION_TIMEOUT_MS,
        credentials: 'include'
    });
}

$(function() {
    // Setup CSRF.
    $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           if (!this.crossDomain) {
               xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
           }
       }
    });

    $("#predict_image_form").submit(function(e) {
        e.preventDefault(); // Prevent the default action of refreshing.

        console.log("Image submitted");
        let file = $('#aircraft_img').prop('files')[0];

        if (file === undefined || file === null) {
            fileUploadFailed();
        } else {
            startWaitingForPredict();
            performPrediction(file, file.name); // Now wait for callback from API (or timeout).
        }
        return false; // Don't refresh
    });
})