
var draw_graph = function(automata){

    var states_graphs = [];

    var canvas  = document.getElementById('graph-canvas');
    var ctx     = canvas.getContext('2d');
    var x       = 150;
    var centerY = canvas.height / 2;
    var radius = 20;
    var height_arrow = 20;
    var initial_state_circle;

    function neighbors(origin, destination){
        return Math.abs(origin.circle.x - destination.circle.x) == 100;
    };

    function Circle(ctx, x, y, radius){
       this.ctx    = ctx;
       this.x      = x;
       this.y      = y;
       this.radius = radius;
    }

    function draw_initial_state_triangle(){
      ctx.beginPath();
      ctx.moveTo(initial_state_circle.x - 22, initial_state_circle.y);
      ctx.lineTo(initial_state_circle.x - 40, initial_state_circle.y - 20);
      ctx.lineTo(initial_state_circle.x - 40, initial_state_circle.y + 20);
      ctx.closePath();
      ctx.stroke();
      ctx.fillStyle = 'white';
      ctx.fill();
    }

    Circle.prototype.draw = function(){
        this.ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
        this.ctx.fillStyle = 'white';
        this.ctx.fill();
        this.ctx.lineWidth = 2;
        this.ctx.strokeStyle = '#003300';
    };

    function NameState(ctx, name, x, y){
        this.ctx  = ctx;
        this.name = name;
        this.x    = x;
        this.y    = y;
    }

    NameState.prototype.draw = function(){
        this.ctx.textAlign    = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillStyle    = 'black';
        this.ctx.fillText(this.name, this.x, this.y);
    };

    function State(name, is_initial, is_final, transition_by_0, transition_by_1, ctx){
        this.ctx             = ctx;
        this.name            = new NameState(this.ctx, name, x, centerY);
        this.circle          = new Circle(this.ctx, x, centerY,radius);
        this.is_initial      = is_initial;
        this.is_final        = is_final;
        this.transition_by_0 = transition_by_0;
        this.transition_by_1 = transition_by_1;
        this.x               = x;
        x = x + 100;
    }

    State.prototype.draw = function(){
        this.ctx.beginPath();
        this.circle.draw();
        this.ctx.stroke();
        this.ctx.beginPath();
        if(this.is_final){
          new Circle(this.ctx, x - 100, centerY, radius - 5).draw();
        }
        this.name.draw();
        this.ctx.stroke();
    };

    function StraightLine(fromx, fromy, tox, toy, symbol, ctx){
        if(fromx < tox) {
            this.fromx = fromx+20;
            this.tox = tox-20;
        }else{
            this.fromx = fromx-20;
            this.tox = tox+20;
        }
        this.symbol = symbol;
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

    function LoopLine(fromx, fromy, symbol, ctx){
        this.symbol = symbol;
        this.fromx = fromx + 15;
        this.fromy = fromy - 14;
        this.ctx = ctx;
        if(this.symbol == '0'){
            this.symboly = 40;
        } else {
            this.symboly = 50;
        }
    }

    LoopLine.prototype.draw = function() {
        var headlen = 10; // length of head in pixels
        var dx = 0;
        var dy = 100;
        var angle = Math.atan2(dy,dx);  
        this.ctx.fillStyle = 'black';
        this.ctx.fillText(this.symbol, this.fromx - 15, this.fromy - this.symboly);
        this.ctx.moveTo(this.fromx, this.fromy);
        this.ctx.lineTo(this.fromx, this.fromy - 15);
        this.ctx.arc(this.fromx - 15, this.fromy - 15, 15, 0, Math.PI, true);
        this.ctx.lineTo(this.fromx - 30, this.fromy);

        this.ctx.lineTo(this.fromx - 30-headlen*Math.cos(angle-Math.PI/6),this.fromy -headlen*Math.sin(angle-Math.PI/6));
        this.ctx.moveTo(this.fromx - 30, this.fromy);
        this.ctx.lineTo(this.fromx - 30-headlen*Math.cos(angle+Math.PI/6),this.fromy -headlen*Math.sin(angle+Math.PI/6));
    };

    function CurvedLine(fromx, fromy, tox, toy, symbol, ctx){
        this.fromx = fromx;
        this.fromy = fromy;
        this.tox = tox;
        this.toy = toy;
        this.symbol = symbol;
        this.ctx = ctx;
        if(this.symbol == '0'){
            this.symboly = 10;
        } else {
            this.symboly = 20;
        }
        height_arrow = height_arrow + 20;
    }

    CurvedLine.prototype.draw = function() {
        var headlen = 10; // length of head in pixels
        this.ctx.fillStyle = 'black';
        this.ctx.fillText(this.symbol, this.fromx + 30, this.fromy - this.symboly);
        this.ctx.moveTo(this.fromx, this.fromy + 20);
        this.ctx.lineTo(this.fromx, this.fromy + height_arrow);
        this.ctx.lineTo(this.tox, this.toy + height_arrow);
        this.ctx.lineTo(this.tox, this.toy + 20);
        this.ctx.lineTo(this.tox - headlen/2, this.toy + 20 + headlen);
        this.ctx.moveTo(this.tox, this.toy + 20);
        this.ctx.lineTo(this.tox + headlen/2, this.toy + 20 + headlen);
    };

    function Transition(origin, destination, symbol, ctx){
        this.origin = origin;
        this.destination = destination;
        this.ctx = ctx;
        if(neighbors(origin, destination)){
            this.arrow  = new StraightLine(origin.x, centerY, destination.x, centerY, symbol, this.ctx);
        } else if(origin == destination){
            this.arrow = new LoopLine(origin.x, centerY, symbol, this.ctx);
        } else {
            this.arrow  = new CurvedLine(origin.x, centerY, destination.x, centerY, symbol, this.ctx);
        }
    }

    Transition.prototype.draw = function(){
        this.ctx.beginPath();
        this.arrow.draw();
        this.ctx.stroke();
    };

    function load_states(){
        states_graphs = [];
        for(i = 0; i < automata.states.length; i++){
          var state =
            new State(automata.states[i].name,
                  automata.states[i].is_initial_state,
                  automata.states[i].is_final_state,
                  automata.states[i].transition_by_0,
                  automata.states[i].transition_by_1,
                  ctx)
          states_graphs.push(state);
          if(automata.states[i].is_initial_state){
            initial_state_circle = state.circle;
          }
        }
    };

    function draw(){
        draw_states();
        draw_transitions();
        draw_initial_state_triangle();
    };

    function draw_states(){
        for(i = 0; i < states_graphs.length; i++){
            var state = states_graphs[i];
            state.draw();
        }
    };

    function draw_transitions(){
        var state;
        for(i = 0; i < states_graphs.length; i++){
            state = states_graphs[i];
            draw_transition(state, state.transition_by_0, '0');
            draw_transition(state, state.transition_by_1, '1');
        }
    }

    function draw_transition(state, transition, symbol){
        if((transition != 'None')){
            var destination = get_state(transition);
            new Transition(state, destination, symbol, ctx).draw();       
        }
    };

    function get_state(name){
        var state;
        for(j = 0; j < states_graphs.length; j++){
            state = states_graphs[j];
            if(state.name.name == name){
               return state;
            }
        }
    };


    load_states();
    draw();

};
