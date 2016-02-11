/**
 * Created by manny42 on 06/02/16.
 */
window.onload = function () {

    var context;

    var canvas = function () {

        var myStickman = document.getElementById("stickman");
        context = myStickman.getContext('2d');
        context.beginPath();
        context.strokeStyle = "#000";
        context.lineWidth = 2;
        drawArray[7]();
        drawArray[8]();
        drawArray[9]();
    };

    var head = function () {
        var myStickman = document.getElementById("stickman");
        context = myStickman.getContext('2d');
        context.beginPath();
        context.arc(60, 25, 10, 0, Math.PI * 2, true);
        context.stroke();
    };

    var draw = function ($pathFromx, $pathFromy, $pathTox, $pathToy) {
        context.moveTo($pathFromx, $pathFromy);
        context.lineTo($pathTox, $pathToy);
        context.stroke();
    };

    var frame1 = function () {
        draw(0, 150, 150, 150);
    };

    var frame2 = function () {
        draw(10, 0, 10, 600);
    };

    var frame3 = function () {
        draw(0, 5, 70, 5);
    };

    var frame4 = function () {
        draw(60, 5, 60, 15);
    };

    var torso = function () {
        draw(60, 36, 60, 70);
    };

    var rightArm = function () {
        draw(60, 46, 100, 50);
    };

    var leftArm = function () {
        draw(60, 46, 20, 50);
    };

    var rightLeg = function () {
        draw(60, 70, 100, 100);
    };

    var leftLeg = function () {
        draw(60, 70, 20, 100);
    };

    var drawArray = [rightLeg, leftLeg, rightArm, leftArm, torso, head, frame4, frame3, frame2, frame1];

    var drawTries = function() {
        if (tries < 5) {
            drawArray[6]();
        }
        if (tries < 4) {
            drawArray[5]();
        }
        if (tries < 3) {
            drawArray[4]();
        }
        if (tries < 2) {
            drawArray[3]();
            drawArray[2]();
        }
        if (tries < 1) {
            drawArray[1]();
            drawArray[0]();
        }
    };

    canvas();
    drawTries();
};
