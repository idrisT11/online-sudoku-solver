
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

var contourStr = urlParams.get('contour');
var imgStr = urlParams.get('token');


var imgLink = 'get_image/'+imgStr;

var contour = contourStr.split('|');
contour = contour.map((row)=>{
    let new_row = row.split('-');
    new_row = new_row.map(e =>
        parseInt(e, 10)
    );

    return new_row;
})

var scaleX = 1;  //The scale will be set as soon as the image is loaded
var scaleY = 1;  //The scale will be set as soon as the image is loaded

var scaledContour = [];

/////////////////////////////////////////////////////////////////////////
var submitLink = document.getElementById('submit');
submitLink.href = generateResultUrl(imgStr, contour);



/////////////////////////////////////////////////////////////////////////
var stage = new Konva.Stage({
    container: 'container',   // id of container <div>
    width: 600,
    height: 600
});

var layerVertx = new Konva.Layer();
var layerLines = new Konva.Layer();
var layerImage = new Konva.Layer();


var vertices = [];
var edges = [];


window.onload = ()=>{
    chargeBorderSelector(imgLink);//imgLink will be defined by the server
}

/////////////////////////////////////////////////////////////////////////

function chargeBorderSelector(imgLink) {
    
    var imageObj = new Image();
    imageObj.onload = function () {

        var yoda = new Konva.Image({
            x: 0,
            y: 0,
            image: imageObj,

        });
        scaleX = 500/yoda.width();
        scaleY = 500/yoda.height();

        yoda.width(500);
        yoda.height(500);

        scaledContour = contour.map((row)=>{
            row[0] *= scaleX;
            row[1] *= scaleY;
            return row;
        });
         
        layerImage.add(yoda);

        showShapes();
    };
    imageObj.src = imgLink;
}

function showShapes(){

    /////////////////////////////////////////////////////////////////////////
    for (let i = 0; i < 4; i++) {

        let circle = new Konva.Circle({
            x: scaledContour[i][0],
            y: scaledContour[i][1],
            radius: 7,
            fill: '#00ff00',
            stroke: 'black',
            strokeWidth: 2
        });

        circle.draggable(true);
        
        vertices.push( circle );

        layerVertx.add(circle);
    }

    /////////////////////////////////////////////////////////////////////////


    for (let i = 0; i < 4; i++) {
        let a = i;
        let b = (i+1)%4;

        let line = new Konva.Line({
            points: [scaledContour[a][0], scaledContour[a][1], scaledContour[b][0], scaledContour[b][1]],
            stroke: 'green',
            strokeWidth: 3,
            lineCap: 'round',
            lineJoin: 'round',
        });

        
        edges.push( line );

        layerLines.add(line);
    }


    /////////////////////////////////////////////////////////////////////////

    for (let i = 0; i < 4; i++) {
        let vertex = vertices[i];
        let a = (i-1+4)%4; //Le plus 4 est due au fait que JS ne gere pas le negatif en modulo
        let b = (i+1)%4;

        vertex.on('dragmove', ()=>{
            let p_1 = [vertex.x(), vertex.y(), vertices[b].x(), vertices[b].y()];
            let p_2 = [vertices[a].x(), vertices[a].y(), vertex.x(), vertex.y()];
            edges[i].points(p_1);
            edges[a].points(p_2);

            scaledContour[i][0] = vertex.x();
            scaledContour[i][1] = vertex.y();

            contour[i][0] = scaledContour[i][0]/scaleX;
            contour[i][1] = scaledContour[i][1]/scaleY;

            submitLink.href = generateResultUrl(imgStr, contour);
        });
        
    }

    stage.add(layerImage);
    stage.add(layerLines);
    stage.add(layerVertx);
    layerVertx.draw();
    layerLines.draw();
    layerImage.draw();
}

function generateResultUrl(token, contour) {
    let url = '/result?token=' + token + '&contour=';
    let contourStr = '';
    for (const row of contour) {
        for (const elem of row) {
            contourStr += Math.floor(elem);
            contourStr += '-';
        }
        contourStr = contourStr.substring(0, contourStr.length-1);
        contourStr += '|';

    }
    contourStr = contourStr.substring(0, contourStr.length-1);
    console.log(contourStr);
    url += contourStr;
    return url;
}


