import React,{useState, useEffect, useRef} from "react";

function Stopwatch(){

    const [isRunning, setIsRunning] = useState(false);
    const [elapsedTime, setelapsedTime] = useState(0);
    const intervalIdRef = useRef(null);
    const startTimeRef = useRef(0);

    useEffect(() => {
        if(isRunning){
            intervalIdRef.current = setInterval(() => {
                setelapsedTime(Date.now() - startTimeRef.current)
            }, 10)
        }

        return () => {
            clearInterval(intervalIdRef.current);
        }
    }, [isRunning]);

    function start(){
        setIsRunning(true);
        startTimeRef.current = Date.now() - elapsedTime;
    }

    function stop(){
        setIsRunning(false);
    }

    function reset(){
        setelapsedTime(0);
        setIsRunning(false);
    }

    function formatTime(){

        let hours = Math.floor(elapsedTime / (1000 * 60 * 60));
        let minutes = Math.floor(elapsedTime / (1000 * 60) % 60);
        let seconds = Math.floor(elapsedTime / (1000) % 60);
        let miliseconds = Math.floor((elapsedTime % 1000) / 10);

        // hours = String(hours).padStart(2,"0");
        // minutes = String(minutes).padStart(2,"0");
        // seconds = String(seconds).padStart(2,"0");
        // miliseconds = String(miliseconds).padStart(2,"0");

        return `${padZero(hours)}:${padZero(minutes)}:${padZero(seconds)}:${padZero(miliseconds)}`;
    }

    function padZero(number){
        return number = number < 10 && number >= 0 ? "0" + number : number;
    }

    return(
        <div className="stopwatch">
            <div className="display">{formatTime()}</div>
            <div className="controls">
                <button onClick={start} className="startButton">START</button>
                <button onClick={reset} className="resetButton">RESET</button>
                <button onClick={stop} className="stopButton">STOP</button>
            </div>
        </div>
    );

}

export default Stopwatch