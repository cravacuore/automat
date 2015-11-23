
var draw_graph = function(automata){
    
    var canvas = document.getElementById('graph-canvas');
    var ctx = canvas.getContext('2d');
    var x = 150;
    var centerY = canvas.height / 2;
    var radius = 20;

    function neighbors(origin, destination){
        return Math.abs(origin.circle.x - destination.circle.x) == 100;
    };

    function Circle(ctx, x, y, radius){
       this.ctx = ctx;
       this.x = x;
       this.y = y;
       this.radius = radius;
    }

    Circle.prototype.draw = function(){
        this.ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
        this.ctx.fillStyle = 'white';
        this.ctx.fill();
        this.ctx.lineWidth = 2;
        this.ctx.strokeStyle = '#003300';
    };

    function NameState(ctx, name, x, y){
        this.ctx = ctx;
        this.name = name;
        this.x = x;
        this.y = y;
    }

    NameState.prototype.draw = function(){
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillStyle = 'black';
        this.ctx.fillText(this.name, this.x, this.y);
    };

    function State(name, is_initial, is_final, ctx){
        this.ctx = ctx;
        this.name = new NameState(this.ctx, name, x, centerY);
        this.circle = new Circle(this.ctx, x, centerY,radius);
        this.is_initial = is_initial;
        this.is_final = is_final;
        this.x = x;
        x = x + 100;
    }

    State.prototype.draw = function(){
        this.ctx.beginPath();
        this.circle.draw();
        this.ctx.stroke();
        this.ctx.beginPath();
        if(this.is_final){
            new Circle(this.ctx, x - 100, centerY,radius - 5).draw();
        }
        this.name.draw();
        this.ctx.stroke();
    };

    function StraightLine(fromx, fromy, tox, toy, ctx){
        if(fromx < tox) {
            this.fromx = fromx+20;
            this.tox = tox-20;
        }else{
            this.fromx = fromx-20;
            this.tox = tox+20;
        }
        this.fromy = fromy;
        this.toy = toy;
        this.ctx = ctx;
    }

    StraightLine.prototype.draw = function() {
        var headlen = 10; // length of head in pixels
        var dx = this.tox-this.fromx;
        var dy = this.toy-this.fromy;
        var angle = Math.atan2(dy,dx);
        this.ctx.moveTo(this.fromx, this.fromy);
        this.ctx.lineTo(this.tox, this.toy);
        this.ctx.lineTo(this.tox-headlen*Math.cos(angle-Math.PI/6),this.toy-headlen*Math.sin(angle-Math.PI/6));
        this.ctx.moveTo(this.tox, this.toy);
        this.ctx.lineTo(this.tox-headlen*Math.cos(angle+Math.PI/6),this.toy-headlen*Math.sin(angle+Math.PI/6));
    };

    function LoopLine(fromx, fromy, ctx){
        this.fromx = fromx + 15;
        this.fromy = fromy - 14;
        this.ctx = ctx;
    }

    LoopLine.prototype.draw = function() {
        var headlen = 10; // length of head in pixels
        var dx = 0;
        var dy = 100;
        var angle = Math.atan2(dy,dx);

        this.ctx.moveTo(this.fromx, this.fromy);
        this.ctx.lineTo(this.fromx, this.fromy - 15);
        this.ctx.arc(this.fromx - 15, this.fromy - 15, 15, 0, Math.PI, true);
        this.ctx.lineTo(this.fromx - 30, this.fromy);

        this.ctx.lineTo(this.fromx - 30-headlen*Math.cos(angle-Math.PI/6),this.fromy -headlen*Math.sin(angle-Math.PI/6));
        this.ctx.moveTo(this.fromx - 30, this.fromy);
        this.ctx.lineTo(this.fromx - 30-headlen*Math.cos(angle+Math.PI/6),this.fromy -headlen*Math.sin(angle+Math.PI/6));
    };        

    function CurvedLine(fromx, fromy, tox, toy, ctx){
        this.fromx = fromx;
        this.fromy = fromy;
        this.tox = tox;
        this.toy = toy;
        this.ctx = ctx;
    }

    CurvedLine.prototype.draw = function() {
        var headlen = 10; // length of head in pixels
        this.ctx.moveTo(this.fromx, this.fromy + 20);
        this.ctx.lineTo(this.fromx, this.fromy + 40);
        this.ctx.lineTo(this.tox, this.toy + 40);
        this.ctx.lineTo(this.tox, this.toy + 20);
        this.ctx.lineTo(this.tox - headlen/2, this.toy + 20 + headlen);
        this.ctx.moveTo(this.tox, this.toy + 20);
        this.ctx.lineTo(this.tox + headlen/2, this.toy + 20 + headlen);
    };

    function Transition(origin, destination, ctx){
        this.origin = origin;
        this.destination = destination;
        this.ctx = ctx;
        if(neighbors(origin, destination)){
            this.arrow  = new StraightLine(origin.x, centerY, destination.x, centerY, this.ctx);
        } else if(origin == destination){
            this.arrow = new LoopLine(origin.x, centerY, this.ctx);
        } else {
            this.arrow  = new CurvedLine(origin.x, centerY, destination.x, centerY, this.ctx);
        }
    }

    Transition.prototype.draw = function(){
        this.ctx.beginPath();
        this.arrow.draw();
        this.ctx.stroke();
    };

   

    function draw_states(){
        for(i = 0; i < automata.states.length; i++) {
            new State(automata.states[i].name, 
                        automata.states[i].is_initial_state, 
                        automata.states[i].is_final_state, 
                        ctx).draw();
        }
    };

    draw_states();

};