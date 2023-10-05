function addWorkout() {
    var workoutType = document.getElementById("workout-type").value;
    var sets = document.getElementById("sets").value;
    var reps = document.getElementById("reps").value;
    if (workoutType && sets && reps) {
        var workoutItem = document.createElement("li");
        workoutItem.textContent = `Workout: ${workoutType}, Sets: ${sets}, Reps: ${reps}`;
        document.getElementById("workout-list").appendChild(workoutItem);
        document.getElementById("workout-type").value = "";
        document.getElementById("sets").value = "";
        document.getElementById("reps").value = "";
    } else {
        alert("Please fill out all fields.");
    }
}

function finishWorkout() {
    var workoutItems = document.querySelectorAll("#workout-list li");
    var workouts = [];

    workoutItems.forEach(function(item) {
        var workoutDetails = item.textContent.split(', ');
        var exercise = workoutDetails[0].replace('Workout: ', '');
        var sets = parseInt(workoutDetails[1].replace('Sets: ', ''));
        var reps = parseInt(workoutDetails[2].replace('Reps: ', ''));
        workouts.push({ exercise, sets, reps });
    });

    // Send workout data to the backend for prediction
    fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ workouts })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the prediction result from the server
        var predictedMuscles = data.predictions.join(', ');
        alert("Here is your workout routine:\n\n" + workoutRoutine + "\n\nPredicted Muscles: " + predictedMuscles);
    })
    .catch(error => console.error('Error:', error));
}