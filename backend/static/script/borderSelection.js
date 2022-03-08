var  contour = [
    [60, 60],
    [50, 400],
    [550, 450],
    [500, 60],
];



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
    let scale = 600/yoda.width();
    stage.height( yoda.height()*scale );

    yoda.scaleX(scale);
    yoda.scaleY(scale);

        layerImage.add(yoda);
    };
    imageObj.src = imgLink;

    /////////////////////////////////////////////////////////////////////////
    for (let i = 0; i < 4; i++) {
        let circle = new Konva.Circle({
            x: contour[i][0],
            y: contour[i][1],
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
            points: [contour[a][0], contour[a][1], contour[b][0], contour[b][1]],
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

            contour[i][0] = vertex.x();
            contour[i][1] = vertex.y();
        });
        
    }

    stage.add(layerImage);
    stage.add(layerLines);
    stage.add(layerVertx);
    layerVertx.draw();
    layerLines.draw();
    layerImage.draw();
}


